from enum import Enum


class StopFunctionCode(str, Enum):
    PORTOFDISCHARGE = "PortOfDischarge"
    FREIGHTPAYABLEAT = "FreightPayableAt"
    PORTOFLOADING = "PortOfLoading"

    def __str__(self) -> str:
        return str(self.value)
