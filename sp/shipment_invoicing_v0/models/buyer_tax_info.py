from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_classification import TaxClassification


T = TypeVar("T", bound="BuyerTaxInfo")


@attr.s(auto_attribs=True)
class BuyerTaxInfo:
    r"""Tax information about the buyer.

    Attributes:
        company_legal_name (Union[Unset, str]): The legal name of the company.
        taxing_region (Union[Unset, str]): The country or region imposing the tax.
        tax_classifications (Union[Unset, List['TaxClassification']]): The list of tax classifications.
    """

    company_legal_name: Union[Unset, str] = UNSET
    taxing_region: Union[Unset, str] = UNSET
    tax_classifications: Union[Unset, List["TaxClassification"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company_legal_name = self.company_legal_name
        taxing_region = self.taxing_region
        tax_classifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_classifications, Unset):
            tax_classifications = []
            for componentsschemas_tax_classification_list_item_data in self.tax_classifications:
                componentsschemas_tax_classification_list_item = (
                    componentsschemas_tax_classification_list_item_data.to_dict()
                )

                tax_classifications.append(componentsschemas_tax_classification_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_legal_name is not UNSET:
            field_dict["CompanyLegalName"] = company_legal_name
        if taxing_region is not UNSET:
            field_dict["TaxingRegion"] = taxing_region
        if tax_classifications is not UNSET:
            field_dict["TaxClassifications"] = tax_classifications

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_classification import TaxClassification

        d = src_dict.copy()
        company_legal_name = d.pop("CompanyLegalName", UNSET)

        taxing_region = d.pop("TaxingRegion", UNSET)

        tax_classifications = []
        _tax_classifications = d.pop("TaxClassifications", UNSET)
        for componentsschemas_tax_classification_list_item_data in _tax_classifications or []:
            componentsschemas_tax_classification_list_item = TaxClassification.from_dict(
                componentsschemas_tax_classification_list_item_data
            )

            tax_classifications.append(componentsschemas_tax_classification_list_item)

        result = cls(
            company_legal_name=company_legal_name,
            taxing_region=taxing_region,
            tax_classifications=tax_classifications,
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
