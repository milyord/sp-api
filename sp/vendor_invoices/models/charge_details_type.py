from enum import Enum


class ChargeDetailsType(str, Enum):
    FREIGHT = "Freight"
    PACKING = "Packing"
    DUTY = "Duty"
    SERVICE = "Service"
    SMALLORDER = "SmallOrder"
    INSURANCEPLACEMENTCOST = "InsurancePlacementCost"
    INSURANCEFEE = "InsuranceFee"
    SPECIALHANDLINGSERVICE = "SpecialHandlingService"
    COLLECTIONANDRECYCLINGSERVICE = "CollectionAndRecyclingService"
    ENVIRONMENTALPROTECTIONSERVICE = "EnvironmentalProtectionService"
    TAXCOLLECTEDATSOURCE = "TaxCollectedAtSource"

    def __str__(self) -> str:
        return str(self.value)
