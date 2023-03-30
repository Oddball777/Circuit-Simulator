from dataclasses import dataclass
from itertools import product
from typing import Optional

import numpy as np
import pandas as pd

from .basic_circuit_elements import Component, Light, Source


@dataclass
class Circuit:
    sources: list[Source]
    indictators: list[Light]
    other_components: Optional[list[Component]]

    def __post_init__(self):
        source_current_vals = [source.isOn for source in self.sources]
        self.make_truth_table()
        for index, source in enumerate(self.sources):
            if source_current_vals[index] == 0:
                source.toggle_off()
            if source_current_vals[index] == 1:
                source.toggle_on()

    def make_truth_table(self):
        source_values = self.get_sources_values()
        series_of_sources = self.get_sources_series(source_values)
        series_of_indicators = self.get_indicators_series(source_values)
        self.truth_table = pd.concat(
            [*series_of_sources, *series_of_indicators], axis=1
        )

    def get_sources_values(self):
        return np.array(list(product(range(2), repeat=len(self.sources))))

    def get_sources_series(self, source_values):
        series_of_sources = [
            pd.Series(source_values.T[i], name=f"Source {i+1}")
            for i in range(len(self.sources))
        ]
        return series_of_sources

    def get_indicators_series(self, source_values):
        indicator_values = self.get_indicators_values(source_values)
        series_of_indictators = [
            pd.Series(indicator_values.T[i], name=f"Indicator {i+1}")
            for i in range(len(self.indictators))
        ]
        return series_of_indictators

    def get_indicators_values(self, source_values):
        indicator_values = []
        for comb in source_values:
            for index, val in enumerate(comb):
                if val == 0:
                    self.sources[index].toggle_off()
                if val == 1:
                    self.sources[index].toggle_on()
            indicator_values_for_this_comb = [
                int(indicator.isOn) for indicator in self.indictators
            ]
            indicator_values.append(indicator_values_for_this_comb)
        return np.array(indicator_values)
