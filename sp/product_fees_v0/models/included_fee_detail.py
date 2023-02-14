from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money_type import MoneyType


T = TypeVar("T", bound="IncludedFeeDetail")


@attr.s(auto_attribs=True)
class IncludedFeeDetail:
    r"""The type of fee, fee amount, and other details.

    Attributes:
        fee_type (str): The type of fee charged to a seller.
        fee_amount (MoneyType):
        final_fee (MoneyType):
        fee_promotion (Union[Unset, MoneyType]):
        tax_amount (Union[Unset, MoneyType]):
    """

    fee_type: str
    fee_amount: "MoneyType"
    final_fee: "MoneyType"
    fee_promotion: Union[Unset, "MoneyType"] = UNSET
    tax_amount: Union[Unset, "MoneyType"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fee_type = self.fee_type
        fee_amount = self.fee_amount.to_dict()

        final_fee = self.final_fee.to_dict()

        fee_promotion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fee_promotion, Unset):
            fee_promotion = self.fee_promotion.to_dict()

        tax_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_amount, Unset):
            tax_amount = self.tax_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FeeType": fee_type,
                "FeeAmount": fee_amount,
                "FinalFee": final_fee,
            }
        )
        if fee_promotion is not UNSET:
            field_dict["FeePromotion"] = fee_promotion
        if tax_amount is not UNSET:
            field_dict["TaxAmount"] = tax_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_type import MoneyType

        d = src_dict.copy()
        fee_type = d.pop("FeeType")

        fee_amount = MoneyType.from_dict(d.pop("FeeAmount"))

        final_fee = MoneyType.from_dict(d.pop("FinalFee"))

        _fee_promotion = d.pop("FeePromotion", UNSET)
        fee_promotion: Union[Unset, MoneyType]
        if isinstance(_fee_promotion, Unset):
            fee_promotion = UNSET
        else:
            fee_promotion = MoneyType.from_dict(_fee_promotion)

        _tax_amount = d.pop("TaxAmount", UNSET)
        tax_amount: Union[Unset, MoneyType]
        if isinstance(_tax_amount, Unset):
            tax_amount = UNSET
        else:
            tax_amount = MoneyType.from_dict(_tax_amount)

        result = cls(
            fee_type=fee_type,
            fee_amount=fee_amount,
            final_fee=final_fee,
            fee_promotion=fee_promotion,
            tax_amount=tax_amount,
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
