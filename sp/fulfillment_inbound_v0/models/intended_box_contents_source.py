from enum import Enum


class IntendedBoxContentsSource(str, Enum):
    NONE = "NONE"
    FEED = "FEED"
    VALUE_2 = "2D_BARCODE"

    def __str__(self) -> str:
        return str(self.value)
