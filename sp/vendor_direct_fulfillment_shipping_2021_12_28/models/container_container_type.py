from enum import Enum


class ContainerContainerType(str, Enum):
    CARTON = "Carton"
    PALLET = "Pallet"

    def __str__(self) -> str:
        return str(self.value)
