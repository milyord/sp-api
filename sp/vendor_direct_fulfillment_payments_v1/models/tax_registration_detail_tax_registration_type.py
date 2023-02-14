from enum import Enum


class TaxRegistrationDetailTaxRegistrationType(str, Enum):
    VAT = "VAT"
    GST = "GST"

    def __str__(self) -> str:
        return str(self.value)
