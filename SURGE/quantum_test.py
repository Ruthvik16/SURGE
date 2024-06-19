import qiskit
from qiskit_aer import Aer
from qiskit import transpile

circuit = qiskit.QuantumCircuit(2)
circuit.h(0)
creg = qiskit.ClassicalRegister(2)
circuit.add_register(creg)
circuit.measure([0,1],[creg[0],creg[1]])

simulator = Aer.get_backend('qasm_simulator')

new_circuit = transpile(circuit, simulator)  
job = simulator.run(new_circuit)
result = job.result()
count = result.get_counts()
print(count)
