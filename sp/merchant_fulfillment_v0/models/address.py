from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    r"""The postal address information.

    Attributes:
        name (str): The name of the addressee, or business name.
        address_line_1 (str): The street address information.
        email (str): The email address.
        city (str): The city.
        postal_code (str): The zip code or postal code.
        country_code (str): The country code. A two-character country code, in ISO 3166-1 alpha-2 format.
        phone (str): The phone number.
        address_line_2 (Union[Unset, str]): Additional street address information.
        address_line_3 (Union[Unset, str]): Additional street address information.
        district_or_county (Union[Unset, str]): The district or county.
        state_or_province_code (Union[Unset, str]): The state or province code. **Note.** Required in the Canada, US,
            and UK marketplaces. Also required for shipments originating from China.
    """

    name: str
    address_line_1: str
    email: str
    city: str
    postal_code: str
    country_code: str
    phone: str
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    district_or_county: Union[Unset, str] = UNSET
    state_or_province_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address_line_1 = self.address_line_1
        email = self.email
        city = self.city
        postal_code = self.postal_code
        country_code = self.country_code
        phone = self.phone
        address_line_2 = self.address_line_2
        address_line_3 = self.address_line_3
        district_or_county = self.district_or_county
        state_or_province_code = self.state_or_province_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
                "AddressLine1": address_line_1,
                "Email": email,
                "City": city,
                "PostalCode": postal_code,
                "CountryCode": country_code,
                "Phone": phone,
            }
        )
        if address_line_2 is not UNSET:
            field_dict["AddressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["AddressLine3"] = address_line_3
        if district_or_county is not UNSET:
            field_dict["DistrictOrCounty"] = district_or_county
        if state_or_province_code is not UNSET:
            field_dict["StateOrProvinceCode"] = state_or_province_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        address_line_1 = d.pop("AddressLine1")

        email = d.pop("Email")

        city = d.pop("City")

        postal_code = d.pop("PostalCode")

        country_code = d.pop("CountryCode")

        phone = d.pop("Phone")

        address_line_2 = d.pop("AddressLine2", UNSET)

        address_line_3 = d.pop("AddressLine3", UNSET)

        district_or_county = d.pop("DistrictOrCounty", UNSET)

        state_or_province_code = d.pop("StateOrProvinceCode", UNSET)

        result = cls(
            name=name,
            address_line_1=address_line_1,
            email=email,
            city=city,
            postal_code=postal_code,
            country_code=country_code,
            phone=phone,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            district_or_county=district_or_county,
            state_or_province_code=state_or_province_code,
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
