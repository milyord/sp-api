from enum import Enum


class SchemaLinkLinkVerb(str, Enum):
    GET = "GET"

    def __str__(self) -> str:
        return str(self.value)
