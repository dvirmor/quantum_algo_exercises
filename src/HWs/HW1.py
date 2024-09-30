from qiskit import transpile
from qiskit.circuit.library import QFT
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService


def encode_phi_stage(circuit):
    circuit.x(2)
    circuit.cx(0, 1)
    # Because qiskit
    circuit.swap(0, 2)


def combine_phi_with_inverse_qft(circuit):
    circuit.append(QFT(3, inverse=True), range(3))
    circuit.measure(range(3), range(3))


def run_qc_on_real_hardware(circuit, token):
    service = QiskitRuntimeService(channel="ibm_quantum", token=token)
    backend = service.least_busy(simulator=False, operational=True)
    shots = 2048
    transpiled_qc = transpile(circuit, backend, optimization_level=3)
    job = backend.run(transpiled_qc, shots=shots)
    # Use the job ID to retrieve your job data later
    print(f">>> Job ID: {job.job_id()}")


def run_1_d(token):
    qc = QuantumCircuit(3, 3)
    encode_phi_stage(qc)
    combine_phi_with_inverse_qft(qc)
    run_qc_on_real_hardware(qc, token)

def plot_results(job_id, token):
    from qiskit_ibm_runtime import QiskitRuntimeService

    service = QiskitRuntimeService(
        channel='ibm_quantum',
        instance='jupiter/internal/default',
        token=token
    )
    job = service.job('cssz9mpvkv50008gcz10')
    job_result = job.result()
    print(job_result)


if __name__ == '__main__':
    from src.main import credentials
    # run_1_d(credentials.token) # Job ID: cvxg1zz22dfg008n21xg
    plot_results(None, credentials.token)
