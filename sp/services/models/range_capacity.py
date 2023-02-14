from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.capacity_type import CapacityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_slot import RangeSlot


T = TypeVar("T", bound="RangeCapacity")


@attr.s(auto_attribs=True)
class RangeCapacity:
    r"""Range capacity entity where each entry has a capacity type and corresponding slots.

    Attributes:
        capacity_type (Union[Unset, CapacityType]): Type of capacity
        slots (Union[Unset, List['RangeSlot']]): Array of capacity slots in range slot format.
    """

    capacity_type: Union[Unset, CapacityType] = UNSET
    slots: Union[Unset, List["RangeSlot"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        capacity_type: Union[Unset, str] = UNSET
        if not isinstance(self.capacity_type, Unset):
            capacity_type = self.capacity_type.value

        slots: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.slots, Unset):
            slots = []
            for slots_item_data in self.slots:
                slots_item = slots_item_data.to_dict()

                slots.append(slots_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capacity_type is not UNSET:
            field_dict["capacityType"] = capacity_type
        if slots is not UNSET:
            field_dict["slots"] = slots

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.range_slot import RangeSlot

        d = src_dict.copy()
        _capacity_type = d.pop("capacityType", UNSET)
        capacity_type: Union[Unset, CapacityType]
        if isinstance(_capacity_type, Unset):
            capacity_type = UNSET
        else:
            capacity_type = CapacityType(_capacity_type)

        slots = []
        _slots = d.pop("slots", UNSET)
        for slots_item_data in _slots or []:
            slots_item = RangeSlot.from_dict(slots_item_data)

            slots.append(slots_item)

        result = cls(
            capacity_type=capacity_type,
            slots=slots,
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
