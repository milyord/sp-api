from enum import Enum


class ContentBadge(str, Enum):
    BULK = "BULK"
    GENERATED = "GENERATED"
    LAUNCHPAD = "LAUNCHPAD"
    PREMIUM = "PREMIUM"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
