from enum import Enum


class ShipmentConfirmationShipmentType(str, Enum):
    TRUCKLOAD = "TruckLoad"
    LESSTHANTRUCKLOAD = "LessThanTruckLoad"
    SMALLPARCEL = "SmallParcel"

    def __str__(self) -> str:
        return str(self.value)
