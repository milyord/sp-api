from enum import Enum


class PackingSlipContentType(str, Enum):
    APPLICATIONPDF = "application/pdf"

    def __str__(self) -> str:
        return str(self.value)
