from enum import Enum


class AdditionalDetailsType(str, Enum):
    SUR = "SUR"
    OCR = "OCR"
    CARTONCOUNT = "CartonCount"

    def __str__(self) -> str:
        return str(self.value)
