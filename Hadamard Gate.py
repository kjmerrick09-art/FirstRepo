# Import required Qiskit modules
from qiskit import QuantumCircuit
#from qiskit import Aer
#from qiskit import execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to qubit 0
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Draw the circuit
print("Quantum Circuit:")
print(qc.draw())

# Use the Qiskit Aer simulator
#simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the simulator
#job = execute(qc, simulator, shots=1024)
#result = job.result()

# Get the counts (measurement results)
#counts = result.get_counts(qc)
#print("\nMeasurement Results:", counts)

# Plot the histogram of results
#plot_histogram(counts)
#plt.show()
