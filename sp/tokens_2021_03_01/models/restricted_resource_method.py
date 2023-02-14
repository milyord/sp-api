from enum import Enum


class RestrictedResourceMethod(str, Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"

    def __str__(self) -> str:
        return str(self.value)
