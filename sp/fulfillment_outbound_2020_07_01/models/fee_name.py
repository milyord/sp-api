from enum import Enum


class FeeName(str, Enum):
    FBAPERUNITFULFILLMENTFEE = "FBAPerUnitFulfillmentFee"
    FBAPERORDERFULFILLMENTFEE = "FBAPerOrderFulfillmentFee"
    FBATRANSPORTATIONFEE = "FBATransportationFee"
    FBAFULFILLMENTCODFEE = "FBAFulfillmentCODFee"

    def __str__(self) -> str:
        return str(self.value)
