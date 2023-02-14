from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_update import InventoryUpdate


T = TypeVar("T", bound="SubmitInventoryUpdateRequest")


@attr.s(auto_attribs=True)
class SubmitInventoryUpdateRequest:
    r"""The request body for the submitInventoryUpdate operation.

    Attributes:
        inventory (Union[Unset, InventoryUpdate]):
    """

    inventory: Union[Unset, "InventoryUpdate"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inventory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = self.inventory.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory is not UNSET:
            field_dict["inventory"] = inventory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inventory_update import InventoryUpdate

        d = src_dict.copy()
        _inventory = d.pop("inventory", UNSET)
        inventory: Union[Unset, InventoryUpdate]
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = InventoryUpdate.from_dict(_inventory)

        result = cls(
            inventory=inventory,
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
