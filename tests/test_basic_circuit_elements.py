import unittest

from circuit_simulator.basic_circuit_elements import Light, Source, Wire


class TestWire(unittest.TestCase):
    def test_init(self):
        wire = Wire()
        self.assertFalse(wire)


class TestSource(unittest.TestCase):
    def set_up(self):
        self.wire = Wire()
        self.source = Source([self.wire])

    def test_init(self):
        self.assertFalse(self.source.isOn)

    def test_toggle(self):
        self.source.toggle()
        self.assertTrue(self.wire.isOn)
