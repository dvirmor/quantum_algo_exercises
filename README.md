# quantum_algo_exercises
# 1
## 1.a

### QFT
![QFT](docs/QFT.png)

### Inverse QFT
![Inverse QFT](docs/Inverse_QFT.png)

## 1.b
![](docs/1_b.jpeg)

## 1.c
The result from b is encoded to the circuit with simple operations, then to reconstruct the original stage we used the inverse QFT and then $InverseQFT*QFT* \phi=\phi$. For more info see the src code: src/HW1.py

## 1.d
We can see that for j=2,6 the value is low, this is the excepted result from the original stage. 

![](docs/1_d.png)

# 2
![](docs/pdf/1.jpg)
![](docs/pdf/2.jpg)
![](docs/pdf/3.jpg)
![](docs/pdf/4.jpg)
![](docs/pdf/5.jpg)
![](docs/pdf/6.jpg)
![](docs/pdf/7.jpg)
![](docs/pdf/8.jpg)

# 3
![](docs/3.png)


# 4
## 4.a
![](docs/4_a.png)

## 4.b
### (i)
![](docs/overlap2.png)

### (ii)
![](docs/overlap3.png)

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
![](docs/z.png)
