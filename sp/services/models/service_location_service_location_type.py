from enum import Enum


class ServiceLocationServiceLocationType(str, Enum):
    IN_HOME = "IN_HOME"
    IN_STORE = "IN_STORE"
    ONLINE = "ONLINE"

    def __str__(self) -> str:
        return str(self.value)
