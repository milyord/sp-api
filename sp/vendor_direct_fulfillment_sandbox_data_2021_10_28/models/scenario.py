from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.test_order import TestOrder


T = TypeVar("T", bound="Scenario")


@attr.s(auto_attribs=True)
class Scenario:
    r"""A scenario test case response returned when the request is successful.

    Attributes:
        scenario_id (str): An identifier that identifies the type of scenario that user can use for testing.
        orders (List['TestOrder']): A list of orders that can be used by the caller to test each life cycle or scenario.
    """

    scenario_id: str
    orders: List["TestOrder"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scenario_id = self.scenario_id
        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()

            orders.append(orders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scenarioId": scenario_id,
                "orders": orders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.test_order import TestOrder

        d = src_dict.copy()
        scenario_id = d.pop("scenarioId")

        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = TestOrder.from_dict(orders_item_data)

            orders.append(orders_item)

        result = cls(
            scenario_id=scenario_id,
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
