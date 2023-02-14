from enum import Enum


class SmallAndLightEligibilityStatus(str, Enum):
    ELIGIBLE = "ELIGIBLE"
    NOT_ELIGIBLE = "NOT_ELIGIBLE"

    def __str__(self) -> str:
        return str(self.value)
