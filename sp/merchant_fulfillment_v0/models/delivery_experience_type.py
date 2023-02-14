from enum import Enum


class DeliveryExperienceType(str, Enum):
    DELIVERYCONFIRMATIONWITHADULTSIGNATURE = "DeliveryConfirmationWithAdultSignature"
    DELIVERYCONFIRMATIONWITHSIGNATURE = "DeliveryConfirmationWithSignature"
    DELIVERYCONFIRMATIONWITHOUTSIGNATURE = "DeliveryConfirmationWithoutSignature"
    NOTRACKING = "NoTracking"

    def __str__(self) -> str:
        return str(self.value)
