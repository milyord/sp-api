from enum import Enum


class UnitOfLength(str, Enum):
    CM = "Cm"

    def __str__(self) -> str:
        return str(self.value)
