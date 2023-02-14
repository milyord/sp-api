from enum import Enum


class StandardIdForLabel(str, Enum):
    AMAZONORDERID = "AmazonOrderId"

    def __str__(self) -> str:
        return str(self.value)
