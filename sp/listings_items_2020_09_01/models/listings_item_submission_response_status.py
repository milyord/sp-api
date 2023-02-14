from enum import Enum


class ListingsItemSubmissionResponseStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    INVALID = "INVALID"

    def __str__(self) -> str:
        return str(self.value)
