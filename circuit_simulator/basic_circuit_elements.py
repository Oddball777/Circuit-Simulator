from abc import ABC
from dataclasses import dataclass


@dataclass
class Wire:
    isOn: bool = False


class Source:
    def __init__(self, outputs: list[Wire]) -> None:
        self.outputs = outputs
        self.isOn = False

    def toggle(self):
        self.isOn = not self.isOn
        for wire in self.outputs:
            wire.isOn = not wire.isOn


@dataclass
class Light:
    inputs: list[Wire]

    @property
    def isOn(self) -> bool:
        return any([wire.isOn for wire in self.inputs])
