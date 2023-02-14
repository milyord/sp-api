from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.delivery_experience_option import DeliveryExperienceOption

if TYPE_CHECKING:
    from ..models.currency_amount import CurrencyAmount


T = TypeVar("T", bound="AvailableDeliveryExperienceOption")


@attr.s(auto_attribs=True)
class AvailableDeliveryExperienceOption:
    r"""The available delivery confirmation options, and the fee charged, if any.

    Attributes:
        delivery_experience_option (DeliveryExperienceOption): The delivery confirmation level.
        charge (CurrencyAmount): Currency type and amount.
    """

    delivery_experience_option: DeliveryExperienceOption
    charge: "CurrencyAmount"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivery_experience_option = self.delivery_experience_option.value

        charge = self.charge.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DeliveryExperienceOption": delivery_experience_option,
                "Charge": charge,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency_amount import CurrencyAmount

        d = src_dict.copy()
        delivery_experience_option = DeliveryExperienceOption(d.pop("DeliveryExperienceOption"))

        charge = CurrencyAmount.from_dict(d.pop("Charge"))

        result = cls(
            delivery_experience_option=delivery_experience_option,
            charge=charge,
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
