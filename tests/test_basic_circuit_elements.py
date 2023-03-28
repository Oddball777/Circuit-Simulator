import unittest

from circuit_simulator.basic_circuit_elements import (
    AndGate,
    Light,
    NandGate,
    NotGate,
    Source,
    Wire,
)


class TestWire(unittest.TestCase):
    def test_init_off(self):
        source = Source(active=False)
        wire = Wire(source)
        self.assertFalse(wire.isOn)

    def test_init_on(self):
        source = Source(active=True)
        wire = Wire(source)
        self.assertTrue(wire.isOn)


class TestSource(unittest.TestCase):
    def test_init_off(self):
        source = Source(active=False)
        self.assertFalse(source.isOn)

    def test_toggle_off_to_on(self):
        source = Source(active=False)
        source.toggle()
        self.assertTrue(source.isOn)

    def test_toggle_on_to_off(self):
        source = Source(active=True)
        source.toggle()
        self.assertFalse(source.isOn)

    def test_toggle_on_if_off(self):
        source = Source(active=False)
        source.toggle_on()
        self.assertTrue(source.isOn)

    def test_toggle_on_if_on(self):
        source = Source(active=True)
        source.toggle_on()
        self.assertTrue(source.isOn)

    def test_toggle_off_if_off(self):
        source = Source(active=False)
        source.toggle_off()
        self.assertFalse(source.isOn)

    def test_toggle_off_if_on(self):
        source = Source(active=True)
        source.toggle_off()
        self.assertFalse(source.isOn)


class TestLight(unittest.TestCase):
    def test_init(self):
        source = Source()
        wire = Wire(source)
        light = Light(wire)
        self.assertFalse(light.isOn)

    def test_isOn_false(self):
        source = Source()
        wire = Wire(source)
        light = Light(wire)
        self.assertFalse(light.isOn)

    def test_isOn_true(self):
        source = Source(active=True)
        wire = Wire(source)
        light = Light(wire)
        self.assertTrue(light.isOn)


class TestAndGate(unittest.TestCase):
    def test_init_all_on(self):
        source1 = Source(active=True)
        source2 = Source(active=True)
        source3 = Source(active=True)
        wire1 = Wire(source1)
        wire2 = Wire(source2)
        wire3 = Wire(source3)
        and_gate = AndGate([wire1, wire2, wire3])
        self.assertTrue(and_gate.isOn)

    def test_init_one_off(self):
        source1 = Source(active=False)
        source2 = Source(active=True)
        source3 = Source(active=True)
        wire1 = Wire(source1)
        wire2 = Wire(source2)
        wire3 = Wire(source3)
        and_gate = AndGate([wire1, wire2, wire3])
        self.assertFalse(and_gate.isOn)

    def test_init_all_off(self):
        source1 = Source(active=False)
        source2 = Source(active=False)
        source3 = Source(active=False)
        wire1 = Wire(source1)
        wire2 = Wire(source2)
        wire3 = Wire(source3)
        and_gate = AndGate([wire1, wire2, wire3])
        self.assertFalse(and_gate.isOn)


class TestNotGate(unittest.TestCase):
    def test_init_on(self):
        source = Source(active=True)
        wire = Wire(source)
        not_gate = NotGate(wire)
        self.assertFalse(not_gate.isOn)

    def test_init_off(self):
        source = Source(active=False)
        wire = Wire(source)
        not_gate = NotGate(wire)
        self.assertTrue(not_gate.isOn)


class TestNandGate(unittest.TestCase):
    def test_init_all_on(self):
        source1 = Source(active=True)
        source2 = Source(active=True)
        source3 = Source(active=True)
        wire1 = Wire(source1)
        wire2 = Wire(source2)
        wire3 = Wire(source3)
        nand_gate = NandGate([wire1, wire2, wire3])
        self.assertFalse(nand_gate.isOn)

    def test_init_all_off(self):
        source1 = Source(active=False)
        source2 = Source(active=False)
        source3 = Source(active=False)
        wire1 = Wire(source1)
        wire2 = Wire(source2)
        wire3 = Wire(source3)
        nand_gate = NandGate([wire1, wire2, wire3])
        self.assertTrue(nand_gate.isOn)

    def test_init_part_on(self):
        source1 = Source(active=True)
        source2 = Source(active=False)
        source3 = Source(active=False)
        wire1 = Wire(source1)
        wire2 = Wire(source2)
        wire3 = Wire(source3)
        nand_gate = NandGate([wire1, wire2, wire3])
        self.assertTrue(nand_gate.isOn)
