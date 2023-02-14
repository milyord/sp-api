from enum import Enum


class FeatureSettingsFeatureFulfillmentPolicy(str, Enum):
    REQUIRED = "Required"
    NOTREQUIRED = "NotRequired"

    def __str__(self) -> str:
        return str(self.value)
