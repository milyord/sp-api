from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order import Order
    from ..models.pagination import Pagination


T = TypeVar("T", bound="OrderList")


@attr.s(auto_attribs=True)
class OrderList:
    r"""
    Attributes:
        pagination (Union[Unset, Pagination]):
        orders (Union[Unset, List['Order']]):
    """

    pagination: Union[Unset, "Pagination"] = UNSET
    orders: Union[Unset, List["Order"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()

                orders.append(orders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order import Order
        from ..models.pagination import Pagination

        d = src_dict.copy()
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        orders = []
        _orders = d.pop("orders", UNSET)
        for orders_item_data in _orders or []:
            orders_item = Order.from_dict(orders_item_data)

            orders.append(orders_item)

        result = cls(
            pagination=pagination,
            orders=orders,
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
