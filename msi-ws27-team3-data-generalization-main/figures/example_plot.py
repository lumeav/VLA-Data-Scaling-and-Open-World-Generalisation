"""Erzeugt figures/example_plot.pdf. Aufruf aus dem Repo-Wurzelverzeichnis: python3 figures/example_plot.py"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

here = Path(__file__).parent
plt.style.use(here / "ieee.mplstyle")
tab20c = plt.get_cmap("tab20c").colors

# tab20c eignet sich für gruppierte Daten: ein Farbton pro Gruppe, Abstufungen für Varianten.
x = np.linspace(0, 10, 200)
fig, ax = plt.subplots(figsize=(3.5, 2.6))
ax.plot(x, np.sin(x) * np.exp(-x / 8), color=tab20c[0], label="Group 1a")
ax.plot(x, 0.7 * np.sin(x) * np.exp(-x / 8), color=tab20c[2], label="Group 1b")
ax.plot(x, 0.6 * np.cos(x) * np.exp(-x / 6), "--", color=tab20c[4], label="Group 2a")
ax.plot(x, 0.4 * np.cos(x) * np.exp(-x / 6), "--", color=tab20c[6], label="Group 2b")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend(ncol=2, loc="lower center", bbox_to_anchor=(0.5, 1.0), handlelength=1.5, columnspacing=1.0)
fig.savefig(here / "example_plot.pdf")
