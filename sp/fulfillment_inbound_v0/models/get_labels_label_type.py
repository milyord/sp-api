from enum import Enum


class GetLabelsLabelType(str, Enum):
    BARCODE_2D = "BARCODE_2D"
    UNIQUE = "UNIQUE"
    PALLET = "PALLET"

    def __str__(self) -> str:
        return str(self.value)
