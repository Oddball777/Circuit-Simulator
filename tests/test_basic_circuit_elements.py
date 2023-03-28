import unittest

from circuit_simulator.basic_circuit_elements import AndGate, Light, Source, Wire


class TestWire(unittest.TestCase):
    def test_init(self):
        source = Source()
        wire = Wire([source])
        self.assertFalse(wire.isOn)


class TestSource(unittest.TestCase):
    def test_init_off(self):
        source = Source()
        self.assertFalse(source.isOn)

    def test_toggle_off_to_on(self):
        source = Source()
        wire = Wire([source])
        source.toggle()
        self.assertTrue(wire.isOn)

    def test_toggle_on_to_off(self):
        source = Source(active=True)
        wire = Wire([source])
        source.toggle()
        self.assertFalse(wire.isOn)

    def test_toggle_on_if_off(self):
        source = Source()
        wire = Wire([source])
        source.toggle_on()
        self.assertTrue(wire.isOn)

    def test_toggle_on_if_on(self):
        source = Source()
        wire = Wire([source])
        source.toggle()
        source.toggle_on()
        self.assertTrue(wire.isOn)

    def test_toggle_off_if_off(self):
        source = Source()
        wire = Wire([source])
        source.toggle_off()
        self.assertFalse(wire.isOn)

    def test_toggle_off_if_on(self):
        source = Source()
        wire = Wire([source])
        source.toggle()
        source.toggle_off()
        self.assertFalse(wire.isOn)


class TestLight(unittest.TestCase):
    def test_init(self):
        source = Source()
        wire = Wire([source])
        light = Light([wire])
        self.assertFalse(light.isOn)

    def test_isOn_false(self):
        source1 = Source()
        source2 = Source()
        wire1 = Wire([source1])
        wire2 = Wire([source2])
        light = Light([wire1, wire2])
        self.assertFalse(light.isOn)

    def test_isOn_true(self):
        source1 = Source()
        source2 = Source()
        wire1 = Wire([source1])
        wire2 = Wire([source2])
        light = Light([wire1, wire2])
        source1.toggle()
        source2.toggle()
        self.assertTrue(light.isOn)


class TestAndGate(unittest.TestCase):
    def test_init_all_on(self):
        source1 = Source(active=True)
        source2 = Source(active=True)
        source3 = Source(active=True)
        wire1 = Wire([source1])
        wire2 = Wire([source2])
        wire3 = Wire([source3])
        and_gate = AndGate([wire1, wire2, wire3])
        self.assertTrue(and_gate.isOn)

    def test_init_one_off(self):
        source1 = Source(active=False)
        source2 = Source(active=True)
        source3 = Source(active=True)
        wire1 = Wire([source1])
        wire2 = Wire([source2])
        wire3 = Wire([source3])
        and_gate = AndGate([wire1, wire2, wire3])
        self.assertFalse(and_gate.isOn)

    def test_init_all_off(self):
        source1 = Source(active=False)
        source2 = Source(active=False)
        source3 = Source(active=False)
        wire1 = Wire([source1])
        wire2 = Wire([source2])
        wire3 = Wire([source3])
        and_gate = AndGate([wire1, wire2, wire3])
        self.assertFalse(and_gate.isOn)
