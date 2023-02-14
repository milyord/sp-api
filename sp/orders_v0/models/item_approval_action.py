from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_approval_action_action_type import ItemApprovalActionActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_approval_action_changes import ItemApprovalActionChanges


T = TypeVar("T", bound="ItemApprovalAction")


@attr.s(auto_attribs=True)
class ItemApprovalAction:
    r"""This object represents an approval action used by the actors in the order item approval process. Check the
    applicable restrictions at the specific approval type schemas.

        Attributes:
            action_type (ItemApprovalActionActionType): Defines the type of action for the approval.
            comment (Union[Unset, str]): Comment message to provide optional additional context on the approval action.
            changes (Union[Unset, ItemApprovalActionChanges]): Changes required for the approval. Each approval type defines
                the allowed changes valid sub-set in its specific schema.
    """

    action_type: ItemApprovalActionActionType
    comment: Union[Unset, str] = UNSET
    changes: Union[Unset, "ItemApprovalActionChanges"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action_type = self.action_type.value

        comment = self.comment
        changes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ActionType": action_type,
            }
        )
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if changes is not UNSET:
            field_dict["Changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_approval_action_changes import ItemApprovalActionChanges

        d = src_dict.copy()
        action_type = ItemApprovalActionActionType(d.pop("ActionType"))

        comment = d.pop("Comment", UNSET)

        _changes = d.pop("Changes", UNSET)
        changes: Union[Unset, ItemApprovalActionChanges]
        if isinstance(_changes, Unset):
            changes = UNSET
        else:
            changes = ItemApprovalActionChanges.from_dict(_changes)

        result = cls(
            action_type=action_type,
            comment=comment,
            changes=changes,
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
