## This repository contains figure sources and plotting scripts associated to the paper "Internal evolutionary conflicts: a mathematical primer".

The repo is organised into two folders:

1. `FigureSources` contains the OmniGraffle and svg files that were used to collect the different panels and make figures. 
2. `Scripts` contains Python scripts that we used to plot the curves of interest from the main and supplementary text.

### FigureSources

All figures that are in the manuscript can be found by searching in this folder for the file figure `Figure<number>_<description>.pdf`.

* Figure 1: conceptual, no scripts required.
* Figure 2: conceptual, no scripts required. 
* Figure 3: panel (a) conceptual, others require the output of `Scripts/invasion-criteria.py` with the flag `drive=True`.
* Figure 4: panel (a) conceptual, others require the output of `Scripts/invasion-criteria.py` with the flag `imprinting=True`.
* Figure 5: panel (a) conceptual but made using `Scripts/plot-2-gaussian.py`, other panels require the output of `Scripts/invasion-criteria.py` with the flag `sexualantagonism=True`.
* Figure S1: requires the output of `Scripts/numerical_keaney.py`, saved to same folder, called `sex_specific_drive_traj.pdf`.
* Figure S2: requires the output of `Scripts/numerical_keaney.py`, saved to same folder, called `multiple_mate_drive_hmap.pdf`.

### Scripts

* `invasion-criteria.py`: used to plot the invasion and other criteria referred to in the main text. Creates non-conceptual panels of Figures 3,4,5.
* `plot-2-gaussians.py`: creates panel (a) of Figure 5 on sexual antagonism.
* `numerical_keaney.py`: creates the figures in the supplementary figures; both deal with extensions to the simple meiotic drive model of the main text.
