from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="FeeComponent")


@attr.s(auto_attribs=True)
class FeeComponent:
    r"""A fee associated with the event.

    Attributes:
        fee_type (Union[Unset, str]): The type of fee. For more information about Selling on Amazon fees, see [Selling
            on Amazon Fee Schedule](https://sellercentral.amazon.com/gp/help/200336920) on Seller Central. For more
            information about Fulfillment by Amazon fees, see [FBA features, services and
            fees](https://sellercentral.amazon.com/gp/help/201074400) on Seller Central.
        fee_amount (Union[Unset, Currency]): A currency type and amount.
    """

    fee_type: Union[Unset, str] = UNSET
    fee_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fee_type = self.fee_type
        fee_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fee_amount, Unset):
            fee_amount = self.fee_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_type is not UNSET:
            field_dict["FeeType"] = fee_type
        if fee_amount is not UNSET:
            field_dict["FeeAmount"] = fee_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        fee_type = d.pop("FeeType", UNSET)

        _fee_amount = d.pop("FeeAmount", UNSET)
        fee_amount: Union[Unset, Currency]
        if isinstance(_fee_amount, Unset):
            fee_amount = UNSET
        else:
            fee_amount = Currency.from_dict(_fee_amount)

        result = cls(
            fee_type=fee_type,
            fee_amount=fee_amount,
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
