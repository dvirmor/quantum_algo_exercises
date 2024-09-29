# quantum_algo_exercises
## 4.b
### (ii)
Note that
$$\Delta_3(\Pi_\phi, |1\rangle\langle 1| \Pi_\psi)$$
is computed as:<br>
$\Delta_3(\Pi_\phi, |1\rangle\langle 1| \Pi_\psi)$ = $\text{Tr}(\Pi_\phi |1\rangle\langle 1| \Pi_\psi)$ <br>
= $\text{Tr}(\langle 1| \Pi_\psi \Pi_\phi |1\rangle)$ <br>
= ${\Pi_\psi \Pi_\phi} (2, 2)$ <br>
= $\text{Tr}(\Pi_\psi \Pi_\phi) - (\Pi_\psi \Pi_\phi)(1,1)$ <br>
= $\Delta_2(\Pi_\psi \Pi_\phi) - \Delta_3(\Pi_\phi |0\rangle\langle 0| \Pi_\psi)$ <br>

Since the right-hand side has already been calculated, we can now compute the left-hand side directly without any further measurements.
### Answer
Recall that $Z$ is defined as:

$$Z = 1 \cdot |0\rangle\langle 0| + (-1) \cdot |1\rangle\langle 1|$$


We will now use the identity proven in part 4(a), along with the previously computed values of $\Delta_2$ and $\Delta_3$, to compute $Z_w$:

$$Z_w = \frac{\Delta_3(\Pi_\phi |0\rangle\langle 0| \Pi_\psi)}{\Delta_2(\Pi_\phi \Pi_\psi)} - \frac{\Delta_3(\Pi_\phi |1\rangle\langle 1| \Pi_\psi)}{\Delta_2(\Pi_\phi \Pi_\psi)}$$

The result $Z_w$ can be computed directly using the above equation.
