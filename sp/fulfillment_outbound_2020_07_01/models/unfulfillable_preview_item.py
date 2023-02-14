from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnfulfillablePreviewItem")


@attr.s(auto_attribs=True)
class UnfulfillablePreviewItem:
    r"""Information about unfulfillable items in a fulfillment order preview.

    Attributes:
        seller_sku (str): The seller SKU of the item.
        quantity (int): The item quantity.
        seller_fulfillment_order_item_id (str): A fulfillment order item identifier created with a call to the
            getFulfillmentPreview operation.
        item_unfulfillable_reasons (Union[Unset, List[str]]):
    """

    seller_sku: str
    quantity: int
    seller_fulfillment_order_item_id: str
    item_unfulfillable_reasons: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        quantity = self.quantity
        seller_fulfillment_order_item_id = self.seller_fulfillment_order_item_id
        item_unfulfillable_reasons: Union[Unset, List[str]] = UNSET
        if not isinstance(self.item_unfulfillable_reasons, Unset):
            item_unfulfillable_reasons = self.item_unfulfillable_reasons

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerSku": seller_sku,
                "quantity": quantity,
                "sellerFulfillmentOrderItemId": seller_fulfillment_order_item_id,
            }
        )
        if item_unfulfillable_reasons is not UNSET:
            field_dict["itemUnfulfillableReasons"] = item_unfulfillable_reasons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seller_sku = d.pop("sellerSku")

        quantity = d.pop("quantity")

        seller_fulfillment_order_item_id = d.pop("sellerFulfillmentOrderItemId")

        item_unfulfillable_reasons = cast(List[str], d.pop("itemUnfulfillableReasons", UNSET))

        result = cls(
            seller_sku=seller_sku,
            quantity=quantity,
            seller_fulfillment_order_item_id=seller_fulfillment_order_item_id,
            item_unfulfillable_reasons=item_unfulfillable_reasons,
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
