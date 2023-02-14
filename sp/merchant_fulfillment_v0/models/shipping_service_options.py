from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.carrier_will_pick_up_option import CarrierWillPickUpOption
from ..models.delivery_experience_type import DeliveryExperienceType
from ..models.label_format import LabelFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_amount import CurrencyAmount


T = TypeVar("T", bound="ShippingServiceOptions")


@attr.s(auto_attribs=True)
class ShippingServiceOptions:
    r"""Extra services provided by a carrier.

    Attributes:
        delivery_experience (DeliveryExperienceType): The delivery confirmation level.
        carrier_will_pick_up (bool): When true, the carrier will pick up the package.

            Note: Scheduled carrier pickup is available only using Dynamex (US), DPD (UK), and Royal Mail (UK).
        declared_value (Union[Unset, CurrencyAmount]): Currency type and amount.
        carrier_will_pick_up_option (Union[Unset, CarrierWillPickUpOption]): Carrier will pick up option.
        label_format (Union[Unset, LabelFormat]): The label format.
    """

    delivery_experience: DeliveryExperienceType
    carrier_will_pick_up: bool
    declared_value: Union[Unset, "CurrencyAmount"] = UNSET
    carrier_will_pick_up_option: Union[Unset, CarrierWillPickUpOption] = UNSET
    label_format: Union[Unset, LabelFormat] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivery_experience = self.delivery_experience.value

        carrier_will_pick_up = self.carrier_will_pick_up
        declared_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.declared_value, Unset):
            declared_value = self.declared_value.to_dict()

        carrier_will_pick_up_option: Union[Unset, str] = UNSET
        if not isinstance(self.carrier_will_pick_up_option, Unset):
            carrier_will_pick_up_option = self.carrier_will_pick_up_option.value

        label_format: Union[Unset, str] = UNSET
        if not isinstance(self.label_format, Unset):
            label_format = self.label_format.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DeliveryExperience": delivery_experience,
                "CarrierWillPickUp": carrier_will_pick_up,
            }
        )
        if declared_value is not UNSET:
            field_dict["DeclaredValue"] = declared_value
        if carrier_will_pick_up_option is not UNSET:
            field_dict["CarrierWillPickUpOption"] = carrier_will_pick_up_option
        if label_format is not UNSET:
            field_dict["LabelFormat"] = label_format

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency_amount import CurrencyAmount

        d = src_dict.copy()
        delivery_experience = DeliveryExperienceType(d.pop("DeliveryExperience"))

        carrier_will_pick_up = d.pop("CarrierWillPickUp")

        _declared_value = d.pop("DeclaredValue", UNSET)
        declared_value: Union[Unset, CurrencyAmount]
        if isinstance(_declared_value, Unset):
            declared_value = UNSET
        else:
            declared_value = CurrencyAmount.from_dict(_declared_value)

        _carrier_will_pick_up_option = d.pop("CarrierWillPickUpOption", UNSET)
        carrier_will_pick_up_option: Union[Unset, CarrierWillPickUpOption]
        if isinstance(_carrier_will_pick_up_option, Unset):
            carrier_will_pick_up_option = UNSET
        else:
            carrier_will_pick_up_option = CarrierWillPickUpOption(_carrier_will_pick_up_option)

        _label_format = d.pop("LabelFormat", UNSET)
        label_format: Union[Unset, LabelFormat]
        if isinstance(_label_format, Unset):
            label_format = UNSET
        else:
            label_format = LabelFormat(_label_format)

        result = cls(
            delivery_experience=delivery_experience,
            carrier_will_pick_up=carrier_will_pick_up,
            declared_value=declared_value,
            carrier_will_pick_up_option=carrier_will_pick_up_option,
            label_format=label_format,
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
