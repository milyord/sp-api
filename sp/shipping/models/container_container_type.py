from enum import Enum


class ContainerContainerType(str, Enum):
    PACKAGE = "PACKAGE"

    def __str__(self) -> str:
        return str(self.value)
