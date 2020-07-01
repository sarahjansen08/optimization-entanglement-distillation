# Optimization-entanglement-distillation

Optimization of entanglement distillation protocols via group theoretical tools.

MAIN FILES <br>
<b>Transversal.ipynb</b>: Given an input (n > 1), this file creates a transversal of right cosets of the subgroup that preserves distillation statistics in the Clifford group. 
This is done in the binary picture. <br>
<b>Distillation_statistics.ipynb</b>: Given a transversal and the corresponding n > 1, this file calculates the distillation statistics.
Based on a criterium (fidelity / success probability / rate) the function best_protocol returns a protocol that optimizes this criterium.
Moreover, the function sucprob_fid_lists returns all possible combinations of success probability and fidelity that can be obtained. <br>
<b>Symplectic-to-clifford.ipynb</b>: Given a symplectic matrix, this file finds a corresponding circuit in terms of Clifford gates. <br>

PLOTS <br>
<b>fidsuc_plot.py</b>: Function to find the pareto front of a set of two-dimensional data points; used in the success probability - fidelity plots. <br>
<b>plots_isotropic.py</b>: Creates success probability - fidelity plots for the isotropic input states with Fin = 0.6, 0.7, 0.8, 0.9. <br>
<b>plots_bell_diagonal.py</b>: Creates success probability - fidelity plots for the Bell diagonal state. <br>
<b>rate.py</b>: Creates plot with the best achievable rate for n = 1, 2, 3, 4. <br>

DATA <br>
<b>2_transversal_inv.sobj</b>: Transversal for n = 2. The inverse symplectic matrices are saved here. <br>
<b>3_transversal_inv.sobj</b>: Transversal for n = 3. <br>
<b>4_transversal_inv.sobj</b>: Transversal for n = 4. <br>
