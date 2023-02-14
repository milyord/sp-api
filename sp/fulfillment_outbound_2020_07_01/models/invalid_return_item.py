from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.invalid_item_reason import InvalidItemReason


T = TypeVar("T", bound="InvalidReturnItem")


@attr.s(auto_attribs=True)
class InvalidReturnItem:
    r"""An item that is invalid for return.

    Attributes:
        seller_return_item_id (str): An identifier assigned by the seller to the return item.
        seller_fulfillment_order_item_id (str): The identifier assigned to the item by the seller when the fulfillment
            order was created.
        invalid_item_reason (InvalidItemReason): The reason that the item is invalid for return.
    """

    seller_return_item_id: str
    seller_fulfillment_order_item_id: str
    invalid_item_reason: "InvalidItemReason"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_return_item_id = self.seller_return_item_id
        seller_fulfillment_order_item_id = self.seller_fulfillment_order_item_id
        invalid_item_reason = self.invalid_item_reason.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerReturnItemId": seller_return_item_id,
                "sellerFulfillmentOrderItemId": seller_fulfillment_order_item_id,
                "invalidItemReason": invalid_item_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invalid_item_reason import InvalidItemReason

        d = src_dict.copy()
        seller_return_item_id = d.pop("sellerReturnItemId")

        seller_fulfillment_order_item_id = d.pop("sellerFulfillmentOrderItemId")

        invalid_item_reason = InvalidItemReason.from_dict(d.pop("invalidItemReason"))

        result = cls(
            seller_return_item_id=seller_return_item_id,
            seller_fulfillment_order_item_id=seller_fulfillment_order_item_id,
            invalid_item_reason=invalid_item_reason,
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
