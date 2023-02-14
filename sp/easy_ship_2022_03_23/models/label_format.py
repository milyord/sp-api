from enum import Enum


class LabelFormat(str, Enum):
    PDF = "PDF"
    ZPL = "ZPL"

    def __str__(self) -> str:
        return str(self.value)
