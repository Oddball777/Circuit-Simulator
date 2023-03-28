from abc import ABC
from dataclasses import dataclass


class Component(ABC):
    @property
    def isOn(self):
        raise NotImplementedError


@dataclass
class Wire:
    inputs: list[Component]

    @property
    def isOn(self):
        return any([component.isOn for component in self.inputs])


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
    inputs: list[Wire]

    @property
    def isOn(self) -> bool:
        return any([wire.isOn for wire in self.inputs])


@dataclass
class AndGate(Component):
    inputs: list[Wire]

    @property
    def isOn(self) -> bool:
        return all([wire.isOn for wire in self.inputs])


@dataclass
class OrGate(Component):
    inputs: list[Wire]

    @property
    def isOn(self) -> bool:
        return any([wire.isOn for wire in self.inputs])
