from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_item_buyer_info import OrderItemBuyerInfo


T = TypeVar("T", bound="OrderItemsBuyerInfoList")


@attr.s(auto_attribs=True)
class OrderItemsBuyerInfoList:
    r"""A single order item's buyer information list with the order ID.

    Attributes:
        order_items (List['OrderItemBuyerInfo']): A single order item's buyer information list.
        amazon_order_id (str): An Amazon-defined order identifier, in 3-7-7 format.
        next_token (Union[Unset, str]): When present and not empty, pass this string token in the next request to return
            the next response page.
    """

    order_items: List["OrderItemBuyerInfo"]
    amazon_order_id: str
    next_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_items = []
        for componentsschemas_order_item_buyer_info_list_item_data in self.order_items:
            componentsschemas_order_item_buyer_info_list_item = (
                componentsschemas_order_item_buyer_info_list_item_data.to_dict()
            )

            order_items.append(componentsschemas_order_item_buyer_info_list_item)

        amazon_order_id = self.amazon_order_id
        next_token = self.next_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OrderItems": order_items,
                "AmazonOrderId": amazon_order_id,
            }
        )
        if next_token is not UNSET:
            field_dict["NextToken"] = next_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_item_buyer_info import OrderItemBuyerInfo

        d = src_dict.copy()
        order_items = []
        _order_items = d.pop("OrderItems")
        for componentsschemas_order_item_buyer_info_list_item_data in _order_items:
            componentsschemas_order_item_buyer_info_list_item = OrderItemBuyerInfo.from_dict(
                componentsschemas_order_item_buyer_info_list_item_data
            )

            order_items.append(componentsschemas_order_item_buyer_info_list_item)

        amazon_order_id = d.pop("AmazonOrderId")

        next_token = d.pop("NextToken", UNSET)

        result = cls(
            order_items=order_items,
            amazon_order_id=amazon_order_id,
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
