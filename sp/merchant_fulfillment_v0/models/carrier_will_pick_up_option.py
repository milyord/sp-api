from enum import Enum


class CarrierWillPickUpOption(str, Enum):
    CARRIERWILLPICKUP = "CarrierWillPickUp"
    SHIPPERWILLDROPOFF = "ShipperWillDropOff"
    NOPREFERENCE = "NoPreference"

    def __str__(self) -> str:
        return str(self.value)
