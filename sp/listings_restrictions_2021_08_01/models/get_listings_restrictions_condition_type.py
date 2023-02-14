from enum import Enum


class GetListingsRestrictionsConditionType(str, Enum):
    NEW_NEW = "new_new"
    NEW_OPEN_BOX = "new_open_box"
    NEW_OEM = "new_oem"
    REFURBISHED_REFURBISHED = "refurbished_refurbished"
    USED_LIKE_NEW = "used_like_new"
    USED_VERY_GOOD = "used_very_good"
    USED_GOOD = "used_good"
    USED_ACCEPTABLE = "used_acceptable"
    COLLECTIBLE_LIKE_NEW = "collectible_like_new"
    COLLECTIBLE_VERY_GOOD = "collectible_very_good"
    COLLECTIBLE_GOOD = "collectible_good"
    COLLECTIBLE_ACCEPTABLE = "collectible_acceptable"
    CLUB_CLUB = "club_club"

    def __str__(self) -> str:
        return str(self.value)
