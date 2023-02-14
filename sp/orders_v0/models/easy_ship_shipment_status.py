from enum import Enum


class EasyShipShipmentStatus(str, Enum):
    PENDINGSCHEDULE = "PendingSchedule"
    PENDINGPICKUP = "PendingPickUp"
    PENDINGDROPOFF = "PendingDropOff"
    LABELCANCELED = "LabelCanceled"
    PICKEDUP = "PickedUp"
    DROPPEDOFF = "DroppedOff"
    ATORIGINFC = "AtOriginFC"
    ATDESTINATIONFC = "AtDestinationFC"
    DELIVERED = "Delivered"
    REJECTEDBYBUYER = "RejectedByBuyer"
    UNDELIVERABLE = "Undeliverable"
    RETURNINGTOSELLER = "ReturningToSeller"
    RETURNEDTOSELLER = "ReturnedToSeller"
    LOST = "Lost"
    OUTFORDELIVERY = "OutForDelivery"
    DAMAGED = "Damaged"

    def __str__(self) -> str:
        return str(self.value)
