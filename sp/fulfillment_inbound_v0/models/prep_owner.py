from enum import Enum


class PrepOwner(str, Enum):
    AMAZON = "AMAZON"
    SELLER = "SELLER"

    def __str__(self) -> str:
        return str(self.value)
