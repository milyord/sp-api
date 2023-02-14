import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.capacity_type import CapacityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RangeSlotCapacityQuery")


@attr.s(auto_attribs=True)
class RangeSlotCapacityQuery:
    r"""Request schema for the `getRangeSlotCapacity` operation. This schema is used to define the time range and capacity
    types that are being queried.

        Attributes:
            start_date_time (datetime.datetime): Start date time from which the capacity slots are being requested in ISO
                8601 format.
            end_date_time (datetime.datetime): End date time up to which the capacity slots are being requested in ISO 8601
                format.
            capacity_types (Union[Unset, List[CapacityType]]): An array of capacity types which are being requested. Default
                value is `[SCHEDULED_CAPACITY]`.
    """

    start_date_time: datetime.datetime
    end_date_time: datetime.datetime
    capacity_types: Union[Unset, List[CapacityType]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date_time = self.start_date_time.isoformat()

        end_date_time = self.end_date_time.isoformat()

        capacity_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.capacity_types, Unset):
            capacity_types = []
            for capacity_types_item_data in self.capacity_types:
                capacity_types_item = capacity_types_item_data.value

                capacity_types.append(capacity_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startDateTime": start_date_time,
                "endDateTime": end_date_time,
            }
        )
        if capacity_types is not UNSET:
            field_dict["capacityTypes"] = capacity_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date_time = isoparse(d.pop("startDateTime"))

        end_date_time = isoparse(d.pop("endDateTime"))

        capacity_types = []
        _capacity_types = d.pop("capacityTypes", UNSET)
        for capacity_types_item_data in _capacity_types or []:
            capacity_types_item = CapacityType(capacity_types_item_data)

            capacity_types.append(capacity_types_item)

        result = cls(
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            capacity_types=capacity_types,
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
