from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.carrier_will_pick_up_option import CarrierWillPickUpOption
from ..models.delivery_experience_option import DeliveryExperienceOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShippingOfferingFilter")


@attr.s(auto_attribs=True)
class ShippingOfferingFilter:
    r"""Filter for use when requesting eligible shipping services.

    Attributes:
        include_packing_slip_with_label (Union[Unset, bool]): When true, include a packing slip with the label.
        include_complex_shipping_options (Union[Unset, bool]): When true, include complex shipping options.
        carrier_will_pick_up (Union[Unset, CarrierWillPickUpOption]): Carrier will pick up option.
        delivery_experience (Union[Unset, DeliveryExperienceOption]): The delivery confirmation level.
    """

    include_packing_slip_with_label: Union[Unset, bool] = UNSET
    include_complex_shipping_options: Union[Unset, bool] = UNSET
    carrier_will_pick_up: Union[Unset, CarrierWillPickUpOption] = UNSET
    delivery_experience: Union[Unset, DeliveryExperienceOption] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        include_packing_slip_with_label = self.include_packing_slip_with_label
        include_complex_shipping_options = self.include_complex_shipping_options
        carrier_will_pick_up: Union[Unset, str] = UNSET
        if not isinstance(self.carrier_will_pick_up, Unset):
            carrier_will_pick_up = self.carrier_will_pick_up.value

        delivery_experience: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_experience, Unset):
            delivery_experience = self.delivery_experience.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_packing_slip_with_label is not UNSET:
            field_dict["IncludePackingSlipWithLabel"] = include_packing_slip_with_label
        if include_complex_shipping_options is not UNSET:
            field_dict["IncludeComplexShippingOptions"] = include_complex_shipping_options
        if carrier_will_pick_up is not UNSET:
            field_dict["CarrierWillPickUp"] = carrier_will_pick_up
        if delivery_experience is not UNSET:
            field_dict["DeliveryExperience"] = delivery_experience

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        include_packing_slip_with_label = d.pop("IncludePackingSlipWithLabel", UNSET)

        include_complex_shipping_options = d.pop("IncludeComplexShippingOptions", UNSET)

        _carrier_will_pick_up = d.pop("CarrierWillPickUp", UNSET)
        carrier_will_pick_up: Union[Unset, CarrierWillPickUpOption]
        if isinstance(_carrier_will_pick_up, Unset):
            carrier_will_pick_up = UNSET
        else:
            carrier_will_pick_up = CarrierWillPickUpOption(_carrier_will_pick_up)

        _delivery_experience = d.pop("DeliveryExperience", UNSET)
        delivery_experience: Union[Unset, DeliveryExperienceOption]
        if isinstance(_delivery_experience, Unset):
            delivery_experience = UNSET
        else:
            delivery_experience = DeliveryExperienceOption(_delivery_experience)

        result = cls(
            include_packing_slip_with_label=include_packing_slip_with_label,
            include_complex_shipping_options=include_complex_shipping_options,
            carrier_will_pick_up=carrier_will_pick_up,
            delivery_experience=delivery_experience,
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
