from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_item_approval_request import OrderItemApprovalRequest


T = TypeVar("T", bound="UpdateOrderApprovalsRequest")


@attr.s(auto_attribs=True)
class UpdateOrderApprovalsRequest:
    r"""The request body for the updateOrderItemsApprovals operation.

    Attributes:
        order_items_approval_requests (List['OrderItemApprovalRequest']): A list of item approval requests.
        approver (Union[Unset, str]): Person or system that triggers the approval actions on behalf of the actor.
    """

    order_items_approval_requests: List["OrderItemApprovalRequest"]
    approver: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_items_approval_requests = []
        for order_items_approval_requests_item_data in self.order_items_approval_requests:
            order_items_approval_requests_item = order_items_approval_requests_item_data.to_dict()

            order_items_approval_requests.append(order_items_approval_requests_item)

        approver = self.approver

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OrderItemsApprovalRequests": order_items_approval_requests,
            }
        )
        if approver is not UNSET:
            field_dict["Approver"] = approver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_item_approval_request import OrderItemApprovalRequest

        d = src_dict.copy()
        order_items_approval_requests = []
        _order_items_approval_requests = d.pop("OrderItemsApprovalRequests")
        for order_items_approval_requests_item_data in _order_items_approval_requests:
            order_items_approval_requests_item = OrderItemApprovalRequest.from_dict(
                order_items_approval_requests_item_data
            )

            order_items_approval_requests.append(order_items_approval_requests_item)

        approver = d.pop("Approver", UNSET)

        result = cls(
            order_items_approval_requests=order_items_approval_requests,
            approver=approver,
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
