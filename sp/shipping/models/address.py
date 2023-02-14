from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    r"""The address.

    Attributes:
        name (str): The name of the person, business or institution at that address.
        address_line_1 (str): First line of that address.
        state_or_region (str): The state or region where the person, business or institution is located.
        city (str): The city where the person, business or institution is located.
        country_code (str): The two digit country code. In ISO 3166-1 alpha-2 format.
        postal_code (str): The postal code of that address. It contains a series of letters or digits or both, sometimes
            including spaces or punctuation.
        address_line_2 (Union[Unset, str]): Additional address information, if required.
        address_line_3 (Union[Unset, str]): Additional address information, if required.
        email (Union[Unset, str]): The email address of the contact associated with the address.
        copy_emails (Union[Unset, List[str]]): The email cc addresses of the contact associated with the address.
        phone_number (Union[Unset, str]): The phone number of the person, business or institution located at that
            address.
    """

    name: str
    address_line_1: str
    state_or_region: str
    city: str
    country_code: str
    postal_code: str
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    copy_emails: Union[Unset, List[str]] = UNSET
    phone_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address_line_1 = self.address_line_1
        state_or_region = self.state_or_region
        city = self.city
        country_code = self.country_code
        postal_code = self.postal_code
        address_line_2 = self.address_line_2
        address_line_3 = self.address_line_3
        email = self.email
        copy_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.copy_emails, Unset):
            copy_emails = self.copy_emails

        phone_number = self.phone_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "addressLine1": address_line_1,
                "stateOrRegion": state_or_region,
                "city": city,
                "countryCode": country_code,
                "postalCode": postal_code,
            }
        )
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if email is not UNSET:
            field_dict["email"] = email
        if copy_emails is not UNSET:
            field_dict["copyEmails"] = copy_emails
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        address_line_1 = d.pop("addressLine1")

        state_or_region = d.pop("stateOrRegion")

        city = d.pop("city")

        country_code = d.pop("countryCode")

        postal_code = d.pop("postalCode")

        address_line_2 = d.pop("addressLine2", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        email = d.pop("email", UNSET)

        copy_emails = cast(List[str], d.pop("copyEmails", UNSET))

        phone_number = d.pop("phoneNumber", UNSET)

        result = cls(
            name=name,
            address_line_1=address_line_1,
            state_or_region=state_or_region,
            city=city,
            country_code=country_code,
            postal_code=postal_code,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            email=email,
            copy_emails=copy_emails,
            phone_number=phone_number,
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
