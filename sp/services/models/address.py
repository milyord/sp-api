from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    r"""The shipping address for the service job.

    Attributes:
        name (str): The name of the person, business, or institution.
        address_line_1 (str): The first line of the address.
        address_line_2 (Union[Unset, str]): Additional address information, if required.
        address_line_3 (Union[Unset, str]): Additional address information, if required.
        city (Union[Unset, str]): The city.
        county (Union[Unset, str]): The county.
        district (Union[Unset, str]): The district.
        state_or_region (Union[Unset, str]): The state or region.
        postal_code (Union[Unset, str]): The postal code. This can contain letters, digits, spaces, and/or punctuation.
        country_code (Union[Unset, str]): The two digit country code, in ISO 3166-1 alpha-2 format.
        phone (Union[Unset, str]): The phone number.
    """

    name: str
    address_line_1: str
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    county: Union[Unset, str] = UNSET
    district: Union[Unset, str] = UNSET
    state_or_region: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address_line_1 = self.address_line_1
        address_line_2 = self.address_line_2
        address_line_3 = self.address_line_3
        city = self.city
        county = self.county
        district = self.district
        state_or_region = self.state_or_region
        postal_code = self.postal_code
        country_code = self.country_code
        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "addressLine1": address_line_1,
            }
        )
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if city is not UNSET:
            field_dict["city"] = city
        if county is not UNSET:
            field_dict["county"] = county
        if district is not UNSET:
            field_dict["district"] = district
        if state_or_region is not UNSET:
            field_dict["stateOrRegion"] = state_or_region
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        address_line_1 = d.pop("addressLine1")

        address_line_2 = d.pop("addressLine2", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        city = d.pop("city", UNSET)

        county = d.pop("county", UNSET)

        district = d.pop("district", UNSET)

        state_or_region = d.pop("stateOrRegion", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        country_code = d.pop("countryCode", UNSET)

        phone = d.pop("phone", UNSET)

        result = cls(
            name=name,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            city=city,
            county=county,
            district=district,
            state_or_region=state_or_region,
            postal_code=postal_code,
            country_code=country_code,
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
