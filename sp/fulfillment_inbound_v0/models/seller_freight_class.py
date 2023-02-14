from enum import Enum


class SellerFreightClass(str, Enum):
    VALUE_0 = "50"
    VALUE_1 = "55"
    VALUE_2 = "60"
    VALUE_3 = "65"
    VALUE_4 = "70"
    VALUE_5 = "77.5"
    VALUE_6 = "85"
    VALUE_7 = "92.5"
    VALUE_8 = "100"
    VALUE_9 = "110"
    VALUE_10 = "125"
    VALUE_11 = "150"
    VALUE_12 = "175"
    VALUE_13 = "200"
    VALUE_14 = "250"
    VALUE_15 = "300"
    VALUE_16 = "400"
    VALUE_17 = "500"

    def __str__(self) -> str:
        return str(self.value)
