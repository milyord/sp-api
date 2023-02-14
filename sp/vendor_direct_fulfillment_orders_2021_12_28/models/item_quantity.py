from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_quantity_unit_of_measure import ItemQuantityUnitOfMeasure
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemQuantity")


@attr.s(auto_attribs=True)
class ItemQuantity:
    r"""Details of quantity ordered.

    Attributes:
        amount (Union[Unset, int]): Acknowledged quantity. This value should not be zero.
        unit_of_measure (Union[Unset, ItemQuantityUnitOfMeasure]): Unit of measure for the acknowledged quantity.
    """

    amount: Union[Unset, int] = UNSET
    unit_of_measure: Union[Unset, ItemQuantityUnitOfMeasure] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        unit_of_measure: Union[Unset, str] = UNSET
        if not isinstance(self.unit_of_measure, Unset):
            unit_of_measure = self.unit_of_measure.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        _unit_of_measure = d.pop("unitOfMeasure", UNSET)
        unit_of_measure: Union[Unset, ItemQuantityUnitOfMeasure]
        if isinstance(_unit_of_measure, Unset):
            unit_of_measure = UNSET
        else:
            unit_of_measure = ItemQuantityUnitOfMeasure(_unit_of_measure)

        result = cls(
            amount=amount,
            unit_of_measure=unit_of_measure,
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
