from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="OrderMetricsInterval")


@attr.s(auto_attribs=True)
class OrderMetricsInterval:
    r"""Contains order metrics.

    Attributes:
        interval (str): The interval of time based on requested granularity (ex. Hour, Day, etc.) If this is the first
            or the last interval from the list, it might contain incomplete data if the requested interval doesn't align
            with the requested granularity (ex. request interval 2018-09-01T02:00:00Z--2018-09-04T19:00:00Z and granularity
            day will result in Sept 1st UTC day and Sept 4th UTC days having partial data).
        unit_count (int): The number of units in orders based on the specified filters.
        order_item_count (int): The number of order items based on the specified filters.
        order_count (int): The number of orders based on the specified filters.
        average_unit_price (Money): The currency type and the amount.
        total_sales (Money): The currency type and the amount.
    """

    interval: str
    unit_count: int
    order_item_count: int
    order_count: int
    average_unit_price: "Money"
    total_sales: "Money"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interval = self.interval
        unit_count = self.unit_count
        order_item_count = self.order_item_count
        order_count = self.order_count
        average_unit_price = self.average_unit_price.to_dict()

        total_sales = self.total_sales.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval": interval,
                "unitCount": unit_count,
                "orderItemCount": order_item_count,
                "orderCount": order_count,
                "averageUnitPrice": average_unit_price,
                "totalSales": total_sales,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        interval = d.pop("interval")

        unit_count = d.pop("unitCount")

        order_item_count = d.pop("orderItemCount")

        order_count = d.pop("orderCount")

        average_unit_price = Money.from_dict(d.pop("averageUnitPrice"))

        total_sales = Money.from_dict(d.pop("totalSales"))

        result = cls(
            interval=interval,
            unit_count=unit_count,
            order_item_count=order_item_count,
            order_count=order_count,
            average_unit_price=average_unit_price,
            total_sales=total_sales,
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
