from enum import Enum


class DeliveryExperienceOption(str, Enum):
    DELIVERYCONFIRMATIONWITHADULTSIGNATURE = "DeliveryConfirmationWithAdultSignature"
    DELIVERYCONFIRMATIONWITHSIGNATURE = "DeliveryConfirmationWithSignature"
    DELIVERYCONFIRMATIONWITHOUTSIGNATURE = "DeliveryConfirmationWithoutSignature"
    NOTRACKING = "NoTracking"
    NOPREFERENCE = "NoPreference"

    def __str__(self) -> str:
        return str(self.value)
