from enum import Enum


class ReportDocumentCompressionAlgorithm(str, Enum):
    GZIP = "GZIP"

    def __str__(self) -> str:
        return str(self.value)
