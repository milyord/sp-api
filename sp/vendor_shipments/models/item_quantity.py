from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_quantity_unit_of_measure import ItemQuantityUnitOfMeasure
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemQuantity")


@attr.s(auto_attribs=True)
class ItemQuantity:
    r"""Details of item quantity.

    Attributes:
        amount (int): Amount of units shipped for a specific item at a shipment level. If the item is present only in
            certain cartons or pallets within the shipment, please provide this at the appropriate carton or pallet level.
        unit_of_measure (ItemQuantityUnitOfMeasure): Unit of measure for the shipped quantity.
        unit_size (Union[Unset, int]): The case size, in the event that we ordered using cases. Otherwise, 1.
    """

    amount: int
    unit_of_measure: ItemQuantityUnitOfMeasure
    unit_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        unit_of_measure = self.unit_of_measure.value

        unit_size = self.unit_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "unitOfMeasure": unit_of_measure,
            }
        )
        if unit_size is not UNSET:
            field_dict["unitSize"] = unit_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount")

        unit_of_measure = ItemQuantityUnitOfMeasure(d.pop("unitOfMeasure"))

        unit_size = d.pop("unitSize", UNSET)

        result = cls(
            amount=amount,
            unit_of_measure=unit_of_measure,
            unit_size=unit_size,
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
