from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile
import numpy as np
import matplotlib.pyplot as plt


def cycle_test_circuit(alpha):
    qc = QuantumCircuit(4, 1)
    qc.h(0)
    qc.ry(alpha, 1)
    qc.h(3)
    qc.cswap(0, 1, 2)
    qc.cswap(0, 2, 3)
    qc.h(0)
    qc.measure(0, 0)
    return qc


def swap_test_circuit(alpha):
    qc = QuantumCircuit(3, 1)
    qc.h(0)
    qc.h(2)
    qc.ry(alpha, 1)
    qc.cswap(0, 1, 2)
    qc.h(0)
    qc.measure(0, 0)
    return qc


def run_circuit(qc):
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)

    # The probability of ancilla being in state |0> gives the overlap as 1 - 2*P(ancilla=1)
    p0 = counts.get('0', 0) / 1024
    overlap_squared = 2 * p0 - 1  # Weak value reconstruction
    return overlap_squared


def compute_and_plot_overlaps2(alphas):
    # List to store the results
    overlaps_2 = []

    # Run the SWAP test for each value of theta
    for alpha in alphas:
        qc = swap_test_circuit(alpha)
        overlap = run_circuit(qc)
        overlaps_2.append(overlap)

    # Plotting the results
    plt.plot(alphas, overlaps_2, color='b')
    plt.xlabel(r'$\theta$ (rad)')
    plt.ylabel(r'$| \langle \phi | \psi \rangle |^2$')
    plt.title('SWAP Test Overlap vs. $\\theta$')
    plt.grid(True)
    plt.show()

    return np.array(overlaps_2)


def compute_and_plot_overlaps3(alphas):
    overlaps_3 = []

    # Run the cycle test for each value of theta and compute the LHS/RHS expression
    for alpha in alphas:
        qc = cycle_test_circuit(alpha)
        overlap = run_circuit(qc)
        overlaps_3.append(overlap)

    plt.plot(alphas, overlaps_3)
    plt.xlabel(r'$\theta$ (rad)', fontsize=12)
    plt.ylabel('Values', fontsize=12)
    plt.title(r'$\Delta_3$')
    plt.grid(True)

    # Show plot
    plt.show()
    return overlaps_3


def compute_and_plot_Z(overlaps_2, overlaps_3, alphas):
    # Compute the new array (Zw) using the formula provided
    new_array = (overlaps_3 / overlaps_2) - (overlaps_2 - overlaps_3 / overlaps_2)
    # Plot the result
    plt.plot(alphas, new_array, marker='o', linestyle='-', color='r')
    plt.xlabel(r'$\theta$')
    plt.ylabel('Zw Values')
    plt.title('Plot of $Z_w$')
    plt.grid(True)
    plt.show()


def run_4_b():
    """
    4.b(ii)
        Note that Δ3(Π_φ, |1⟩⟨1| Π_ψ) is computed as:
        Δ3(Π_φ, |1⟩⟨1| Π_ψ) = Tr(Π_φ |1⟩⟨1| Π_ψ)
                              = Tr(⟨1| Π_ψ Π_φ |1⟩)
                              = (Π_ψ Π_φ)_(2,2)
                              = Tr(Π_ψ Π_φ) - (Π_ψ Π_φ)_(1,1)
                              = Δ2(Π_ψ Π_φ) - Δ3(Π_φ |0⟩⟨0| Π_ψ)

        Since the right hand side has already been calculated,
        we can now compute the left hand side directly without any further measurements.
    4.b
        Recall that Z is defined as:
        Z = 1 * |0⟩⟨0| + (-1) * |1⟩⟨1|

        We will now use the identity proven in part 4(a),
        along with the previously computed values of Δ2 and Δ3,
        to compute Z_w:

        Z_w = (Δ3(Π_φ |0⟩⟨0| Π_ψ) / Δ2(Π_φ Π_ψ)) - (Δ3(Π_φ |1⟩⟨1| Π_ψ) / Δ2(Π_φ Π_ψ))

        The result Z_w can be computed directly using the above equation.
    """
    alphas = [0, np.pi / 3, np.pi / 2, np.pi, 4 * np.pi / 3]

    overlaps_2 = compute_and_plot_overlaps2(alphas)

    overlaps_3 = compute_and_plot_overlaps3(alphas)

    compute_and_plot_Z(overlaps_2, overlaps_3, alphas)
