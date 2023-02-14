from enum import Enum


class GetLabelsPageType(str, Enum):
    PACKAGELABEL_LETTER_2 = "PackageLabel_Letter_2"
    PACKAGELABEL_LETTER_4 = "PackageLabel_Letter_4"
    PACKAGELABEL_LETTER_6 = "PackageLabel_Letter_6"
    PACKAGELABEL_LETTER_6_CARRIERLEFT = "PackageLabel_Letter_6_CarrierLeft"
    PACKAGELABEL_A4_2 = "PackageLabel_A4_2"
    PACKAGELABEL_A4_4 = "PackageLabel_A4_4"
    PACKAGELABEL_PLAIN_PAPER = "PackageLabel_Plain_Paper"
    PACKAGELABEL_PLAIN_PAPER_CARRIERBOTTOM = "PackageLabel_Plain_Paper_CarrierBottom"
    PACKAGELABEL_THERMAL = "PackageLabel_Thermal"
    PACKAGELABEL_THERMAL_UNIFIED = "PackageLabel_Thermal_Unified"
    PACKAGELABEL_THERMAL_NONPCP = "PackageLabel_Thermal_NonPCP"
    PACKAGELABEL_THERMAL_NO_CARRIER_ROTATION = "PackageLabel_Thermal_No_Carrier_Rotation"

    def __str__(self) -> str:
        return str(self.value)
