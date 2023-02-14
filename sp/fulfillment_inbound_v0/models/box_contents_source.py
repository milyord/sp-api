from enum import Enum


class BoxContentsSource(str, Enum):
    NONE = "NONE"
    FEED = "FEED"
    VALUE_2 = "2D_BARCODE"
    INTERACTIVE = "INTERACTIVE"

    def __str__(self) -> str:
        return str(self.value)
