from enum import Enum


class TransportationDetailsTransportationMode(str, Enum):
    ROAD = "Road"
    AIR = "Air"
    OCEAN = "Ocean"

    def __str__(self) -> str:
        return str(self.value)
