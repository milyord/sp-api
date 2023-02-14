import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FixedSlot")


@attr.s(auto_attribs=True)
class FixedSlot:
    r"""In this slot format each slot only has the requested capacity types. This slot size is as specified by slot
    duration.

        Attributes:
            start_date_time (Union[Unset, datetime.datetime]): Start date time of slot in ISO 8601 format with precision of
                seconds.
            scheduled_capacity (Union[Unset, int]): Scheduled capacity corresponding to the slot. This capacity represents
                the originally allocated capacity as per resource schedule.
            available_capacity (Union[Unset, int]): Available capacity corresponding to the slot. This capacity represents
                the capacity available for allocation to reservations.
            encumbered_capacity (Union[Unset, int]): Encumbered capacity corresponding to the slot. This capacity represents
                the capacity allocated for Amazon Jobs/Appointments/Orders.
            reserved_capacity (Union[Unset, int]): Reserved capacity corresponding to the slot. This capacity represents the
                capacity made unavailable due to events like Breaks/Leaves/Lunch.
    """

    start_date_time: Union[Unset, datetime.datetime] = UNSET
    scheduled_capacity: Union[Unset, int] = UNSET
    available_capacity: Union[Unset, int] = UNSET
    encumbered_capacity: Union[Unset, int] = UNSET
    reserved_capacity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        scheduled_capacity = self.scheduled_capacity
        available_capacity = self.available_capacity
        encumbered_capacity = self.encumbered_capacity
        reserved_capacity = self.reserved_capacity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if scheduled_capacity is not UNSET:
            field_dict["scheduledCapacity"] = scheduled_capacity
        if available_capacity is not UNSET:
            field_dict["availableCapacity"] = available_capacity
        if encumbered_capacity is not UNSET:
            field_dict["encumberedCapacity"] = encumbered_capacity
        if reserved_capacity is not UNSET:
            field_dict["reservedCapacity"] = reserved_capacity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: Union[Unset, datetime.datetime]
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        scheduled_capacity = d.pop("scheduledCapacity", UNSET)

        available_capacity = d.pop("availableCapacity", UNSET)

        encumbered_capacity = d.pop("encumberedCapacity", UNSET)

        reserved_capacity = d.pop("reservedCapacity", UNSET)

        result = cls(
            start_date_time=start_date_time,
            scheduled_capacity=scheduled_capacity,
            available_capacity=available_capacity,
            encumbered_capacity=encumbered_capacity,
            reserved_capacity=reserved_capacity,
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
