from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.charge_details_type import ChargeDetailsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money
    from ..models.tax_detail import TaxDetail


T = TypeVar("T", bound="ChargeDetails")


@attr.s(auto_attribs=True)
class ChargeDetails:
    r"""Monetary and tax details of the charge.

    Attributes:
        type (ChargeDetailsType): Type of charge applied.
        charge_amount (Money): An amount of money, including units in the form of currency.
        tax_details (Union[Unset, List['TaxDetail']]): Individual tax details per line item.
    """

    type: ChargeDetailsType
    charge_amount: "Money"
    tax_details: Union[Unset, List["TaxDetail"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        charge_amount = self.charge_amount.to_dict()

        tax_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_details, Unset):
            tax_details = []
            for tax_details_item_data in self.tax_details:
                tax_details_item = tax_details_item_data.to_dict()

                tax_details.append(tax_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "chargeAmount": charge_amount,
            }
        )
        if tax_details is not UNSET:
            field_dict["taxDetails"] = tax_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money
        from ..models.tax_detail import TaxDetail

        d = src_dict.copy()
        type = ChargeDetailsType(d.pop("type"))

        charge_amount = Money.from_dict(d.pop("chargeAmount"))

        tax_details = []
        _tax_details = d.pop("taxDetails", UNSET)
        for tax_details_item_data in _tax_details or []:
            tax_details_item = TaxDetail.from_dict(tax_details_item_data)

            tax_details.append(tax_details_item)

        result = cls(
            type=type,
            charge_amount=charge_amount,
            tax_details=tax_details,
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
