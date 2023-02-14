from enum import Enum


class ReservationType(str, Enum):
    APPOINTMENT = "APPOINTMENT"
    TRAVEL = "TRAVEL"
    VACATION = "VACATION"
    BREAK = "BREAK"
    TRAINING = "TRAINING"

    def __str__(self) -> str:
        return str(self.value)
