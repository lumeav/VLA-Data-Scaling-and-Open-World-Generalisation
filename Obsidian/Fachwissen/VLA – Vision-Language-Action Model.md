
**VLA** steht für **Vision-Language-Action**. Es bezeichnet ein KI-Modell, das **Bilder/Video, Sprache und konkrete Handlungen** miteinander verbindet.

## Kernpaper: RT-2: Vision-Language-Action Models – Transfer Web Knowledge to Robotic Control

- **Kernidee:** Ein Roboter lernt, seine visuelle Umgebung zu verstehen, menschliche Anweisungen zu interpretieren und daraus direkt motorische Aktionen abzuleiten.
- von Google Deepmind 2023 veröffentlicht

## **1. Was bedeutet VLA?**

Ein VLA-Modell verarbeitet drei Informationsarten:

| Bestandteil | Bedeutung             | Beispiel                        |
| ----------- | --------------------- | ------------------------------- |
| Vision      | Was sehe ich?         | Eine Kamera erkennt eine Tasse. |
| Language    | Was soll ich tun?     | „Nimm die Tasse.“               |
| Action      | Wie führe ich es aus? | Arm bewegen, Greifer schließen. |

## **2. Wie funktioniert RT-2 technisch?**

Die zentrale Idee ist relativ einfach, aber sehr wirkungsvoll:

**Eine Roboterbewegung wird in eine Token-Sequenz umgewandelt. Dadurch kann ein Sprachmodell lernen, Roboteraktionen genauso vorherzusagen wie Wörter.**

![[Pasted image 20261115143613 1.png]]


---

## Wo liegen die Grenzen?

Das Paper zeigt auch, dass ein VLA nicht automatisch neue körperliche Fähigkeiten entwickelt.

|Problem|Erklärung|
|---|---|
|Begrenzte Motorik|Das Modell kann primär Bewegungen ausführen, die es aus Roboterdaten gelernt hat.|
|Geschwindigkeit|Das 55-Milliarden-Parameter-Modell erreicht nur ca. 1–3 Aktionen pro Sekunde.|
|Datenabhängigkeit|Für neue physische Fähigkeiten braucht es weiterhin geeignete Roboterdaten.|
|Hardwareabhängigkeit|Die vorhergesagten Bewegungen müssen zum jeweiligen Roboter und seinen Steuerparametern passen.|


---

## Begriffe 

**VLM = Vision-Language Model**

Ein VLM ist ein KI-Modell, das Bilder und Sprache miteinander verknüpfen kann.

Es versteht gleichzeitig:

- **Vision:** Visuelle Informationen, beispielsweise Bilder einer Kamera.
- **Language:** Sprachliche Informationen, beispielsweise Fragen oder Anweisungen.

### **Was ist ein VLA?**
**VLA = Vision-Language-Action Model**

Ein VLA erweitert das Konzept eines VLM um die Fähigkeit, Aktionen zu erzeugen.


### WAM = World Action Model

Das ist eine Weiterentwicklung des VLA-Ansatzes in der Robotik. Der wesentliche Unterschied: Ein WAM lernt nicht nur, welche Aktion es ausführen soll, sondern auch, **wie sich die physische Welt durch diese Aktion verändern wird.**


![[Pasted image 20261115144501 1.png]]

![[Pasted image 20261115144635 1.png]]

WAM = Thema 6

Ein WAM (World-Action Model) verbindet zwei Dinge:

1. **Roboteraktionen:** Was soll der Roboter tun?
2. **Weltveränderung:** Wie verändert sich die Umgebung durch diese Aktion?

=> **Roboter können neue Bewegungen und Aufgaben besser lernen, ohne jede einzelne Bewegung vorher als Roboterdemonstration gesehen haben zu müssen.**