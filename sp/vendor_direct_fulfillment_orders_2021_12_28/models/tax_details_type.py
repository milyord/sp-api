from enum import Enum


class TaxDetailsType(str, Enum):
    CONSUMPTION = "CONSUMPTION"
    GST = "GST"
    MWST = "MwSt."
    PST = "PST"
    TOTAL = "TOTAL"
    TVA = "TVA"
    VAT = "VAT"

    def __str__(self) -> str:
        return str(self.value)
