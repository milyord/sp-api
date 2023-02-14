from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Location")


@attr.s(auto_attribs=True)
class Location:
    r"""The location where the person, business or institution is located.

    Attributes:
        state_or_region (Union[Unset, str]): The state or region where the person, business or institution is located.
        city (Union[Unset, str]): The city where the person, business or institution is located.
        country_code (Union[Unset, str]): The two digit country code. In ISO 3166-1 alpha-2 format.
        postal_code (Union[Unset, str]): The postal code of that address. It contains a series of letters or digits or
            both, sometimes including spaces or punctuation.
    """

    state_or_region: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state_or_region = self.state_or_region
        city = self.city
        country_code = self.country_code
        postal_code = self.postal_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state_or_region is not UNSET:
            field_dict["stateOrRegion"] = state_or_region
        if city is not UNSET:
            field_dict["city"] = city
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state_or_region = d.pop("stateOrRegion", UNSET)

        city = d.pop("city", UNSET)

        country_code = d.pop("countryCode", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        result = cls(
            state_or_region=state_or_region,
            city=city,
            country_code=country_code,
            postal_code=postal_code,
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
