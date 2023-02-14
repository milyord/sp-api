from enum import Enum


class ErrorErrorLevel(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
