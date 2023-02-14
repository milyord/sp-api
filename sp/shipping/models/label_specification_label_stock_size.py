from enum import Enum


class LabelSpecificationLabelStockSize(str, Enum):
    VALUE_0 = "4x6"

    def __str__(self) -> str:
        return str(self.value)
