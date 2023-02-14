from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tax_details_type import TaxDetailsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="TaxDetails")


@attr.s(auto_attribs=True)
class TaxDetails:
    r"""
    Attributes:
        tax_amount (Money): An amount of money, including units in the form of currency.
        tax_rate (Union[Unset, str]): A decimal number with no loss of precision. Useful when precision loss is
            unacceptable, as with currencies. Follows RFC7159 for number representation.
        taxable_amount (Union[Unset, Money]): An amount of money, including units in the form of currency.
        type (Union[Unset, TaxDetailsType]): Tax type.
    """

    tax_amount: "Money"
    tax_rate: Union[Unset, str] = UNSET
    taxable_amount: Union[Unset, "Money"] = UNSET
    type: Union[Unset, TaxDetailsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_amount = self.tax_amount.to_dict()

        tax_rate = self.tax_rate
        taxable_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.taxable_amount, Unset):
            taxable_amount = self.taxable_amount.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxAmount": tax_amount,
            }
        )
        if tax_rate is not UNSET:
            field_dict["taxRate"] = tax_rate
        if taxable_amount is not UNSET:
            field_dict["taxableAmount"] = taxable_amount
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        tax_amount = Money.from_dict(d.pop("taxAmount"))

        tax_rate = d.pop("taxRate", UNSET)

        _taxable_amount = d.pop("taxableAmount", UNSET)
        taxable_amount: Union[Unset, Money]
        if isinstance(_taxable_amount, Unset):
            taxable_amount = UNSET
        else:
            taxable_amount = Money.from_dict(_taxable_amount)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TaxDetailsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TaxDetailsType(_type)

        result = cls(
            tax_amount=tax_amount,
            tax_rate=tax_rate,
            taxable_amount=taxable_amount,
            type=type,
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
