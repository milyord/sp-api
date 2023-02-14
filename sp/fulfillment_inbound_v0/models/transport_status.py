from enum import Enum


class TransportStatus(str, Enum):
    WORKING = "WORKING"
    ESTIMATING = "ESTIMATING"
    ESTIMATED = "ESTIMATED"
    ERROR_ON_ESTIMATING = "ERROR_ON_ESTIMATING"
    CONFIRMING = "CONFIRMING"
    CONFIRMED = "CONFIRMED"
    ERROR_ON_CONFIRMING = "ERROR_ON_CONFIRMING"
    VOIDING = "VOIDING"
    VOIDED = "VOIDED"
    ERROR_IN_VOIDING = "ERROR_IN_VOIDING"
    ERROR = "ERROR"

    def __str__(self) -> str:
        return str(self.value)
