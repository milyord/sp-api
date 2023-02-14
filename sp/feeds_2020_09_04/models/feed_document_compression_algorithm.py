from enum import Enum


class FeedDocumentCompressionAlgorithm(str, Enum):
    GZIP = "GZIP"

    def __str__(self) -> str:
        return str(self.value)
