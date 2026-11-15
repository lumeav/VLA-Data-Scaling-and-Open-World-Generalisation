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