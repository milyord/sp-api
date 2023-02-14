from enum import Enum


class ShippingLabelLabelFormat(str, Enum):
    PNG = "PNG"
    ZPL = "ZPL"

    def __str__(self) -> str:
        return str(self.value)
