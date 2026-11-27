

## Kernfrage

**Wie kann man die semantischen Fähigkeiten eines vortrainierten Vision-Language Models erhalten und gleichzeitig eine schnelle, präzise und kontinuierliche Robotersteuerung ermöglichen?**

## Problem

Das Problem entsteht durch die Kombination zweier unterschiedlicher Anforderungen:

- Ein Vision-Language Model (VLM) benötigt große Transformer-Netzwerke, um Sprache und Bilder zu verstehen.
- Ein Roboter benötigt kontinuierliche Bewegungsbefehle, die mit hoher Frequenz und geringer Latenz erzeugt werden müssen.


Bisherige Ansätze lösen das häufig durch zusätzliche Action Experts, die kontinuierliche Bewegungen mittels Diffusion oder Flow Matching generieren. Dabei entsteht jedoch ein Problem: Die neu initialisierten Action Experts können beim Training die bereits erlernten Repräsentationen des vortrainierten VLM negativ beeinflussen.

Die Autoren nennen dieses Problem eine Form von _Gradient Interference_.
Ihre Lösung heißt **Knowledge Insulation**.

### Idee:

Das vortrainierte VLM soll weiterhin lernen, Roboteraktionen vorherzusagen, aber die Gradienten des neu hinzugefügten kontinuierlichen Action Experts dürfen nicht direkt in das VLM-Backbone zurückfließen.

Dadurch sollen drei Vorteile gleichzeitig erreicht werden:
1. Schnelleres Training.
2. Schnelle und präzise Robotersteuerung.
3. Bessere Übertragung des vortrainierten semantischen Wissens auf Robotikaufgaben.



## Ausgangsproblem: Der Konflikt zwischen Sprachmodell und Robotersteuerung



### **Ansatz A: Diskrete Aktionsvorhersage**

Die kontinuierlichen Bewegungen werden in diskrete Tokens umgewandelt.

Beispielsweise wird eine Bewegung in einzelne Wertebereiche aufgeteilt:

- Position: Token 1
- Orientierung: Token 2
- Greiferöffnung: Token 3

Das Modell sagt diese Tokens autoregressiv voraus, ähnlich wie ein Sprachmodell Wörter generiert.

**Vorteile:**

- Nutzt die bestehende Transformer-Architektur.
- Ermöglicht effizientes Training mit Next-Token-Prediction.
- Kann gut mit Sprach- und Bilddaten kombiniert werden.

**Nachteile:**

- Informationsverlust durch Diskretisierung.
- Langsame autoregressive Inferenz.
- Begrenzte Präzision bei dynamischen Bewegungen.



### **Ansatz B: Kontinuierliche Aktionsvorhersage**

Hier werden Aktionen direkt als kontinuierliche Werte generiert.

Dafür verwenden moderne VLA-Modelle beispielsweise:

- Diffusion
- Flow Matching
- Spezialisierte Action Experts
    

**Vorteile:**

- Präzisere kontinuierliche Bewegungen.
- Schnelle Generierung ganzer Aktionssequenzen.
- Geeignet für dynamische und feinmotorische Aufgaben.

**Nachteile:**

- Zusätzliche Parameter müssen neu trainiert werden.
- Die Gradienten dieser Module können das vortrainierte VLM negativ beeinflussen.
- Das Training kann deutlich langsamer konvergieren.

## Lösung: Knowledge Insulation

Die vorgeschlagene Architektur besteht aus zwei miteinander interagierenden Komponenten:

1. **VLM Backbone:** Verarbeitet Bilder, Sprache und diskrete Aktions-Tokens.
2. **Action Expert:** Generiert kontinuierliche Roboteraktionen mittels Flow Matching.

### **Wie funktioniert das?**

Während des Trainings werden beide Komponenten gleichzeitig trainiert:
- Das VLM sagt diskrete Aktionen voraus.
- Der Action Expert generiert kontinuierliche Aktionen.
- Beide Komponenten können Informationen über Attention austauschen.
- Die Gradienten des Action Experts werden jedoch daran gehindert, in das VLM-Backbone zurückzufließen.


## Ergebnisse

### **Ergebnis A: Bessere Trainingsgeschwindigkeit**

Das vorgeschlagene Verfahren konvergiert deutlich schneller als ein Modell, das ausschließlich mit Flow Matching trainiert wird.

**π₀ benötigt ungefähr 7,5-mal so viele Trainingsschritte, um ein vergleichbares Leistungsniveau zu erreichen.**

Das neue Verfahren erreicht damit eine Trainingsgeschwindigkeit, die ungefähr der von π₀-FAST entspricht.

### **Ergebnis B: Schnellere Inferenz**

|Modell|Steuerungsfrequenz|
|---|---|
|Autoregressives VLA (π₀-FAST)|ca. 1,3 Hz|
|Kontinuierliches VLA (π₀)|ca. 10 Hz|
|Vorgeschlagenes Verfahren|ca. 10 Hz|

Ein weiteres Beispiel verdeutlicht das Problem:

π₀-FAST benötigt auf einer RTX 4090 ungefähr 750 ms, um eine Aktionssequenz für eine Sekunde Roboterbewegung zu generieren.

Das ist für dynamische Echtzeitsteuerung problematisch.
Der kontinuierliche Action Expert vermeidet diese langsame autoregressive Dekodierung.

### **Ergebnis C: Bessere Sprachbefolgung**

Ein wesentliches Experiment untersucht, ob der Roboter tatsächlich die sprachliche Instruktion befolgt.

Beispiel:

„Lege den Löffel in den Abfalleimer.“

Ein Modell könnte stattdessen ein anderes Objekt greifen, das visuell ähnlich oder statistisch häufiger in den Trainingsdaten vorkommt.

Die Autoren zeigen:

- π₀ hat Schwierigkeiten, die konkrete Instruktion zuverlässig zu befolgen.
- Joint Training ohne Knowledge Insulation verschlechtert die Sprachbefolgung.
- π₀-FAST folgt Sprache besser, ist aber langsam.
- Das vorgeschlagene Verfahren verbindet gute Sprachbefolgung mit schneller Steuerung.

Das ist wichtig, weil Robotermodelle nicht nur visuelle Muster reproduzieren dürfen. Sie müssen tatsächlich die gewünschte Handlung ausführen.


### **Ergebnis D: Generalisierung auf unbekannte Objekte**

Die Autoren untersuchen, ob allgemeines Wissen aus VLM-Daten auf physische Roboteraktionen übertragen werden kann.

Dazu wird ein mobiler Roboter mit unbekannten Haushaltsgegenständen konfrontiert.

Die Aufgabe lautet, Gegenstände von einer Küchenarbeitsplatte in eine geöffnete Schublade zu legen.

Die Objekte wurden während des Trainings nicht gesehen.

**Ergebnis:** Das zusätzliche Training mit allgemeinen Vision-Language-Daten verbessert die Generalisierung auf unbekannte Objektkategorien deutlich.

## Grenzen

![[Pasted image 20261116075727.png]]

## Erkenntnisse 

![[Pasted image 20261116075800.png]]