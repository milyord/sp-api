from enum import Enum


class LabelPrepType(str, Enum):
    NO_LABEL = "NO_LABEL"
    SELLER_LABEL = "SELLER_LABEL"
    AMAZON_LABEL = "AMAZON_LABEL"

    def __str__(self) -> str:
        return str(self.value)
