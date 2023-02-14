from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.detailed_shipping_time_type_availability_type import DetailedShippingTimeTypeAvailabilityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DetailedShippingTimeType")


@attr.s(auto_attribs=True)
class DetailedShippingTimeType:
    r"""The time range in which an item will likely be shipped once an order has been placed.

    Attributes:
        minimum_hours (Union[Unset, int]): The minimum time, in hours, that the item will likely be shipped after the
            order has been placed.
        maximum_hours (Union[Unset, int]): The maximum time, in hours, that the item will likely be shipped after the
            order has been placed.
        available_date (Union[Unset, str]): The date when the item will be available for shipping. Only displayed for
            items that are not currently available for shipping.
        availability_type (Union[Unset, DetailedShippingTimeTypeAvailabilityType]): Indicates whether the item is
            available for shipping now, or on a known or an unknown date in the future. If known, the availableDate property
            indicates the date that the item will be available for shipping. Possible values: NOW, FUTURE_WITHOUT_DATE,
            FUTURE_WITH_DATE.
    """

    minimum_hours: Union[Unset, int] = UNSET
    maximum_hours: Union[Unset, int] = UNSET
    available_date: Union[Unset, str] = UNSET
    availability_type: Union[Unset, DetailedShippingTimeTypeAvailabilityType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        minimum_hours = self.minimum_hours
        maximum_hours = self.maximum_hours
        available_date = self.available_date
        availability_type: Union[Unset, str] = UNSET
        if not isinstance(self.availability_type, Unset):
            availability_type = self.availability_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minimum_hours is not UNSET:
            field_dict["minimumHours"] = minimum_hours
        if maximum_hours is not UNSET:
            field_dict["maximumHours"] = maximum_hours
        if available_date is not UNSET:
            field_dict["availableDate"] = available_date
        if availability_type is not UNSET:
            field_dict["availabilityType"] = availability_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        minimum_hours = d.pop("minimumHours", UNSET)

        maximum_hours = d.pop("maximumHours", UNSET)

        available_date = d.pop("availableDate", UNSET)

        _availability_type = d.pop("availabilityType", UNSET)
        availability_type: Union[Unset, DetailedShippingTimeTypeAvailabilityType]
        if isinstance(_availability_type, Unset):
            availability_type = UNSET
        else:
            availability_type = DetailedShippingTimeTypeAvailabilityType(_availability_type)

        result = cls(
            minimum_hours=minimum_hours,
            maximum_hours=maximum_hours,
            available_date=available_date,
            availability_type=availability_type,
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
