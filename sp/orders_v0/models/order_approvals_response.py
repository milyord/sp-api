from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_item_approvals import OrderItemApprovals


T = TypeVar("T", bound="OrderApprovalsResponse")


@attr.s(auto_attribs=True)
class OrderApprovalsResponse:
    r"""The order items list with approvals along with the order ID.

    Attributes:
        order_items_approvals_list (List['OrderItemApprovals']): List of OrderItemApprovals.
        next_token (Union[Unset, str]): When present and not empty, pass this string token in the next request to return
            the next response page.
    """

    order_items_approvals_list: List["OrderItemApprovals"]
    next_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_items_approvals_list = []
        for order_items_approvals_list_item_data in self.order_items_approvals_list:
            order_items_approvals_list_item = order_items_approvals_list_item_data.to_dict()

            order_items_approvals_list.append(order_items_approvals_list_item)

        next_token = self.next_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OrderItemsApprovalsList": order_items_approvals_list,
            }
        )
        if next_token is not UNSET:
            field_dict["NextToken"] = next_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_item_approvals import OrderItemApprovals

        d = src_dict.copy()
        order_items_approvals_list = []
        _order_items_approvals_list = d.pop("OrderItemsApprovalsList")
        for order_items_approvals_list_item_data in _order_items_approvals_list:
            order_items_approvals_list_item = OrderItemApprovals.from_dict(order_items_approvals_list_item_data)

            order_items_approvals_list.append(order_items_approvals_list_item)

        next_token = d.pop("NextToken", UNSET)

        result = cls(
            order_items_approvals_list=order_items_approvals_list,
            next_token=next_token,
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
