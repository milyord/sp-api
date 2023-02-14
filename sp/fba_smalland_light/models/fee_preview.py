from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.fee_line_item import FeeLineItem
    from ..models.money_type import MoneyType


T = TypeVar("T", bound="FeePreview")


@attr.s(auto_attribs=True)
class FeePreview:
    r"""The fee estimate for a specific item.

    Attributes:
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) value used to identify the item.
        price (Union[Unset, MoneyType]):
        fee_breakdown (Union[Unset, List['FeeLineItem']]): A list of the Small and Light fees for the item.
        total_fees (Union[Unset, MoneyType]):
        errors (Union[Unset, List['Error']]): One or more unexpected errors occurred during the
            getSmallAndLightFeePreview operation.
    """

    asin: Union[Unset, str] = UNSET
    price: Union[Unset, "MoneyType"] = UNSET
    fee_breakdown: Union[Unset, List["FeeLineItem"]] = UNSET
    total_fees: Union[Unset, "MoneyType"] = UNSET
    errors: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        fee_breakdown: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fee_breakdown, Unset):
            fee_breakdown = []
            for fee_breakdown_item_data in self.fee_breakdown:
                fee_breakdown_item = fee_breakdown_item_data.to_dict()

                fee_breakdown.append(fee_breakdown_item)

        total_fees: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_fees, Unset):
            total_fees = self.total_fees.to_dict()

        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asin is not UNSET:
            field_dict["asin"] = asin
        if price is not UNSET:
            field_dict["price"] = price
        if fee_breakdown is not UNSET:
            field_dict["feeBreakdown"] = fee_breakdown
        if total_fees is not UNSET:
            field_dict["totalFees"] = total_fees
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.fee_line_item import FeeLineItem
        from ..models.money_type import MoneyType

        d = src_dict.copy()
        asin = d.pop("asin", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, MoneyType]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = MoneyType.from_dict(_price)

        fee_breakdown = []
        _fee_breakdown = d.pop("feeBreakdown", UNSET)
        for fee_breakdown_item_data in _fee_breakdown or []:
            fee_breakdown_item = FeeLineItem.from_dict(fee_breakdown_item_data)

            fee_breakdown.append(fee_breakdown_item)

        _total_fees = d.pop("totalFees", UNSET)
        total_fees: Union[Unset, MoneyType]
        if isinstance(_total_fees, Unset):
            total_fees = UNSET
        else:
            total_fees = MoneyType.from_dict(_total_fees)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = Error.from_dict(errors_item_data)

            errors.append(errors_item)

        result = cls(
            asin=asin,
            price=price,
            fee_breakdown=fee_breakdown,
            total_fees=total_fees,
            errors=errors,
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
