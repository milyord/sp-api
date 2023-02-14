from enum import Enum


class ServiceType(str, Enum):
    AMAZON_SHIPPING_GROUND = "Amazon Shipping Ground"
    AMAZON_SHIPPING_STANDARD = "Amazon Shipping Standard"
    AMAZON_SHIPPING_PREMIUM = "Amazon Shipping Premium"

    def __str__(self) -> str:
        return str(self.value)
