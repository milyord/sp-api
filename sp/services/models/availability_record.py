import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recurrence import Recurrence


T = TypeVar("T", bound="AvailabilityRecord")


@attr.s(auto_attribs=True)
class AvailabilityRecord:
    r"""`AvailabilityRecord` to represent the capacity of a resource over a time range.

    Attributes:
        start_time (datetime.datetime): Denotes the time from when the resource is available in a day in ISO-8601
            format.
        end_time (datetime.datetime): Denotes the time till when the resource is available in a day in ISO-8601 format.
        recurrence (Union[Unset, Recurrence]): Repeated occurrence of an event in a time range.
        capacity (Union[Unset, int]): Signifies the capacity of a resource which is available.
    """

    start_time: datetime.datetime
    end_time: datetime.datetime
    recurrence: Union[Unset, "Recurrence"] = UNSET
    capacity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        recurrence: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.to_dict()

        capacity = self.capacity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startTime": start_time,
                "endTime": end_time,
            }
        )
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if capacity is not UNSET:
            field_dict["capacity"] = capacity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.recurrence import Recurrence

        d = src_dict.copy()
        start_time = isoparse(d.pop("startTime"))

        end_time = isoparse(d.pop("endTime"))

        _recurrence = d.pop("recurrence", UNSET)
        recurrence: Union[Unset, Recurrence]
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = Recurrence.from_dict(_recurrence)

        capacity = d.pop("capacity", UNSET)

        result = cls(
            start_time=start_time,
            end_time=end_time,
            recurrence=recurrence,
            capacity=capacity,
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
