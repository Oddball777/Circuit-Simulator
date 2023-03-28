import unittest

from circuit_simulator.basic_circuit_elements import Light, Source, Wire


class TestWire(unittest.TestCase):
    def test_init(self):
        wire = Wire()
        self.assertFalse(wire.isOn)


class TestSource(unittest.TestCase):
    def test_init(self):
        wire = Wire()
        source = Source([wire])
        self.assertFalse(source.isOn)

    def test_toggle(self):
        wire = Wire()
        source = Source([wire])
        source.toggle()
        self.assertTrue(wire.isOn)

    def test_toggle_on_if_off(self):
        wire = Wire()
        source = Source([wire])
        source.toggle_on()
        self.assertTrue(wire.isOn)

    def test_toggle_on_if_on(self):
        wire = Wire()
        source = Source([wire])
        source.toggle()
        source.toggle_on()
        self.assertTrue(wire.isOn)

    def test_toggle_off_if_off(self):
        wire = Wire()
        source = Source([wire])
        source.toggle_off()
        self.assertFalse(wire.isOn)

    def test_toggle_off_if_on(self):
        wire = Wire()
        source = Source([wire])
        source.toggle()
        source.toggle_off()
        self.assertFalse(wire.isOn)


class TestLight(unittest.TestCase):
    def test_init(self):
        wire = Wire()
        source = Source([wire])
        light = Light([wire])
        self.assertFalse(light.isOn)

    def test_isOn_false(self):
        wire1 = Wire()
        wire2 = Wire()
        source1 = Source([wire1])
        source2 = Source([wire2])
        light = Light([wire1, wire2])
        self.assertFalse(light.isOn)

    def test_isOn_true(self):
        wire1 = Wire()
        wire2 = Wire()
        source1 = Source([wire1])
        source2 = Source([wire2])
        light = Light([wire1, wire2])
        source1.toggle()
        source2.toggle()
        self.assertTrue(light.isOn)
