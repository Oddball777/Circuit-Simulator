from dataclasses import dataclass

from .basic_circuit_elements import Component, Light, Source


@dataclass
class Circuit:
    sources: list[Source]
    other_components: list[Component]
    indictators: list[Light]
