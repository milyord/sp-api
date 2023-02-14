from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_capacity import RangeCapacity


T = TypeVar("T", bound="RangeSlotCapacity")


@attr.s(auto_attribs=True)
class RangeSlotCapacity:
    r"""Response schema for the `getRangeSlotCapacity` operation.

    Attributes:
        resource_id (Union[Unset, str]): Resource Identifier.
        capacities (Union[Unset, List['RangeCapacity']]): Array of range capacities where each entry is for a specific
            capacity type.
        next_page_token (Union[Unset, str]): Next page token, if there are more pages.
    """

    resource_id: Union[Unset, str] = UNSET
    capacities: Union[Unset, List["RangeCapacity"]] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_id = self.resource_id
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
        if capacities is not UNSET:
            field_dict["capacities"] = capacities
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.range_capacity import RangeCapacity

        d = src_dict.copy()
        resource_id = d.pop("resourceId", UNSET)

        capacities = []
        _capacities = d.pop("capacities", UNSET)
        for capacities_item_data in _capacities or []:
            capacities_item = RangeCapacity.from_dict(capacities_item_data)

            capacities.append(capacities_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        result = cls(
            resource_id=resource_id,
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
