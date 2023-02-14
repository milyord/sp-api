from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.carrier_will_pick_up_option import CarrierWillPickUpOption

if TYPE_CHECKING:
    from ..models.currency_amount import CurrencyAmount


T = TypeVar("T", bound="AvailableCarrierWillPickUpOption")


@attr.s(auto_attribs=True)
class AvailableCarrierWillPickUpOption:
    r"""Indicates whether the carrier will pick up the package, and what fee is charged, if any.

    Attributes:
        carrier_will_pick_up_option (CarrierWillPickUpOption): Carrier will pick up option.
        charge (CurrencyAmount): Currency type and amount.
    """

    carrier_will_pick_up_option: CarrierWillPickUpOption
    charge: "CurrencyAmount"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carrier_will_pick_up_option = self.carrier_will_pick_up_option.value

        charge = self.charge.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CarrierWillPickUpOption": carrier_will_pick_up_option,
                "Charge": charge,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency_amount import CurrencyAmount

        d = src_dict.copy()
        carrier_will_pick_up_option = CarrierWillPickUpOption(d.pop("CarrierWillPickUpOption"))

        charge = CurrencyAmount.from_dict(d.pop("Charge"))

        result = cls(
            carrier_will_pick_up_option=carrier_will_pick_up_option,
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
