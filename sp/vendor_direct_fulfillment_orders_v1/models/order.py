from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_details import OrderDetails


T = TypeVar("T", bound="Order")


@attr.s(auto_attribs=True)
class Order:
    r"""
    Attributes:
        purchase_order_number (str): The purchase order number for this order. Formatting Notes: alpha-numeric code.
        order_details (Union[Unset, OrderDetails]): Details of an order.
    """

    purchase_order_number: str
    order_details: Union[Unset, "OrderDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        order_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_details, Unset):
            order_details = self.order_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderNumber": purchase_order_number,
            }
        )
        if order_details is not UNSET:
            field_dict["orderDetails"] = order_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_details import OrderDetails

        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        _order_details = d.pop("orderDetails", UNSET)
        order_details: Union[Unset, OrderDetails]
        if isinstance(_order_details, Unset):
            order_details = UNSET
        else:
            order_details = OrderDetails.from_dict(_order_details)

        result = cls(
            purchase_order_number=purchase_order_number,
            order_details=order_details,
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
