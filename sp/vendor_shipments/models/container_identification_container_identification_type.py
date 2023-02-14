from enum import Enum


class ContainerIdentificationContainerIdentificationType(str, Enum):
    SSCC = "SSCC"
    AMZNCC = "AMZNCC"
    GTIN = "GTIN"
    BPS = "BPS"
    CID = "CID"

    def __str__(self) -> str:
        return str(self.value)
