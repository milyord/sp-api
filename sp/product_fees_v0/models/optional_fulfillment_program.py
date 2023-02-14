from enum import Enum


class OptionalFulfillmentProgram(str, Enum):
    FBA_CORE = "FBA_CORE"
    FBA_SNL = "FBA_SNL"
    FBA_EFN = "FBA_EFN"

    def __str__(self) -> str:
        return str(self.value)
