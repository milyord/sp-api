from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.delivery_window import DeliveryWindow


T = TypeVar("T", bound="ScheduledDeliveryInfo")


@attr.s(auto_attribs=True)
class ScheduledDeliveryInfo:
    r"""Delivery information for a scheduled delivery.

    Attributes:
        delivery_time_zone (str): The time zone of the destination address for the fulfillment order preview. Must be an
            IANA time zone name. Example: Asia/Tokyo.
        delivery_windows (List['DeliveryWindow']): An array of delivery windows.
    """

    delivery_time_zone: str
    delivery_windows: List["DeliveryWindow"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivery_time_zone = self.delivery_time_zone
        delivery_windows = []
        for componentsschemas_delivery_window_list_item_data in self.delivery_windows:
            componentsschemas_delivery_window_list_item = componentsschemas_delivery_window_list_item_data.to_dict()

            delivery_windows.append(componentsschemas_delivery_window_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deliveryTimeZone": delivery_time_zone,
                "deliveryWindows": delivery_windows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_window import DeliveryWindow

        d = src_dict.copy()
        delivery_time_zone = d.pop("deliveryTimeZone")

        delivery_windows = []
        _delivery_windows = d.pop("deliveryWindows")
        for componentsschemas_delivery_window_list_item_data in _delivery_windows:
            componentsschemas_delivery_window_list_item = DeliveryWindow.from_dict(
                componentsschemas_delivery_window_list_item_data
            )

            delivery_windows.append(componentsschemas_delivery_window_list_item)

        result = cls(
            delivery_time_zone=delivery_time_zone,
            delivery_windows=delivery_windows,
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
