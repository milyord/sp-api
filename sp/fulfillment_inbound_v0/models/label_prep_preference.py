from enum import Enum


class LabelPrepPreference(str, Enum):
    SELLER_LABEL = "SELLER_LABEL"
    AMAZON_LABEL_ONLY = "AMAZON_LABEL_ONLY"
    AMAZON_LABEL_PREFERRED = "AMAZON_LABEL_PREFERRED"

    def __str__(self) -> str:
        return str(self.value)
