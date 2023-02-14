from enum import Enum


class VolumeUnitOfMeasure(str, Enum):
    CUFT = "CuFt"
    CUIN = "CuIn"
    CUM = "CuM"
    CUY = "CuY"

    def __str__(self) -> str:
        return str(self.value)
