from enum import Enum


class CreateReportScheduleSpecificationPeriod(str, Enum):
    PT5M = "PT5M"
    PT15M = "PT15M"
    PT30M = "PT30M"
    PT1H = "PT1H"
    PT2H = "PT2H"
    PT4H = "PT4H"
    PT8H = "PT8H"
    PT12H = "PT12H"
    P1D = "P1D"
    P2D = "P2D"
    P3D = "P3D"
    PT84H = "PT84H"
    P7D = "P7D"
    P14D = "P14D"
    P15D = "P15D"
    P18D = "P18D"
    P30D = "P30D"
    P1M = "P1M"

    def __str__(self) -> str:
        return str(self.value)
