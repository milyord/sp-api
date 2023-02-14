from enum import Enum


class ColorType(str, Enum):
    DARK = "DARK"
    LIGHT = "LIGHT"

    def __str__(self) -> str:
        return str(self.value)
