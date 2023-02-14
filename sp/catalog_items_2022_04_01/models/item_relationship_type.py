from enum import Enum


class ItemRelationshipType(str, Enum):
    VARIATION = "VARIATION"
    PACKAGE_HIERARCHY = "PACKAGE_HIERARCHY"

    def __str__(self) -> str:
        return str(self.value)
