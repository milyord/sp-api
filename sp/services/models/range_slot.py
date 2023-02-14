import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RangeSlot")


@attr.s(auto_attribs=True)
class RangeSlot:
    r"""Capacity slots represented in a format similar to availability rules.

    Attributes:
        start_date_time (Union[Unset, datetime.datetime]): Start date time of slot in ISO 8601 format with precision of
            seconds.
        end_date_time (Union[Unset, datetime.datetime]): End date time of slot in ISO 8601 format with precision of
            seconds.
        capacity (Union[Unset, int]): Capacity of the slot.
    """

    start_date_time: Union[Unset, datetime.datetime] = UNSET
    end_date_time: Union[Unset, datetime.datetime] = UNSET
    capacity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

        capacity = self.capacity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if capacity is not UNSET:
            field_dict["capacity"] = capacity

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

        _end_date_time = d.pop("endDateTime", UNSET)
        end_date_time: Union[Unset, datetime.datetime]
        if isinstance(_end_date_time, Unset):
            end_date_time = UNSET
        else:
            end_date_time = isoparse(_end_date_time)

        capacity = d.pop("capacity", UNSET)

        result = cls(
            start_date_time=start_date_time,
            end_date_time=end_date_time,
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
