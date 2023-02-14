from enum import Enum


class FileType(str, Enum):
    APPLICATIONPDF = "application/pdf"
    APPLICATIONZPL = "application/zpl"
    IMAGEPNG = "image/png"

    def __str__(self) -> str:
        return str(self.value)
