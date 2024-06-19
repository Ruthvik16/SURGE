import qiskit
from qiskit_aer import Aer
from qiskit import transpile
circuit = qiskit.QuantumCircuit(4)

circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)

circuit.cx(0, 1)
circuit.cx(1, 2)
circuit.cx(2, 3)

circuit.x(3)
circuit.cz(0, 2)
circuit.ry(0.5, 1)

creg = qiskit.ClassicalRegister(4)
circuit.add_register(creg)
circuit.measure([0, 1, 2, 3], [creg[0], creg[1], creg[2], creg[3]])

simulator = Aer.get_backend('qasm_simulator')
new_circuit = transpile(circuit, simulator)

job = simulator.run(new_circuit)
result = job.result()
count = result.get_counts()
print(count)

