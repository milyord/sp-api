from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.tax_registration_details_tax_registration_type import TaxRegistrationDetailsTaxRegistrationType

T = TypeVar("T", bound="TaxRegistrationDetails")


@attr.s(auto_attribs=True)
class TaxRegistrationDetails:
    r"""Tax registration details of the entity.

    Attributes:
        tax_registration_type (TaxRegistrationDetailsTaxRegistrationType): Tax registration type for the entity.
        tax_registration_number (str): Tax registration number for the entity. For example, VAT ID.
    """

    tax_registration_type: TaxRegistrationDetailsTaxRegistrationType
    tax_registration_number: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_registration_type = self.tax_registration_type.value

        tax_registration_number = self.tax_registration_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxRegistrationType": tax_registration_type,
                "taxRegistrationNumber": tax_registration_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tax_registration_type = TaxRegistrationDetailsTaxRegistrationType(d.pop("taxRegistrationType"))

        tax_registration_number = d.pop("taxRegistrationNumber")

        result = cls(
            tax_registration_type=tax_registration_type,
            tax_registration_number=tax_registration_number,
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
