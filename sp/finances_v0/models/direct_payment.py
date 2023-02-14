from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="DirectPayment")


@attr.s(auto_attribs=True)
class DirectPayment:
    r"""A payment made directly to a seller.

    Attributes:
        direct_payment_type (Union[Unset, str]): The type of payment.

            Possible values:

            * StoredValueCardRevenue - The amount that is deducted from the seller's account because the seller received
            money through a stored value card.

            * StoredValueCardRefund - The amount that Amazon returns to the seller if the order that is bought using a
            stored value card is refunded.

            * PrivateLabelCreditCardRevenue - The amount that is deducted from the seller's account because the seller
            received money through a private label credit card offered by Amazon.

            * PrivateLabelCreditCardRefund - The amount that Amazon returns to the seller if the order that is bought using
            a private label credit card offered by Amazon is refunded.

            * CollectOnDeliveryRevenue - The COD amount that the seller collected directly from the buyer.

            * CollectOnDeliveryRefund - The amount that Amazon refunds to the buyer if an order paid for by COD is refunded.
        direct_payment_amount (Union[Unset, Currency]): A currency type and amount.
    """

    direct_payment_type: Union[Unset, str] = UNSET
    direct_payment_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        direct_payment_type = self.direct_payment_type
        direct_payment_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.direct_payment_amount, Unset):
            direct_payment_amount = self.direct_payment_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direct_payment_type is not UNSET:
            field_dict["DirectPaymentType"] = direct_payment_type
        if direct_payment_amount is not UNSET:
            field_dict["DirectPaymentAmount"] = direct_payment_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        direct_payment_type = d.pop("DirectPaymentType", UNSET)

        _direct_payment_amount = d.pop("DirectPaymentAmount", UNSET)
        direct_payment_amount: Union[Unset, Currency]
        if isinstance(_direct_payment_amount, Unset):
            direct_payment_amount = UNSET
        else:
            direct_payment_amount = Currency.from_dict(_direct_payment_amount)

        result = cls(
            direct_payment_type=direct_payment_type,
            direct_payment_amount=direct_payment_amount,
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
