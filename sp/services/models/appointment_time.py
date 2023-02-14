import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="AppointmentTime")


@attr.s(auto_attribs=True)
class AppointmentTime:
    r"""The time of the appointment window.

    Attributes:
        start_time (datetime.datetime): The date and time of the start of the appointment window in ISO 8601 format.
        duration_in_minutes (int): The duration of the appointment window, in minutes.
    """

    start_time: datetime.datetime
    duration_in_minutes: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_time = self.start_time.isoformat()

        duration_in_minutes = self.duration_in_minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startTime": start_time,
                "durationInMinutes": duration_in_minutes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_time = isoparse(d.pop("startTime"))

        duration_in_minutes = d.pop("durationInMinutes")

        result = cls(
            start_time=start_time,
            duration_in_minutes=duration_in_minutes,
        )

        result.additional_properties = d
        return result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
