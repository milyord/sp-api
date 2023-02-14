from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyerTaxInformation")


@attr.s(auto_attribs=True)
class BuyerTaxInformation:
    r"""Contains the business invoice tax information. Available only in the TR marketplace.

    Attributes:
        buyer_legal_company_name (Union[Unset, str]): Business buyer's company legal name.
        buyer_business_address (Union[Unset, str]): Business buyer's address.
        buyer_tax_registration_id (Union[Unset, str]): Business buyer's tax registration ID.
        buyer_tax_office (Union[Unset, str]): Business buyer's tax office.
    """

    buyer_legal_company_name: Union[Unset, str] = UNSET
    buyer_business_address: Union[Unset, str] = UNSET
    buyer_tax_registration_id: Union[Unset, str] = UNSET
    buyer_tax_office: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        buyer_legal_company_name = self.buyer_legal_company_name
        buyer_business_address = self.buyer_business_address
        buyer_tax_registration_id = self.buyer_tax_registration_id
        buyer_tax_office = self.buyer_tax_office

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buyer_legal_company_name is not UNSET:
            field_dict["BuyerLegalCompanyName"] = buyer_legal_company_name
        if buyer_business_address is not UNSET:
            field_dict["BuyerBusinessAddress"] = buyer_business_address
        if buyer_tax_registration_id is not UNSET:
            field_dict["BuyerTaxRegistrationId"] = buyer_tax_registration_id
        if buyer_tax_office is not UNSET:
            field_dict["BuyerTaxOffice"] = buyer_tax_office

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        buyer_legal_company_name = d.pop("BuyerLegalCompanyName", UNSET)

        buyer_business_address = d.pop("BuyerBusinessAddress", UNSET)

        buyer_tax_registration_id = d.pop("BuyerTaxRegistrationId", UNSET)

        buyer_tax_office = d.pop("BuyerTaxOffice", UNSET)

        result = cls(
            buyer_legal_company_name=buyer_legal_company_name,
            buyer_business_address=buyer_business_address,
            buyer_tax_registration_id=buyer_tax_registration_id,
            buyer_tax_office=buyer_tax_office,
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
