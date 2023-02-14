from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="Promotion")


@attr.s(auto_attribs=True)
class Promotion:
    r"""A promotion applied to an item.

    Attributes:
        promotion_type (Union[Unset, str]): The type of promotion.
        promotion_id (Union[Unset, str]): The seller-specified identifier for the promotion.
        promotion_amount (Union[Unset, Currency]): A currency type and amount.
    """

    promotion_type: Union[Unset, str] = UNSET
    promotion_id: Union[Unset, str] = UNSET
    promotion_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promotion_type = self.promotion_type
        promotion_id = self.promotion_id
        promotion_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promotion_amount, Unset):
            promotion_amount = self.promotion_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promotion_type is not UNSET:
            field_dict["PromotionType"] = promotion_type
        if promotion_id is not UNSET:
            field_dict["PromotionId"] = promotion_id
        if promotion_amount is not UNSET:
            field_dict["PromotionAmount"] = promotion_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        promotion_type = d.pop("PromotionType", UNSET)

        promotion_id = d.pop("PromotionId", UNSET)

        _promotion_amount = d.pop("PromotionAmount", UNSET)
        promotion_amount: Union[Unset, Currency]
        if isinstance(_promotion_amount, Unset):
            promotion_amount = UNSET
        else:
            promotion_amount = Currency.from_dict(_promotion_amount)

        result = cls(
            promotion_type=promotion_type,
            promotion_id=promotion_id,
            promotion_amount=promotion_amount,
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
