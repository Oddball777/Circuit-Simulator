import unittest

from circuit_simulator.basic_circuit_elements import (
    AndGate,
    Light,
    NandGate,
    NorGate,
    NotGate,
    OrGate,
    Source,
    Wire,
    XnorGate,
    XorGate,
)
from circuit_simulator.circuit import Circuit


class TestCircuit(unittest.TestCase):
    def set_up(self) -> None:
        ...

    def test_init_circuit(self):
        ...
