from enum import Enum


class ContainerContainerType(str, Enum):
    CARTON = "carton"
    PALLET = "pallet"

    def __str__(self) -> str:
        return str(self.value)
