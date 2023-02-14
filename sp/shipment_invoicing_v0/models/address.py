from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.address_type_enum import AddressTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    r"""The shipping address details of the shipment.

    Attributes:
        name (Union[Unset, str]): The name.
        address_line_1 (Union[Unset, str]): The street address.
        address_line_2 (Union[Unset, str]): Additional street address information, if required.
        address_line_3 (Union[Unset, str]): Additional street address information, if required.
        city (Union[Unset, str]): The city.
        county (Union[Unset, str]): The county.
        district (Union[Unset, str]): The district.
        state_or_region (Union[Unset, str]): The state or region.
        postal_code (Union[Unset, str]): The postal code.
        country_code (Union[Unset, str]): The country code.
        phone (Union[Unset, str]): The phone number.
        address_type (Union[Unset, AddressTypeEnum]): The shipping address type.
    """

    name: Union[Unset, str] = UNSET
    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    county: Union[Unset, str] = UNSET
    district: Union[Unset, str] = UNSET
    state_or_region: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    address_type: Union[Unset, AddressTypeEnum] = UNSET
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
        address_type: Union[Unset, str] = UNSET
        if not isinstance(self.address_type, Unset):
            address_type = self.address_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if address_line_1 is not UNSET:
            field_dict["AddressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["AddressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["AddressLine3"] = address_line_3
        if city is not UNSET:
            field_dict["City"] = city
        if county is not UNSET:
            field_dict["County"] = county
        if district is not UNSET:
            field_dict["District"] = district
        if state_or_region is not UNSET:
            field_dict["StateOrRegion"] = state_or_region
        if postal_code is not UNSET:
            field_dict["PostalCode"] = postal_code
        if country_code is not UNSET:
            field_dict["CountryCode"] = country_code
        if phone is not UNSET:
            field_dict["Phone"] = phone
        if address_type is not UNSET:
            field_dict["AddressType"] = address_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        address_line_1 = d.pop("AddressLine1", UNSET)

        address_line_2 = d.pop("AddressLine2", UNSET)

        address_line_3 = d.pop("AddressLine3", UNSET)

        city = d.pop("City", UNSET)

        county = d.pop("County", UNSET)

        district = d.pop("District", UNSET)

        state_or_region = d.pop("StateOrRegion", UNSET)

        postal_code = d.pop("PostalCode", UNSET)

        country_code = d.pop("CountryCode", UNSET)

        phone = d.pop("Phone", UNSET)

        _address_type = d.pop("AddressType", UNSET)
        address_type: Union[Unset, AddressTypeEnum]
        if isinstance(_address_type, Unset):
            address_type = UNSET
        else:
            address_type = AddressTypeEnum(_address_type)

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
            address_type=address_type,
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
