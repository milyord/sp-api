from enum import Enum


class ListContentDocumentAsinRelationsIncludedDataSetItem(str, Enum):
    METADATA = "METADATA"

    def __str__(self) -> str:
        return str(self.value)
