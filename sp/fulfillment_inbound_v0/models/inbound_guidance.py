from enum import Enum


class InboundGuidance(str, Enum):
    INBOUNDNOTRECOMMENDED = "InboundNotRecommended"
    INBOUNDOK = "InboundOK"

    def __str__(self) -> str:
        return str(self.value)
