from enum import Enum


class LabelFormat(str, Enum):
    PDF = "PDF"
    PNG = "PNG"
    ZPL203 = "ZPL203"
    ZPL300 = "ZPL300"
    SHIPPINGSERVICEDEFAULT = "ShippingServiceDefault"

    def __str__(self) -> str:
        return str(self.value)
