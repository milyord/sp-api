from enum import Enum


class PackageStatus(str, Enum):
    READYFORPICKUP = "ReadyForPickup"
    PICKEDUP = "PickedUp"
    ATORIGINFC = "AtOriginFC"
    ATDESTINATIONFC = "AtDestinationFC"
    DELIVERED = "Delivered"
    REJECTED = "Rejected"
    UNDELIVERABLE = "Undeliverable"
    RETURNEDTOSELLER = "ReturnedToSeller"
    LOSTINTRANSIT = "LostInTransit"
    LABELCANCELED = "LabelCanceled"
    DAMAGEDINTRANSIT = "DamagedInTransit"
    OUTFORDELIVERY = "OutForDelivery"

    def __str__(self) -> str:
        return str(self.value)
