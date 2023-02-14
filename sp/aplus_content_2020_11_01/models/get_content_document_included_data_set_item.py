from enum import Enum


class GetContentDocumentIncludedDataSetItem(str, Enum):
    CONTENTS = "CONTENTS"
    METADATA = "METADATA"

    def __str__(self) -> str:
        return str(self.value)
