from enum import Enum


class RegulatedInformationFieldFieldType(str, Enum):
    TEXT = "Text"
    FILEATTACHMENT = "FileAttachment"

    def __str__(self) -> str:
        return str(self.value)
