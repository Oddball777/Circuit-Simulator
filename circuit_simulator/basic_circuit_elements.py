from abc import ABC
from dataclasses import dataclass


class Component(ABC):
    @property
    def isOn(self):
        raise NotImplementedError


@dataclass
class Wire(Component):
    input: Component

    @property
    def isOn(self):
        return self.input.isOn


@dataclass
class Source(Component):
    active: bool = False

    @property
    def isOn(self):
        return self.active

    def toggle(self):
        self.active = not self.active

    def toggle_on(self):
        if not self.active:
            self.toggle()

    def toggle_off(self):
        if self.active:
            self.toggle()


@dataclass
class Light(Component):
    input: Wire | Component

    @property
    def isOn(self) -> bool:
        return self.input.isOn


@dataclass
class AndGate(Component):
    inputs: list[Wire | Component]

    @property
    def isOn(self) -> bool:
        return all([wire.isOn for wire in self.inputs])


@dataclass
class OrGate(Component):
    inputs: list[Wire | Component]

    @property
    def isOn(self) -> bool:
        return any([wire.isOn for wire in self.inputs])


@dataclass
class NotGate(Component):
    input: Wire | Component

    @property
    def isOn(self) -> bool:
        return not self.input.isOn


@dataclass
class NandGate(Component):
    inputs: list[Wire | Component]

    @property
    def isOn(self) -> bool:
        return not all([wire.isOn for wire in self.inputs])


@dataclass
class NorGate(Component):
    inputs: list[Wire | Component]

    @property
    def isOn(self) -> bool:
        return not any([wire.isOn for wire in self.inputs])


@dataclass
class XorGate(Component):
    inputs: list[Wire | Component]

    @property
    def isOn(self) -> bool:
        return False if (sum([wire.isOn for wire in self.inputs]) % 2 == 0) else True


@dataclass
class XnorGate(Component):
    inputs: list[Wire | Component]

    @property
    def isOn(self) -> bool:
        return True if (sum([wire.isOn for wire in self.inputs]) % 2 == 0) else False
