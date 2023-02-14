from enum import Enum


class AppointmentSlotReportSchedulingType(str, Enum):
    REAL_TIME_SCHEDULING = "REAL_TIME_SCHEDULING"
    NON_REAL_TIME_SCHEDULING = "NON_REAL_TIME_SCHEDULING"

    def __str__(self) -> str:
        return str(self.value)
