from enum import Enum


class TaxCollectionResponsibleParty(str, Enum):
    AMAZON_SERVICES_INC = "Amazon Services, Inc."

    def __str__(self) -> str:
        return str(self.value)
