from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    r"""Address of the party.

    Attributes:
        name (str): The name of the person, business or institution at that address.
        address_line_1 (str): First line of the address.
        city (str): The city where the person, business or institution is located.
        state_or_region (str): The state or region where person, business or institution is located.
        postal_code (str): The postal code of that address. It conatins a series of letters or digits or both, sometimes
            including spaces or punctuation.
        country_code (str): The two digit country code in ISO 3166-1 alpha-2 format.
        address_line_2 (Union[Unset, str]): Additional street address information, if required.
        address_line_3 (Union[Unset, str]): Additional street address information, if required.
        county (Union[Unset, str]): The county where person, business or institution is located.
        district (Union[Unset, str]): The district where person, business or institution is located.
        phone (Union[Unset, str]): The phone number of the person, business or institution located at that address.
    """

    name: str
    address_line_1: str
    city: str
    state_or_region: str
    postal_code: str
    country_code: str
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    county: Union[Unset, str] = UNSET
    district: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address_line_1 = self.address_line_1
        city = self.city
        state_or_region = self.state_or_region
        postal_code = self.postal_code
        country_code = self.country_code
        address_line_2 = self.address_line_2
        address_line_3 = self.address_line_3
        county = self.county
        district = self.district
        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "addressLine1": address_line_1,
                "city": city,
                "stateOrRegion": state_or_region,
                "postalCode": postal_code,
                "countryCode": country_code,
            }
        )
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if county is not UNSET:
            field_dict["county"] = county
        if district is not UNSET:
            field_dict["district"] = district
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        address_line_1 = d.pop("addressLine1")

        city = d.pop("city")

        state_or_region = d.pop("stateOrRegion")

        postal_code = d.pop("postalCode")

        country_code = d.pop("countryCode")

        address_line_2 = d.pop("addressLine2", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        county = d.pop("county", UNSET)

        district = d.pop("district", UNSET)

        phone = d.pop("phone", UNSET)

        result = cls(
            name=name,
            address_line_1=address_line_1,
            city=city,
            state_or_region=state_or_region,
            postal_code=postal_code,
            country_code=country_code,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            county=county,
            district=district,
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
