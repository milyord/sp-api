from enum import Enum


class FeedDocumentEncryptionDetailsStandard(str, Enum):
    AES = "AES"

    def __str__(self) -> str:
        return str(self.value)
