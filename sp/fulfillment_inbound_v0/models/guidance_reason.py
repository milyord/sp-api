from enum import Enum


class GuidanceReason(str, Enum):
    SLOWMOVINGASIN = "SlowMovingASIN"
    NOAPPLICABLEGUIDANCE = "NoApplicableGuidance"

    def __str__(self) -> str:
        return str(self.value)
