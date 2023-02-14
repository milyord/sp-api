from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.available_carrier_will_pick_up_option import AvailableCarrierWillPickUpOption
    from ..models.available_delivery_experience_option import AvailableDeliveryExperienceOption


T = TypeVar("T", bound="AvailableShippingServiceOptions")


@attr.s(auto_attribs=True)
class AvailableShippingServiceOptions:
    r"""The available shipping service options.

    Attributes:
        available_carrier_will_pick_up_options (List['AvailableCarrierWillPickUpOption']): List of available carrier
            pickup options.
        available_delivery_experience_options (List['AvailableDeliveryExperienceOption']): List of available delivery
            experience options.
    """

    available_carrier_will_pick_up_options: List["AvailableCarrierWillPickUpOption"]
    available_delivery_experience_options: List["AvailableDeliveryExperienceOption"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_carrier_will_pick_up_options = []
        for (
            componentsschemas_available_carrier_will_pick_up_options_list_item_data
        ) in self.available_carrier_will_pick_up_options:
            componentsschemas_available_carrier_will_pick_up_options_list_item = (
                componentsschemas_available_carrier_will_pick_up_options_list_item_data.to_dict()
            )

            available_carrier_will_pick_up_options.append(
                componentsschemas_available_carrier_will_pick_up_options_list_item
            )

        available_delivery_experience_options = []
        for (
            componentsschemas_available_delivery_experience_options_list_item_data
        ) in self.available_delivery_experience_options:
            componentsschemas_available_delivery_experience_options_list_item = (
                componentsschemas_available_delivery_experience_options_list_item_data.to_dict()
            )

            available_delivery_experience_options.append(
                componentsschemas_available_delivery_experience_options_list_item
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AvailableCarrierWillPickUpOptions": available_carrier_will_pick_up_options,
                "AvailableDeliveryExperienceOptions": available_delivery_experience_options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.available_carrier_will_pick_up_option import AvailableCarrierWillPickUpOption
        from ..models.available_delivery_experience_option import AvailableDeliveryExperienceOption

        d = src_dict.copy()
        available_carrier_will_pick_up_options = []
        _available_carrier_will_pick_up_options = d.pop("AvailableCarrierWillPickUpOptions")
        for (
            componentsschemas_available_carrier_will_pick_up_options_list_item_data
        ) in _available_carrier_will_pick_up_options:
            componentsschemas_available_carrier_will_pick_up_options_list_item = (
                AvailableCarrierWillPickUpOption.from_dict(
                    componentsschemas_available_carrier_will_pick_up_options_list_item_data
                )
            )

            available_carrier_will_pick_up_options.append(
                componentsschemas_available_carrier_will_pick_up_options_list_item
            )

        available_delivery_experience_options = []
        _available_delivery_experience_options = d.pop("AvailableDeliveryExperienceOptions")
        for (
            componentsschemas_available_delivery_experience_options_list_item_data
        ) in _available_delivery_experience_options:
            componentsschemas_available_delivery_experience_options_list_item = (
                AvailableDeliveryExperienceOption.from_dict(
                    componentsschemas_available_delivery_experience_options_list_item_data
                )
            )

            available_delivery_experience_options.append(
                componentsschemas_available_delivery_experience_options_list_item
            )

        result = cls(
            available_carrier_will_pick_up_options=available_carrier_will_pick_up_options,
            available_delivery_experience_options=available_delivery_experience_options,
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
