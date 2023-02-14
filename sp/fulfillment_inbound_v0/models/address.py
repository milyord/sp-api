from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    r"""
    Attributes:
        name (str): Name of the individual or business.
        address_line_1 (str): The street address information.
        city (str): The city.
        state_or_province_code (str): The state or province code.

            If state or province codes are used in your marketplace, it is recommended that you include one with your
            request. This helps Amazon to select the most appropriate Amazon fulfillment center for your inbound shipment
            plan.
        country_code (str): The country code in two-character ISO 3166-1 alpha-2 format.
        postal_code (str): The postal code.

            If postal codes are used in your marketplace, we recommended that you include one with your request. This helps
            Amazon select the most appropriate Amazon fulfillment center for the inbound shipment plan.
        address_line_2 (Union[Unset, str]): Additional street address information, if required.
        district_or_county (Union[Unset, str]): The district or county.
    """

    name: str
    address_line_1: str
    city: str
    state_or_province_code: str
    country_code: str
    postal_code: str
    address_line_2: Union[Unset, str] = UNSET
    district_or_county: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address_line_1 = self.address_line_1
        city = self.city
        state_or_province_code = self.state_or_province_code
        country_code = self.country_code
        postal_code = self.postal_code
        address_line_2 = self.address_line_2
        district_or_county = self.district_or_county

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
                "AddressLine1": address_line_1,
                "City": city,
                "StateOrProvinceCode": state_or_province_code,
                "CountryCode": country_code,
                "PostalCode": postal_code,
            }
        )
        if address_line_2 is not UNSET:
            field_dict["AddressLine2"] = address_line_2
        if district_or_county is not UNSET:
            field_dict["DistrictOrCounty"] = district_or_county

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        address_line_1 = d.pop("AddressLine1")

        city = d.pop("City")

        state_or_province_code = d.pop("StateOrProvinceCode")

        country_code = d.pop("CountryCode")

        postal_code = d.pop("PostalCode")

        address_line_2 = d.pop("AddressLine2", UNSET)

        district_or_county = d.pop("DistrictOrCounty", UNSET)

        result = cls(
            name=name,
            address_line_1=address_line_1,
            city=city,
            state_or_province_code=state_or_province_code,
            country_code=country_code,
            postal_code=postal_code,
            address_line_2=address_line_2,
            district_or_county=district_or_county,
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
