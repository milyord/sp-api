import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.day_of_week import DayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="Recurrence")


@attr.s(auto_attribs=True)
class Recurrence:
    r"""Repeated occurrence of an event in a time range.

    Attributes:
        end_time (datetime.datetime): End time of the recurrence.
        days_of_week (Union[Unset, List[DayOfWeek]]): Days of the week when recurrence is valid. If the schedule is
            valid every Monday, input will only contain `MONDAY` in the list.
        days_of_month (Union[Unset, List[int]]): Days of the month when recurrence is valid.
    """

    end_time: datetime.datetime
    days_of_week: Union[Unset, List[DayOfWeek]] = UNSET
    days_of_month: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_time = self.end_time.isoformat()

        days_of_week: Union[Unset, List[str]] = UNSET
        if not isinstance(self.days_of_week, Unset):
            days_of_week = []
            for days_of_week_item_data in self.days_of_week:
                days_of_week_item = days_of_week_item_data.value

                days_of_week.append(days_of_week_item)

        days_of_month: Union[Unset, List[int]] = UNSET
        if not isinstance(self.days_of_month, Unset):
            days_of_month = self.days_of_month

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endTime": end_time,
            }
        )
        if days_of_week is not UNSET:
            field_dict["daysOfWeek"] = days_of_week
        if days_of_month is not UNSET:
            field_dict["daysOfMonth"] = days_of_month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_time = isoparse(d.pop("endTime"))

        days_of_week = []
        _days_of_week = d.pop("daysOfWeek", UNSET)
        for days_of_week_item_data in _days_of_week or []:
            days_of_week_item = DayOfWeek(days_of_week_item_data)

            days_of_week.append(days_of_week_item)

        days_of_month = cast(List[int], d.pop("daysOfMonth", UNSET))

        result = cls(
            end_time=end_time,
            days_of_week=days_of_week,
            days_of_month=days_of_month,
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
