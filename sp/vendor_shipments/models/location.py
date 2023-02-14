from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Location")


@attr.s(auto_attribs=True)
class Location:
    r"""Location identifier.

    Attributes:
        type (Union[Unset, str]): Type of location identification.
        location_code (Union[Unset, str]): Location code.
        country_code (Union[Unset, str]): The two digit country code. In ISO 3166-1 alpha-2 format.
    """

    type: Union[Unset, str] = UNSET
    location_code: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        location_code = self.location_code
        country_code = self.country_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if location_code is not UNSET:
            field_dict["locationCode"] = location_code
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        location_code = d.pop("locationCode", UNSET)

        country_code = d.pop("countryCode", UNSET)

        result = cls(
            type=type,
            location_code=location_code,
            country_code=country_code,
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
