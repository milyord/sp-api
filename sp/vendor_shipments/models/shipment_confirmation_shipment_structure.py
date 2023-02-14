from enum import Enum


class ShipmentConfirmationShipmentStructure(str, Enum):
    PALLETIZEDASSORTMENTCASE = "PalletizedAssortmentCase"
    LOOSEASSORTMENTCASE = "LooseAssortmentCase"
    PALLETOFITEMS = "PalletOfItems"
    PALLETIZEDSTANDARDCASE = "PalletizedStandardCase"
    LOOSESTANDARDCASE = "LooseStandardCase"
    MASTERPALLET = "MasterPallet"
    MASTERCASE = "MasterCase"

    def __str__(self) -> str:
        return str(self.value)
