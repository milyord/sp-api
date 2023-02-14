from enum import Enum


class ShippingSpeedCategory(str, Enum):
    STANDARD = "Standard"
    EXPEDITED = "Expedited"
    PRIORITY = "Priority"
    SCHEDULEDDELIVERY = "ScheduledDelivery"

    def __str__(self) -> str:
        return str(self.value)
