from enum import Enum


class ResearchingQuantityEntryName(str, Enum):
    RESEARCHINGQUANTITYINSHORTTERM = "researchingQuantityInShortTerm"
    RESEARCHINGQUANTITYINMIDTERM = "researchingQuantityInMidTerm"
    RESEARCHINGQUANTITYINLONGTERM = "researchingQuantityInLongTerm"

    def __str__(self) -> str:
        return str(self.value)
