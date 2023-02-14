from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fixed_slot import FixedSlot


T = TypeVar("T", bound="FixedSlotCapacity")


@attr.s(auto_attribs=True)
class FixedSlotCapacity:
    r"""Response schema for the `getFixedSlotCapacity` operation.

    Attributes:
        resource_id (Union[Unset, str]): Resource Identifier.
        slot_duration (Union[Unset, float]): The duration of each slot which is returned. This value will be a multiple
            of 5 and fall in the following range: 5 <= `slotDuration` <= 360.
        capacities (Union[Unset, List['FixedSlot']]): Array of capacity slots in fixed slot format.
        next_page_token (Union[Unset, str]): Next page token, if there are more pages.
    """

    resource_id: Union[Unset, str] = UNSET
    slot_duration: Union[Unset, float] = UNSET
    capacities: Union[Unset, List["FixedSlot"]] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_id = self.resource_id
        slot_duration = self.slot_duration
        capacities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.capacities, Unset):
            capacities = []
            for capacities_item_data in self.capacities:
                capacities_item = capacities_item_data.to_dict()

                capacities.append(capacities_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if slot_duration is not UNSET:
            field_dict["slotDuration"] = slot_duration
        if capacities is not UNSET:
            field_dict["capacities"] = capacities
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fixed_slot import FixedSlot

        d = src_dict.copy()
        resource_id = d.pop("resourceId", UNSET)

        slot_duration = d.pop("slotDuration", UNSET)

        capacities = []
        _capacities = d.pop("capacities", UNSET)
        for capacities_item_data in _capacities or []:
            capacities_item = FixedSlot.from_dict(capacities_item_data)

            capacities.append(capacities_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        result = cls(
            resource_id=resource_id,
            slot_duration=slot_duration,
            capacities=capacities,
            next_page_token=next_page_token,
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
