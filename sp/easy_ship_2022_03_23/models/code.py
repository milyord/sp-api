from enum import Enum


class Code(str, Enum):
    INVALIDINPUT = "InvalidInput"
    INVALIDTIMESLOTID = "InvalidTimeSlotId"
    SCHEDULEDPACKAGEALREADYEXISTS = "ScheduledPackageAlreadyExists"
    SCHEDULEWINDOWEXPIRED = "ScheduleWindowExpired"
    RETRYABLEAFTERGETTINGNEWSLOTS = "RetryableAfterGettingNewSlots"
    TIMESLOTNOTAVAILABLE = "TimeSlotNotAvailable"
    RESOURCENOTFOUND = "ResourceNotFound"
    INVALIDORDERSTATE = "InvalidOrderState"
    REGIONNOTSUPPORTED = "RegionNotSupported"
    ORDERNOTELIGIBLEFORRESCHEDULING = "OrderNotEligibleForRescheduling"
    INTERNALSERVERERROR = "InternalServerError"

    def __str__(self) -> str:
        return str(self.value)
