from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_approval_actor import ItemApprovalActor
from ..models.item_approval_approval_action_process_status import ItemApprovalApprovalActionProcessStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_approval_action import ItemApprovalAction


T = TypeVar("T", bound="ItemApproval")


@attr.s(auto_attribs=True)
class ItemApproval:
    r"""Generic item approval. Check the applicable restrictions at the specific approval type schemas.

    Attributes:
        sequence_id (int): Sequence number of the item approval. Each ItemApproval gets its sequenceId automatically
            from a monotonic increasing function.
        timestamp (str): Timestamp when the ItemApproval was recorded by Amazon's internal order approvals system. In
            ISO 8601 date time format.
        actor (ItemApprovalActor): High level actors involved in the approval process.
        approval_action (ItemApprovalAction): This object represents an approval action used by the actors in the order
            item approval process. Check the applicable restrictions at the specific approval type schemas.
        approval_action_process_status (ItemApprovalApprovalActionProcessStatus): Status of approval action.
        approver (Union[Unset, str]): Person or system that triggers the approval actions on behalf of the actor.
        approval_action_process_status_message (Union[Unset, str]): Optional message to communicate optional additional
            context about the current status of the approval action.
    """

    sequence_id: int
    timestamp: str
    actor: ItemApprovalActor
    approval_action: "ItemApprovalAction"
    approval_action_process_status: ItemApprovalApprovalActionProcessStatus
    approver: Union[Unset, str] = UNSET
    approval_action_process_status_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sequence_id = self.sequence_id
        timestamp = self.timestamp
        actor = self.actor.value

        approval_action = self.approval_action.to_dict()

        approval_action_process_status = self.approval_action_process_status.value

        approver = self.approver
        approval_action_process_status_message = self.approval_action_process_status_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SequenceId": sequence_id,
                "Timestamp": timestamp,
                "Actor": actor,
                "ApprovalAction": approval_action,
                "ApprovalActionProcessStatus": approval_action_process_status,
            }
        )
        if approver is not UNSET:
            field_dict["Approver"] = approver
        if approval_action_process_status_message is not UNSET:
            field_dict["ApprovalActionProcessStatusMessage"] = approval_action_process_status_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_approval_action import ItemApprovalAction

        d = src_dict.copy()
        sequence_id = d.pop("SequenceId")

        timestamp = d.pop("Timestamp")

        actor = ItemApprovalActor(d.pop("Actor"))

        approval_action = ItemApprovalAction.from_dict(d.pop("ApprovalAction"))

        approval_action_process_status = ItemApprovalApprovalActionProcessStatus(d.pop("ApprovalActionProcessStatus"))

        approver = d.pop("Approver", UNSET)

        approval_action_process_status_message = d.pop("ApprovalActionProcessStatusMessage", UNSET)

        result = cls(
            sequence_id=sequence_id,
            timestamp=timestamp,
            actor=actor,
            approval_action=approval_action,
            approval_action_process_status=approval_action_process_status,
            approver=approver,
            approval_action_process_status_message=approval_action_process_status_message,
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
