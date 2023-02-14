from enum import Enum


class ContentType(str, Enum):
    EBC = "EBC"
    EMC = "EMC"

    def __str__(self) -> str:
        return str(self.value)
