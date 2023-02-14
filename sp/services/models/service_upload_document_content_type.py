from enum import Enum


class ServiceUploadDocumentContentType(str, Enum):
    TIFF = "TIFF"
    JPG = "JPG"
    PNG = "PNG"
    JPEG = "JPEG"
    GIF = "GIF"
    PDF = "PDF"

    def __str__(self) -> str:
        return str(self.value)
