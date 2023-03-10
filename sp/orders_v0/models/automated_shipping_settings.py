from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomatedShippingSettings")


@attr.s(auto_attribs=True)
class AutomatedShippingSettings:
    r"""Contains information regarding the Shipping Settings Automation program, such as whether the order's shipping
    settings were generated automatically, and what those settings are.

        Attributes:
            has_automated_shipping_settings (Union[Unset, bool]): When true, this order has automated shipping settings
                generated by Amazon. This order could be identified as an SSA order.
            automated_carrier (Union[Unset, str]): Auto-generated carrier for SSA orders.
            automated_ship_method (Union[Unset, str]): Auto-generated ship method for SSA orders.
    """

    has_automated_shipping_settings: Union[Unset, bool] = UNSET
    automated_carrier: Union[Unset, str] = UNSET
    automated_ship_method: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_automated_shipping_settings = self.has_automated_shipping_settings
        automated_carrier = self.automated_carrier
        automated_ship_method = self.automated_ship_method

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_automated_shipping_settings is not UNSET:
            field_dict["HasAutomatedShippingSettings"] = has_automated_shipping_settings
        if automated_carrier is not UNSET:
            field_dict["AutomatedCarrier"] = automated_carrier
        if automated_ship_method is not UNSET:
            field_dict["AutomatedShipMethod"] = automated_ship_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        has_automated_shipping_settings = d.pop("HasAutomatedShippingSettings", UNSET)

        automated_carrier = d.pop("AutomatedCarrier", UNSET)

        automated_ship_method = d.pop("AutomatedShipMethod", UNSET)

        result = cls(
            has_automated_shipping_settings=has_automated_shipping_settings,
            automated_carrier=automated_carrier,
            automated_ship_method=automated_ship_method,
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
