from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_status import OrderStatus
    from ..models.pagination import Pagination


T = TypeVar("T", bound="OrderListStatus")


@attr.s(auto_attribs=True)
class OrderListStatus:
    r"""
    Attributes:
        pagination (Union[Unset, Pagination]):
        orders_status (Union[Unset, List['OrderStatus']]):
    """

    pagination: Union[Unset, "Pagination"] = UNSET
    orders_status: Union[Unset, List["OrderStatus"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        orders_status: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orders_status, Unset):
            orders_status = []
            for orders_status_item_data in self.orders_status:
                orders_status_item = orders_status_item_data.to_dict()

                orders_status.append(orders_status_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if orders_status is not UNSET:
            field_dict["ordersStatus"] = orders_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_status import OrderStatus
        from ..models.pagination import Pagination

        d = src_dict.copy()
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        orders_status = []
        _orders_status = d.pop("ordersStatus", UNSET)
        for orders_status_item_data in _orders_status or []:
            orders_status_item = OrderStatus.from_dict(orders_status_item_data)

            orders_status.append(orders_status_item)

        result = cls(
            pagination=pagination,
            orders_status=orders_status,
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
