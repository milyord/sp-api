from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tax_registration_detail_tax_registration_type import TaxRegistrationDetailTaxRegistrationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="TaxRegistrationDetail")


@attr.s(auto_attribs=True)
class TaxRegistrationDetail:
    r"""Tax registration details of the entity.

    Attributes:
        tax_registration_number (str): Tax registration number for the party. For example, VAT ID.
        tax_registration_type (Union[Unset, TaxRegistrationDetailTaxRegistrationType]): Tax registration type for the
            entity.
        tax_registration_address (Union[Unset, Address]): Address of the party.
        tax_registration_message (Union[Unset, str]): Tax registration message that can be used for additional tax
            related details.
    """

    tax_registration_number: str
    tax_registration_type: Union[Unset, TaxRegistrationDetailTaxRegistrationType] = UNSET
    tax_registration_address: Union[Unset, "Address"] = UNSET
    tax_registration_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_registration_number = self.tax_registration_number
        tax_registration_type: Union[Unset, str] = UNSET
        if not isinstance(self.tax_registration_type, Unset):
            tax_registration_type = self.tax_registration_type.value

        tax_registration_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_registration_address, Unset):
            tax_registration_address = self.tax_registration_address.to_dict()

        tax_registration_message = self.tax_registration_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxRegistrationNumber": tax_registration_number,
            }
        )
        if tax_registration_type is not UNSET:
            field_dict["taxRegistrationType"] = tax_registration_type
        if tax_registration_address is not UNSET:
            field_dict["taxRegistrationAddress"] = tax_registration_address
        if tax_registration_message is not UNSET:
            field_dict["taxRegistrationMessage"] = tax_registration_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        tax_registration_number = d.pop("taxRegistrationNumber")

        _tax_registration_type = d.pop("taxRegistrationType", UNSET)
        tax_registration_type: Union[Unset, TaxRegistrationDetailTaxRegistrationType]
        if isinstance(_tax_registration_type, Unset):
            tax_registration_type = UNSET
        else:
            tax_registration_type = TaxRegistrationDetailTaxRegistrationType(_tax_registration_type)

        _tax_registration_address = d.pop("taxRegistrationAddress", UNSET)
        tax_registration_address: Union[Unset, Address]
        if isinstance(_tax_registration_address, Unset):
            tax_registration_address = UNSET
        else:
            tax_registration_address = Address.from_dict(_tax_registration_address)

        tax_registration_message = d.pop("taxRegistrationMessage", UNSET)

        result = cls(
            tax_registration_number=tax_registration_number,
            tax_registration_type=tax_registration_type,
            tax_registration_address=tax_registration_address,
            tax_registration_message=tax_registration_message,
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
