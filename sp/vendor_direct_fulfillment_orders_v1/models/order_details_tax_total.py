from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_details import TaxDetails


T = TypeVar("T", bound="OrderDetailsTaxTotal")


@attr.s(auto_attribs=True)
class OrderDetailsTaxTotal:
    r"""
    Attributes:
        tax_line_item (Union[Unset, List['TaxDetails']]): A list of tax line items.
    """

    tax_line_item: Union[Unset, List["TaxDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_line_item: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_line_item, Unset):
            tax_line_item = []
            for componentsschemas_tax_line_item_item_data in self.tax_line_item:
                componentsschemas_tax_line_item_item = componentsschemas_tax_line_item_item_data.to_dict()

                tax_line_item.append(componentsschemas_tax_line_item_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tax_line_item is not UNSET:
            field_dict["taxLineItem"] = tax_line_item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_details import TaxDetails

        d = src_dict.copy()
        tax_line_item = []
        _tax_line_item = d.pop("taxLineItem", UNSET)
        for componentsschemas_tax_line_item_item_data in _tax_line_item or []:
            componentsschemas_tax_line_item_item = TaxDetails.from_dict(componentsschemas_tax_line_item_item_data)

            tax_line_item.append(componentsschemas_tax_line_item_item)

        result = cls(
            tax_line_item=tax_line_item,
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
