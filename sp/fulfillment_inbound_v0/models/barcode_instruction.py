from enum import Enum


class BarcodeInstruction(str, Enum):
    REQUIRESFNSKULABEL = "RequiresFNSKULabel"
    CANUSEORIGINALBARCODE = "CanUseOriginalBarcode"
    MUSTPROVIDESELLERSKU = "MustProvideSellerSKU"

    def __str__(self) -> str:
        return str(self.value)
