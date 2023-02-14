from enum import Enum


class LabelSpecificationLabelFormat(str, Enum):
    PNG = "PNG"

    def __str__(self) -> str:
        return str(self.value)
