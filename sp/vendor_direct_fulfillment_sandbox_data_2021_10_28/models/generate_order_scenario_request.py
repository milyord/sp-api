from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_scenario_request import OrderScenarioRequest


T = TypeVar("T", bound="GenerateOrderScenarioRequest")


@attr.s(auto_attribs=True)
class GenerateOrderScenarioRequest:
    r"""The request body for the generateOrderScenarios operation.

    Attributes:
        orders (Union[Unset, List['OrderScenarioRequest']]): The list of test orders requested as indicated by party
            identifiers.
    """

    orders: Union[Unset, List["OrderScenarioRequest"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()

                orders.append(orders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_scenario_request import OrderScenarioRequest

        d = src_dict.copy()
        orders = []
        _orders = d.pop("orders", UNSET)
        for orders_item_data in _orders or []:
            orders_item = OrderScenarioRequest.from_dict(orders_item_data)

            orders.append(orders_item)

        result = cls(
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
