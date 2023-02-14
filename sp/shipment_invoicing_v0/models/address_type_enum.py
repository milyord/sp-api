from enum import Enum


class AddressTypeEnum(str, Enum):
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"

    def __str__(self) -> str:
        return str(self.value)
