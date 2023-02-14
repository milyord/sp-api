from enum import Enum


class ErrorReason(str, Enum):
    DOESNOTEXIST = "DoesNotExist"
    INVALIDASIN = "InvalidASIN"

    def __str__(self) -> str:
        return str(self.value)
