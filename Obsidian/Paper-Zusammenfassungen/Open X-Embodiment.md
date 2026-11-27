**Kann ein Roboter von den Erfahrungen anderer Roboter lernen, auch wenn diese eine andere Bauweise, Sensorik und Steuerung besitzen?**

Die Autoren übertragen dafür ein Prinzip aus dem Training großer Sprach- und Bildmodelle auf die Robotik: Statt für jeden Roboter und jede Aufgabe ein eigenes Modell zu trainieren, werden möglichst viele unterschiedliche Roboterdaten zusammengeführt und zum Training eines gemeinsamen Modells verwendet.

Das Ergebnis ist das Projekt **Open X-Embodiment (OXE)** und die darauf trainierten Modelle **RT-1-X und RT-2-X**.

Die wichtigste Erkenntnis: Das gemeinsame Training mit Daten unterschiedlicher Roboter kann die Leistungsfähigkeit einzelner Roboter verbessern. Dieses Phänomen wird als _Positive Transfer_ bezeichnet.


---

## **Ausgangsproblem**

Klassischerweise werden Robotermodelle sehr spezifisch trainiert:

- Ein Modell für einen bestimmten Robotertyp.
- Ein Modell für eine bestimmte Umgebung.
- Ein Modell für eine bestimmte Aufgabe.

Das führt zu mehreren Problemen:
1. **Begrenzte Datenmenge:** Einzelne Forschungsgruppen verfügen meist nur über relativ kleine Datensätze.
2. **Geringe Generalisierung:** Ein Modell funktioniert häufig nur mit dem Roboter und in der Umgebung, für die es trainiert wurde.
3. **Hoher Trainingsaufwand:** Neue Roboter und Aufgaben benötigen häufig neue Trainingsdaten.
    

Bei Sprachmodellen funktioniert ein anderer Ansatz: Große, heterogene Datenmengen ermöglichen das Erlernen allgemeiner Fähigkeiten, die anschließend auf neue Aufgaben übertragen werden können. => Die Autoren wollen dieses Prinzip auf physische Roboter übertragen.


## **Open X-Embodiment Dataset**

- **1 Mio.+** Robot-Trajektorien
- **22** Roboter-Embodiments
- **60** Einzelne Datensätze
- **34** Forschungslabore bei der Datensammlung

Die Daten stammen von unterschiedlichen Robotern und unterscheiden sich teilweise erheblich hinsichtlich ihrer mechanischen Konstruktion und ihrer Sensorik. Die Datensätze enthalten unterschiedliche Manipulationsaufgaben:

- Greifen und Platzieren
- Schieben und Ziehen
- Öffnen und Schließen
- Einsetzen und Zusammenbauen
- Navigation und Objektmanipulation

**Wichtig:** Der Datensatz besteht nicht aus künstlich erzeugten Simulationen, sondern überwiegend aus realen Roboterinteraktionen. Die Daten werden im einheitlichen RLDS-Format (RLDS = Reinforcement Learning Datasets) bereitgestellt.


---

## Experimentelle Ergebnisse

Die Autoren untersuchen drei zentrale Fragen:

1. Verbessert das gemeinsame Training die Leistung einzelner Roboter?
2. Können Roboter Fähigkeiten anderer Roboter übernehmen?
3. Welche Rolle spielen Modellgröße und Vortraining?

Dafür führen sie insgesamt **3.600 Evaluierungstests mit sechs verschiedenen Robotern** durch.


### **Ergebnis A: Positive Transfer**

RT-1-X wird mit Daten verschiedener Roboter trainiert und anschließend auf einzelnen Robotern getestet.

Das Ergebnis:

- Bei vier von fünf untersuchten Datensätzen mit relativ wenigen Trainingsdaten verbessert RT-1-X die Leistung gegenüber den jeweiligen spezialisierten Ausgangsmodellen.
- Im Durchschnitt zeigt RT-1-X laut Autoren eine etwa 50 % höhere Erfolgsrate als die ursprünglichen Methoden.

Das bedeutet: Ein Roboter profitiert von Erfahrungen, die mit anderen Robotern gesammelt wurden.


---

### **Ergebnis B: Neue Fähigkeiten durch andere Roboter**

Besonders interessant ist das Experiment mit RT-2-X.

Hier wird untersucht, ob ein Google-Roboter Fähigkeiten ausführen kann, die ausschließlich in den Trainingsdaten eines anderen Roboters vorkommen.

Beispiel:

- Der WidowX-Roboter besitzt Trainingsdaten für bestimmte Manipulationsaufgaben.
- Der Google-Roboter besitzt diese Fähigkeiten in seinen eigenen Trainingsdaten nicht.
- RT-2-X wird mit den Daten beider Roboter trainiert.
- Anschließend wird getestet, ob der Google-Roboter die zusätzlichen Aufgaben ausführen kann.

Zentrales Ergebnis

RT-2-X erreicht bei diesen zusätzlichen Fähigkeiten eine Erfolgsrate von **75,8 %**, während das ursprüngliche RT-2-Modell nur **27,3 %** erreicht.

Das entspricht ungefähr einer Verdreifachung.

|Modell|Erfolgsrate|
|---|---|
|RT-2|27,3 %|
|RT-2-X|75,8 %|
|RT-2-X ohne Bridge-Datensatz|42,8 %|

Das Entfernen der WidowX-Trainingsdaten (Bridge) reduziert die Leistung erheblich. Das ist ein deutlicher Hinweis darauf, dass das Modell tatsächlich Fähigkeiten zwischen Robotern überträgt.


---

Die Autoren zeigen außerdem, dass ein größeres Modell erforderlich sein kann, um heterogene Roboterdaten effektiv zu nutzen.

RT-1-X reicht bei großen Datensätzen teilweise nicht aus und kann gegenüber einem spezialisierten Modell schlechter abschneiden.

RT-2-X mit 55 Milliarden Parametern kann dagegen von den zusätzlichen Daten profitieren.

Auch das Web-Vortraining ist wichtig: Ein RT-2-X-Modell, das von Grund auf trainiert wird, erzielt in den untersuchten Emergent-Skills-Tests 0 %, während die web-vortrainierte Variante deutlich bessere Ergebnisse erreicht.


![[Pasted image 20261116065306.png]]


## Grenzen und offene Probleme

![[Pasted image 20261116065425.png]]


Ein besonders wichtiger Punkt: **Positive Transfer ist nicht automatisch garantiert.** Mehr Daten unterschiedlicher Roboter können helfen, aber auch zu schlechteren Ergebnissen führen, wenn das Modell nicht genügend Kapazität besitzt oder die Daten nicht gut zusammenpassen.


![[Pasted image 20261116065645.png]]