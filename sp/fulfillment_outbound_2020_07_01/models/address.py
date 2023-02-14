from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    r"""A physical address.

    Attributes:
        name (str): The name of the person, business or institution at the address.
        address_line_1 (str): The first line of the address.
        state_or_region (str): The state or region where the person, business or institution is located.
        country_code (str): The two digit country code. In ISO 3166-1 alpha-2 format.
        address_line_2 (Union[Unset, str]): Additional address information, if required.
        address_line_3 (Union[Unset, str]): Additional address information, if required.
        city (Union[Unset, str]): The city where the person, business, or institution is located.
        district_or_county (Union[Unset, str]): The district or county where the person, business, or institution is
            located.
        postal_code (Union[Unset, str]): The postal code of the address.
        phone (Union[Unset, str]): The phone number of the person, business, or institution located at the address.
    """

    name: str
    address_line_1: str
    state_or_region: str
    country_code: str
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    district_or_county: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address_line_1 = self.address_line_1
        state_or_region = self.state_or_region
        country_code = self.country_code
        address_line_2 = self.address_line_2
        address_line_3 = self.address_line_3
        city = self.city
        district_or_county = self.district_or_county
        postal_code = self.postal_code
        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "addressLine1": address_line_1,
                "stateOrRegion": state_or_region,
                "countryCode": country_code,
            }
        )
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if city is not UNSET:
            field_dict["city"] = city
        if district_or_county is not UNSET:
            field_dict["districtOrCounty"] = district_or_county
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        address_line_1 = d.pop("addressLine1")

        state_or_region = d.pop("stateOrRegion")

        country_code = d.pop("countryCode")

        address_line_2 = d.pop("addressLine2", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        city = d.pop("city", UNSET)

        district_or_county = d.pop("districtOrCounty", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        phone = d.pop("phone", UNSET)

        result = cls(
            name=name,
            address_line_1=address_line_1,
            state_or_region=state_or_region,
            country_code=country_code,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            city=city,
            district_or_county=district_or_county,
            postal_code=postal_code,
            phone=phone,
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
