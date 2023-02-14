from enum import Enum


class PrepInstruction(str, Enum):
    POLYBAGGING = "Polybagging"
    BUBBLEWRAPPING = "BubbleWrapping"
    TAPING = "Taping"
    BLACKSHRINKWRAPPING = "BlackShrinkWrapping"
    LABELING = "Labeling"
    HANGGARMENT = "HangGarment"
    SETCREATION = "SetCreation"
    BOXING = "Boxing"
    REMOVEFROMHANGER = "RemoveFromHanger"
    DEBUNDLE = "Debundle"
    SUFFOCATIONSTICKERING = "SuffocationStickering"
    CAPSEALING = "CapSealing"
    SETSTICKERING = "SetStickering"
    BLANKSTICKERING = "BlankStickering"
    NOPREP = "NoPrep"

    def __str__(self) -> str:
        return str(self.value)
