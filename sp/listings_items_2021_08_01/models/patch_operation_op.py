from enum import Enum


class PatchOperationOp(str, Enum):
    ADD = "add"
    REPLACE = "replace"
    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)
