from enum import Enum


class PoaPoaType(str, Enum):
    NO_SIGNATURE_DUMMY_POS = "NO_SIGNATURE_DUMMY_POS"
    CUSTOMER_SIGNATURE = "CUSTOMER_SIGNATURE"
    DUMMY_RECEIPT = "DUMMY_RECEIPT"
    POA_RECEIPT = "POA_RECEIPT"

    def __str__(self) -> str:
        return str(self.value)
