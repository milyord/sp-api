from enum import Enum


class IssueSeverity(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"

    def __str__(self) -> str:
        return str(self.value)
