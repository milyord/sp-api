from enum import Enum


class HazmatType(str, Enum):
    NONE = "None"
    LQHAZMAT = "LQHazmat"

    def __str__(self) -> str:
        return str(self.value)
