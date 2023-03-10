from enum import Enum


class CurrentStatus(str, Enum):
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    RETURNING = "RETURNING"
    RETURNED = "RETURNED"
    UNDELIVERABLE = "UNDELIVERABLE"
    DELAYED = "DELAYED"
    AVAILABLE_FOR_PICKUP = "AVAILABLE_FOR_PICKUP"
    CUSTOMER_ACTION = "CUSTOMER_ACTION"
    UNKNOWN = "UNKNOWN"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERY_ATTEMPTED = "DELIVERY_ATTEMPTED"
    PICKUP_SUCCESSFUL = "PICKUP_SUCCESSFUL"
    PICKUP_CANCELLED = "PICKUP_CANCELLED"
    PICKUP_ATTEMPTED = "PICKUP_ATTEMPTED"
    PICKUP_SCHEDULED = "PICKUP_SCHEDULED"
    RETURN_REQUEST_ACCEPTED = "RETURN_REQUEST_ACCEPTED"
    REFUND_ISSUED = "REFUND_ISSUED"
    RETURN_RECEIVED_IN_FC = "RETURN_RECEIVED_IN_FC"

    def __str__(self) -> str:
        return str(self.value)
