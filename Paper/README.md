# Team 3: Daten, Skalierung und Open-World-Generalisierung

Ausarbeitung im MSI-Seminar *Vision-Language-Action-Modelle in der Robotik*, WS 2026/27, HTWG Konstanz.

**Leitfrage:** Welche Daten machen ein VLA generalisierbar, und wie verhindert man, dass das VLM sein Weltwissen verliert?

**Querschnittsthema für alle Teams:** Wie belastbar ist die Evaluation?

**Kernpapers:**
- Open X-Embodiment: Robotic Learning Datasets and RT-X Models, Open X-Embodiment Collaboration 2023 (https://arxiv.org/abs/2310.08864), `oxe2023`
- DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset, Khazatsky et al. 2024 (https://arxiv.org/abs/2403.12945), `khazatsky2024droid`
- π0.5: a Vision-Language-Action Model with Open-World Generalization, Physical Intelligence 2025 (https://arxiv.org/abs/2504.16054), `pi2025pi05`
- Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better, Driess et al. 2025 (https://arxiv.org/abs/2505.23705), `driess2025ki`

**Zusatzpapers:**
- Emergence of Human to Robot Transfer in Vision-Language-Action Models, Kareer et al. 2025 (https://arxiv.org/abs/2512.22414), `kareer2025h2r`
- π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities, Physical Intelligence 2026 (https://arxiv.org/abs/2604.15483), `pi2026pi07`

## Vorgaben

- 6 Seiten ohne Literaturverzeichnis, IEEE-Format (https://www.ieee-ras.org/publications/t-ase/), Survey-Stil
- Sprache: **Englisch**
- Abgabe: siehe Moodle

## Aufbau

| Datei | Inhalt |
|---|---|
| `main.tex` | Titel, Autoren, Einbinden der Abschnitte |
| `sections/00_abstract.tex` | Abstract und Index Terms |
| `sections/01_introduction.tex` | Introduction |
| `sections/02_examples.tex` | Beispiele im IEEE-Stil (Abschnitte, Zitate, Listen, Gleichungen, Abbildungen, Tabellen, Algorithmen), durch eigene Abschnitte ersetzen |
| `sections/03_conclusion.tex` | Conclusion |
| `sections/04_acknowledgment.tex` | Acknowledgment mit Angabe der genutzten KI-Werkzeuge |
| `tables/` | Tabellen, eine Datei pro Tabelle (Beispiele: `example.tex`, `example_wide.tex`) |
| `refs.bib` | Literatur |
| `figures/` | Abbildungen, gemeinsamer Plot-Stil `ieee.mplstyle` (Beispiel: `example_plot.py` → `example_plot.pdf`) |

Die Gliederung legt ihr selbst fest. Eigene Abschnitte als Dateien unter `sections/` anlegen und in `main.tex` einbinden. `sections/02_examples.tex` zeigt die üblichen Elemente im IEEE-Stil und wird vor der Abgabe entfernt, ebenso die Beispieldateien in `tables/` und `figures/` (`ieee.mplstyle` bleibt).

## Bauen

```
make          # PDF nach build/main.pdf
make pages    # Seitenzahl
make check    # schlägt fehl, solange noch \TODO-Platzhalter im PDF stehen
```

Voraussetzung ist eine TeX-Distribution mit `latexmk` (z.B. TeX Live). Alternativ das Repo als ZIP in Overleaf hochladen, `main.tex` ist das Hauptdokument.

## Hinweise

- Literatur nur über `refs.bib` zitieren (`\cite{...}`). Die Kernpapers, Zusatzpapers und Surveys sind schon eingetragen. Wo es eine veröffentlichte Version gibt, den arXiv-Eintrag darauf umstellen (z.B. BibTeX von dblp.org).
- Abbildungen nach `figures/`, möglichst als PDF. Plots mit Python mit `plt.style.use("figures/ieee.mplstyle")` erstellen: Schrift wie im Fließtext (Times, 10 pt), Spaltenbreite, Farben aus `tab20c` (ein Farbton pro Gruppe, hellere Abstufungen für Varianten). Übernommene Abbildungen immer mit Quelle in der Bildunterschrift.
- Im Acknowledgment (`sections/04_acknowledgment.tex`) angeben, welche KI-Werkzeuge (Name, Version) wofür, in welchen Abschnitten und in welchem Umfang genutzt wurden, oder dass keine genutzt wurden. Die Verantwortung für den Inhalt liegt bei euch.
- Vor der Abgabe müssen alle `\TODO{...}` entfernt sein (`make check`).
- Regelmäßig committen, beide Teammitglieder. Build-Dateien und PDFs nicht einchecken (`.gitignore`).
