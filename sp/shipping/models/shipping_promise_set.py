from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="ShippingPromiseSet")


@attr.s(auto_attribs=True)
class ShippingPromiseSet:
    r"""The promised delivery time and pickup time.

    Attributes:
        delivery_window (Union[Unset, TimeRange]): The time range.
        receive_window (Union[Unset, TimeRange]): The time range.
    """

    delivery_window: Union[Unset, "TimeRange"] = UNSET
    receive_window: Union[Unset, "TimeRange"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivery_window: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_window, Unset):
            delivery_window = self.delivery_window.to_dict()

        receive_window: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.receive_window, Unset):
            receive_window = self.receive_window.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_window is not UNSET:
            field_dict["deliveryWindow"] = delivery_window
        if receive_window is not UNSET:
            field_dict["receiveWindow"] = receive_window

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.time_range import TimeRange

        d = src_dict.copy()
        _delivery_window = d.pop("deliveryWindow", UNSET)
        delivery_window: Union[Unset, TimeRange]
        if isinstance(_delivery_window, Unset):
            delivery_window = UNSET
        else:
            delivery_window = TimeRange.from_dict(_delivery_window)

        _receive_window = d.pop("receiveWindow", UNSET)
        receive_window: Union[Unset, TimeRange]
        if isinstance(_receive_window, Unset):
            receive_window = UNSET
        else:
            receive_window = TimeRange.from_dict(_receive_window)

        result = cls(
            delivery_window=delivery_window,
            receive_window=receive_window,
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
