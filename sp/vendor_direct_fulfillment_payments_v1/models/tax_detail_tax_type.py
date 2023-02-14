from enum import Enum


class TaxDetailTaxType(str, Enum):
    CGST = "CGST"
    SGST = "SGST"
    CESS = "CESS"
    UTGST = "UTGST"
    IGST = "IGST"
    MWST = "MwSt."
    PST = "PST"
    TVA = "TVA"
    VAT = "VAT"
    GST = "GST"
    ST = "ST"
    CONSUMPTION = "Consumption"
    MUTUALLYDEFINED = "MutuallyDefined"
    DOMESTICVAT = "DomesticVAT"

    def __str__(self) -> str:
        return str(self.value)
