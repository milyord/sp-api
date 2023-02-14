from enum import Enum


class ProductTypeDefinitionRequirementsEnforced(str, Enum):
    ENFORCED = "ENFORCED"
    NOT_ENFORCED = "NOT_ENFORCED"

    def __str__(self) -> str:
        return str(self.value)
