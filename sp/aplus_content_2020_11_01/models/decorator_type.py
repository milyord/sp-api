from enum import Enum


class DecoratorType(str, Enum):
    LIST_ITEM = "LIST_ITEM"
    LIST_ORDERED = "LIST_ORDERED"
    LIST_UNORDERED = "LIST_UNORDERED"
    STYLE_BOLD = "STYLE_BOLD"
    STYLE_ITALIC = "STYLE_ITALIC"
    STYLE_LINEBREAK = "STYLE_LINEBREAK"
    STYLE_PARAGRAPH = "STYLE_PARAGRAPH"
    STYLE_UNDERLINE = "STYLE_UNDERLINE"

    def __str__(self) -> str:
        return str(self.value)
