from enum import Enum


class ReportProcessingStatus(str, Enum):
    CANCELLED = "CANCELLED"
    DONE = "DONE"
    FATAL = "FATAL"
    IN_PROGRESS = "IN_PROGRESS"
    IN_QUEUE = "IN_QUEUE"

    def __str__(self) -> str:
        return str(self.value)
