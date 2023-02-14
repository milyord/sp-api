from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fulfillment_order import FulfillmentOrder


T = TypeVar("T", bound="ListAllFulfillmentOrdersResult")


@attr.s(auto_attribs=True)
class ListAllFulfillmentOrdersResult:
    r"""
    Attributes:
        next_token (Union[Unset, str]): When present and not empty, pass this string token in the next request to return
            the next response page.
        fulfillment_orders (Union[Unset, List['FulfillmentOrder']]): An array of fulfillment order information.
    """

    next_token: Union[Unset, str] = UNSET
    fulfillment_orders: Union[Unset, List["FulfillmentOrder"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_token = self.next_token
        fulfillment_orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulfillment_orders, Unset):
            fulfillment_orders = []
            for fulfillment_orders_item_data in self.fulfillment_orders:
                fulfillment_orders_item = fulfillment_orders_item_data.to_dict()

                fulfillment_orders.append(fulfillment_orders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token
        if fulfillment_orders is not UNSET:
            field_dict["fulfillmentOrders"] = fulfillment_orders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fulfillment_order import FulfillmentOrder

        d = src_dict.copy()
        next_token = d.pop("nextToken", UNSET)

        fulfillment_orders = []
        _fulfillment_orders = d.pop("fulfillmentOrders", UNSET)
        for fulfillment_orders_item_data in _fulfillment_orders or []:
            fulfillment_orders_item = FulfillmentOrder.from_dict(fulfillment_orders_item_data)

            fulfillment_orders.append(fulfillment_orders_item)

        result = cls(
            next_token=next_token,
            fulfillment_orders=fulfillment_orders,
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
