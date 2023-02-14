from enum import Enum


class ServiceJobServiceJobStatus(str, Enum):
    NOT_SERVICED = "NOT_SERVICED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    PENDING_SCHEDULE = "PENDING_SCHEDULE"
    NOT_FULFILLABLE = "NOT_FULFILLABLE"
    HOLD = "HOLD"
    PAYMENT_DECLINED = "PAYMENT_DECLINED"

    def __str__(self) -> str:
        return str(self.value)
