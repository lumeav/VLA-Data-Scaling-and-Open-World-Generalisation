**Kernfrage:** Können Roboter Fähigkeiten aus menschlichen Videos lernen, ohne dass jedes Video manuell in Roboteraktionen übersetzt werden muss?


## Problemstellung

Roboterdaten sind teuer: Ein Roboter muss für jede gewünschte Fähigkeit zunächst teleoperiert oder anderweitig trainiert werden. Menschliche Videos sind dagegen vergleichsweise einfach und umfangreich zu sammeln.

Das Problem: Mensch und Roboter besitzen unterschiedliche Körper, Kameraperspektiven und Bewegungsmöglichkeiten. Ein menschliches Video lässt sich deshalb nicht ohne Weiteres in Roboteraktionen übersetzen.

Die Autoren untersuchen, ob ein VLA-Modell diese Unterschiede selbst überbrücken kann – durch vielfältiges Vortraining statt durch speziell entwickelte Alignment-Verfahren.


## **Datenerfassung:**

- Eine Kopfkamera zeichnet die Umgebung auf.
- Zwei Handgelenkkameras erfassen die Interaktion mit Objekten.
- Visual SLAM rekonstruiert die Bewegung der Kopfkamera im Raum.
- Computer Vision verfolgt 17 dreidimensionale Keypoints pro Hand.
- Die Videos werden mit sprachlichen Beschreibungen von Teilaufgaben annotiert.

Insgesamt sammeln die Autoren etwa **14 Stunden menschliche Demonstrationen** für vier Aufgaben: Tisch abräumen, Gewürze sortieren, eine Kommode aufräumen und Eier nach Farben sortieren.


## Lernziele des Modells

|Lernziel|Bedeutung|
|---|---|
|Low-Level Action Prediction|Vorhersage konkreter Bewegungen anhand rekonstruierter Handbewegungen|
|High-Level Subtask Prediction|Vorhersage sprachlicher Teilaufgaben, z. B. „Nimm die Gewürzflasche“|


## Ergebnisse

|Generalisierung|Nur Roboterdaten|Mensch + Roboter|Verbesserung|
|---|---|---|---|
|Gewürze aufräumen (neue Szene)|32 %|71 %|+39 Prozentpunkte|
|Kommode aufräumen (neue Szene)|25 %|50 %|+25 Prozentpunkte|
|Tisch abräumen (neue Objekte)|53 %|63 %|+10 Prozentpunkte|
|Eier nach Farbe sortieren (neue Aufgabe)|57 %|78 %|+21 Prozentpunkte|

Die Ergebnisse zeigen, dass menschliche Videos nicht nur die visuelle Erkennung verbessern, sondern auch neue Aufgaben und Handlungskonzepte vermitteln können. Besonders deutlich wird das beim Sortieren der Eier: Ohne menschliche Videos kann der Roboter Eier zwar greifen und ablegen, versteht aber nicht das Sortierprinzip. Mit menschlichen Videos steigt die Sortiergenauigkeit von 57 auf 78 %.


## Warum funktioniert das?

Die Autoren zeigen, dass der Transfer stark von der Vielfalt des robotischen Vortrainings abhängt:

- Bei keinem oder wenig Vortraining kann das Modell kaum von menschlichen Videos profitieren.
- Mit zunehmender Vielfalt an Aufgaben, Szenen und Robotertypen wird der Transfer deutlich besser.
- Besonders hilfreich ist Cross-Embodiment-Pretraining, also Vortraining mit unterschiedlichen Robotertypen.

## wichtige Erkenntnisse

![[Pasted image 20261116134629.png]]


## Limitationen

![[Pasted image 20261116134558.png]]