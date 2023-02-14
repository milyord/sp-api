from enum import Enum


class ImportDetailsMethodOfPayment(str, Enum):
    PAIDBYBUYER = "PaidByBuyer"
    COLLECTONDELIVERY = "CollectOnDelivery"
    DEFINEDBYBUYERANDSELLER = "DefinedByBuyerAndSeller"
    FOBPORTOFCALL = "FOBPortOfCall"
    PREPAIDBYSELLER = "PrepaidBySeller"
    PAIDBYSELLER = "PaidBySeller"

    def __str__(self) -> str:
        return str(self.value)
