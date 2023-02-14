from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.item_approval_action import ItemApprovalAction


T = TypeVar("T", bound="OrderItemApprovalRequest")


@attr.s(auto_attribs=True)
class OrderItemApprovalRequest:
    r"""Order item apecific approval request.

    Attributes:
        order_item_id (str): The unique identifier of the order item.
        approval_action (ItemApprovalAction): This object represents an approval action used by the actors in the order
            item approval process. Check the applicable restrictions at the specific approval type schemas.
    """

    order_item_id: str
    approval_action: "ItemApprovalAction"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_item_id = self.order_item_id
        approval_action = self.approval_action.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OrderItemId": order_item_id,
                "ApprovalAction": approval_action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_approval_action import ItemApprovalAction

        d = src_dict.copy()
        order_item_id = d.pop("OrderItemId")

        approval_action = ItemApprovalAction.from_dict(d.pop("ApprovalAction"))

        result = cls(
            order_item_id=order_item_id,
            approval_action=approval_action,
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
