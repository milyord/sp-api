from enum import Enum


class SmallAndLightEnrollmentStatus(str, Enum):
    ENROLLED = "ENROLLED"
    NOT_ENROLLED = "NOT_ENROLLED"

    def __str__(self) -> str:
        return str(self.value)
