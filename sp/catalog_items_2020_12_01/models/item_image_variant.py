from enum import Enum


class ItemImageVariant(str, Enum):
    MAIN = "MAIN"
    PT01 = "PT01"
    PT02 = "PT02"
    PT03 = "PT03"
    PT04 = "PT04"
    PT05 = "PT05"
    PT06 = "PT06"
    PT07 = "PT07"
    PT08 = "PT08"
    SWCH = "SWCH"

    def __str__(self) -> str:
        return str(self.value)
