from enum import Enum


class OrderDetailsPurchaseOrderType(str, Enum):
    REGULARORDER = "RegularOrder"
    CONSIGNEDORDER = "ConsignedOrder"
    NEWPRODUCTINTRODUCTION = "NewProductIntroduction"
    RUSHORDER = "RushOrder"

    def __str__(self) -> str:
        return str(self.value)
