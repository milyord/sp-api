from enum import Enum


class ReturnItemDisposition(str, Enum):
    SELLABLE = "Sellable"
    DEFECTIVE = "Defective"
    CUSTOMERDAMAGED = "CustomerDamaged"
    CARRIERDAMAGED = "CarrierDamaged"
    FULFILLERDAMAGED = "FulfillerDamaged"

    def __str__(self) -> str:
        return str(self.value)
