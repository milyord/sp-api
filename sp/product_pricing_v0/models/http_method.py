from enum import Enum


class HttpMethod(str, Enum):
    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
