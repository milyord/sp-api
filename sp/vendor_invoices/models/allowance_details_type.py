from enum import Enum


class AllowanceDetailsType(str, Enum):
    DISCOUNT = "Discount"
    DISCOUNTINCENTIVE = "DiscountIncentive"
    DEFECTIVE = "Defective"
    PROMOTIONAL = "Promotional"
    UNSALEABLEMERCHANDISE = "UnsaleableMerchandise"
    SPECIAL = "Special"

    def __str__(self) -> str:
        return str(self.value)
