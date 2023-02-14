from enum import Enum


class FeeLineItemFeeType(str, Enum):
    FBAWEIGHTBASEDFEE = "FBAWeightBasedFee"
    FBAPERORDERFULFILLMENTFEE = "FBAPerOrderFulfillmentFee"
    FBAPERUNITFULFILLMENTFEE = "FBAPerUnitFulfillmentFee"
    COMMISSION = "Commission"

    def __str__(self) -> str:
        return str(self.value)
