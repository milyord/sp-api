from enum import Enum


class ImportDetailsInternationalCommercialTerms(str, Enum):
    EXWORKS = "ExWorks"
    FREECARRIER = "FreeCarrier"
    FREEONBOARD = "FreeOnBoard"
    FREEALONGSIDESHIP = "FreeAlongSideShip"
    CARRIAGEPAIDTO = "CarriagePaidTo"
    COSTANDFREIGHT = "CostAndFreight"
    CARRIAGEANDINSURANCEPAIDTO = "CarriageAndInsurancePaidTo"
    COSTINSURANCEANDFREIGHT = "CostInsuranceAndFreight"
    DELIVEREDATTERMINAL = "DeliveredAtTerminal"
    DELIVEREDATPLACE = "DeliveredAtPlace"
    DELIVERDUTYPAID = "DeliverDutyPaid"

    def __str__(self) -> str:
        return str(self.value)
