from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="PaymentExecutionDetailItem")


@attr.s(auto_attribs=True)
class PaymentExecutionDetailItem:
    r"""Information about a sub-payment method used to pay for a COD order.

    Attributes:
        payment (Money): The monetary value of the order.
        payment_method (str): A sub-payment method for a COD order.

            Possible values:

            * COD - Cash On Delivery.

            * GC - Gift Card.

            * PointsAccount - Amazon Points.
    """

    payment: "Money"
    payment_method: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment = self.payment.to_dict()

        payment_method = self.payment_method

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Payment": payment,
                "PaymentMethod": payment_method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        payment = Money.from_dict(d.pop("Payment"))

        payment_method = d.pop("PaymentMethod")

        result = cls(
            payment=payment,
            payment_method=payment_method,
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
