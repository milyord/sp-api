from enum import Enum


class AsinBadge(str, Enum):
    BRAND_NOT_ELIGIBLE = "BRAND_NOT_ELIGIBLE"
    CATALOG_NOT_FOUND = "CATALOG_NOT_FOUND"
    CONTENT_NOT_PUBLISHED = "CONTENT_NOT_PUBLISHED"
    CONTENT_PUBLISHED = "CONTENT_PUBLISHED"

    def __str__(self) -> str:
        return str(self.value)
