from enum import Enum


class GetServiceJobsSortField(str, Enum):
    JOB_DATE = "JOB_DATE"
    JOB_STATUS = "JOB_STATUS"

    def __str__(self) -> str:
        return str(self.value)
