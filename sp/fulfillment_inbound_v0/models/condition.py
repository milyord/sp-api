from enum import Enum


class Condition(str, Enum):
    NEWITEM = "NewItem"
    NEWWITHWARRANTY = "NewWithWarranty"
    NEWOEM = "NewOEM"
    NEWOPENBOX = "NewOpenBox"
    USEDLIKENEW = "UsedLikeNew"
    USEDVERYGOOD = "UsedVeryGood"
    USEDGOOD = "UsedGood"
    USEDACCEPTABLE = "UsedAcceptable"
    USEDPOOR = "UsedPoor"
    USEDREFURBISHED = "UsedRefurbished"
    COLLECTIBLELIKENEW = "CollectibleLikeNew"
    COLLECTIBLEVERYGOOD = "CollectibleVeryGood"
    COLLECTIBLEGOOD = "CollectibleGood"
    COLLECTIBLEACCEPTABLE = "CollectibleAcceptable"
    COLLECTIBLEPOOR = "CollectiblePoor"
    REFURBISHEDWITHWARRANTY = "RefurbishedWithWarranty"
    REFURBISHED = "Refurbished"
    CLUB = "Club"

    def __str__(self) -> str:
        return str(self.value)
