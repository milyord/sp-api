from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.item_approval_status import ItemApprovalStatus
from ..models.item_approval_type import ItemApprovalType

if TYPE_CHECKING:
    from ..models.item_approval import ItemApproval


T = TypeVar("T", bound="OrderItemApprovals")


@attr.s(auto_attribs=True)
class OrderItemApprovals:
    r"""List of item approvals gathered during the approval process.

    Attributes:
        order_item_id (str): The unique identifier of the order item.
        approval_type (ItemApprovalType): Defines the approval process types available for order items.
        approval_status (ItemApprovalStatus): Defines the possible status of an order item approval.
        item_approvals (List['ItemApproval']):
    """

    order_item_id: str
    approval_type: ItemApprovalType
    approval_status: ItemApprovalStatus
    item_approvals: List["ItemApproval"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_item_id = self.order_item_id
        approval_type = self.approval_type.value

        approval_status = self.approval_status.value

        item_approvals = []
        for item_approvals_item_data in self.item_approvals:
            item_approvals_item = item_approvals_item_data.to_dict()

            item_approvals.append(item_approvals_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OrderItemId": order_item_id,
                "ApprovalType": approval_type,
                "ApprovalStatus": approval_status,
                "ItemApprovals": item_approvals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_approval import ItemApproval

        d = src_dict.copy()
        order_item_id = d.pop("OrderItemId")

        approval_type = ItemApprovalType(d.pop("ApprovalType"))

        approval_status = ItemApprovalStatus(d.pop("ApprovalStatus"))

        item_approvals = []
        _item_approvals = d.pop("ItemApprovals")
        for item_approvals_item_data in _item_approvals:
            item_approvals_item = ItemApproval.from_dict(item_approvals_item_data)

            item_approvals.append(item_approvals_item)

        result = cls(
            order_item_id=order_item_id,
            approval_type=approval_type,
            approval_status=approval_status,
            item_approvals=item_approvals,
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
