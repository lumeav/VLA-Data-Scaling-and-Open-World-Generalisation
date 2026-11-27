
## Kernfrage

**Wie können Roboter lernen, Manipulationsaufgaben auch in unbekannten Umgebungen, mit unbekannten Objekten und unter veränderten Bedingungen zuverlässig auszuführen?**


## Hypothese vor dem Paper

Nicht nur die Menge der Trainingsdaten ist entscheidend, sondern vor allem deren Vielfalt.


Bisherige Roboterdatensätze enthalten häufig viele Demonstrationen, die aber unter sehr ähnlichen Bedingungen aufgenommen wurden. Ein Modell lernt dadurch möglicherweise nicht die eigentliche Manipulationsfähigkeit, sondern passt sich an bestimmte Umgebungen, Kameraperspektiven und Objektpositionen an.

Die Autoren entwickeln deshalb **DROID (Distributed Robot Interaction Dataset)**: einen großen, dezentral gesammelten Datensatz mit realen Roboterinteraktionen aus zahlreichen unterschiedlichen Umgebungen, um Robotermodelle robuster und besser generalisierbar zu machen.


## Ausgangsproblem

In der klassischen Robotik werden Trainingsdaten häufig unter kontrollierten Laborbedingungen gesammelt.

Beispielsweise:

- Ein Roboter steht an einem festen Tisch.
- Eine Kamera besitzt eine unveränderte Perspektive.
- Objekte befinden sich an bekannten Positionen.
- Die Beleuchtung bleibt konstant.
- Aufgaben wiederholen sich häufig.

![[Pasted image 20261116070144.png]]


## DROID-Datensatz 

![[Pasted image 20261116070251.png]]

Beispielsweise kann dieselbe Handlung beschrieben werden als:

- „Pick up the cup.“
- „Grab the mug.“
- „Move the cup to the other side.“
    
Dadurch wird auch die sprachliche Vielfalt erhöht.


Es wird immer der selbe Roboter für die Aufnahme der Daten verwendet.


## Ergebnisse

### **Ergebnis A: DROID verbessert die Erfolgsrate**

Zentrales Ergebnis

Das Training mit DROID verbessert die durchschnittliche Erfolgsrate gegenüber den Vergleichsverfahren:

- **+22 Prozentpunkte** im In-Distribution-Test gegenüber dem nächstbesten Verfahren.
- **+17 Prozentpunkte** im Out-of-Distribution-Test gegenüber dem nächstbesten Verfahren.

Das ist besonders relevant, weil die Vorteile auch bei unbekannten oder veränderten Bedingungen auftreten.



### **Ergebnis B: Robustheit gegenüber unbekannten Situationen**

Die Autoren verändern gezielt die Testbedingungen.

Beispiele:

- Zusätzliche Gegenstände werden auf den Tisch gelegt.
- Andere Chipsverpackungen werden verwendet.
- Unbekannte Objekte werden manipuliert.
- Die Kameraposition wird verändert.
- Zusätzliche Ablenkungsobjekte werden in die Umgebung eingebracht.
    

Die Modelle, die ausschließlich mit aufgabenspezifischen Daten trainiert wurden, verlieren dabei deutlich an Leistung.

Die mit DROID trainierten Modelle bleiben wesentlich robuster.


### **Ergebnis C: Vielfalt ist wichtiger als reine Datenmenge**

Der Datensatz mit höherer Szenenvielfalt erzielt bessere Ergebnisse bei den Out-of-Distribution-Tests.


### Einschränkungen

![[Pasted image 20261116071424.png]]


## wichtigsten Erkenntnisse

![[Pasted image 20261116071511.png]]