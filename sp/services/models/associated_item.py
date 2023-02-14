from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.associated_item_item_status import AssociatedItemItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_delivery import ItemDelivery


T = TypeVar("T", bound="AssociatedItem")


@attr.s(auto_attribs=True)
class AssociatedItem:
    r"""Information about an item associated with the service job.

    Attributes:
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
        title (Union[Unset, str]): The title of the item.
        quantity (Union[Unset, int]): The total number of items included in the order.
        order_id (Union[Unset, str]): The Amazon-defined identifier for an order placed by the buyer, in 3-7-7 format.
        item_status (Union[Unset, AssociatedItemItemStatus]): The status of the item.
        brand_name (Union[Unset, str]): The brand name of the item.
        item_delivery (Union[Unset, ItemDelivery]): Delivery information for the item.
    """

    asin: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    order_id: Union[Unset, str] = UNSET
    item_status: Union[Unset, AssociatedItemItemStatus] = UNSET
    brand_name: Union[Unset, str] = UNSET
    item_delivery: Union[Unset, "ItemDelivery"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        title = self.title
        quantity = self.quantity
        order_id = self.order_id
        item_status: Union[Unset, str] = UNSET
        if not isinstance(self.item_status, Unset):
            item_status = self.item_status.value

        brand_name = self.brand_name
        item_delivery: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_delivery, Unset):
            item_delivery = self.item_delivery.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asin is not UNSET:
            field_dict["asin"] = asin
        if title is not UNSET:
            field_dict["title"] = title
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if item_status is not UNSET:
            field_dict["itemStatus"] = item_status
        if brand_name is not UNSET:
            field_dict["brandName"] = brand_name
        if item_delivery is not UNSET:
            field_dict["itemDelivery"] = item_delivery

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_delivery import ItemDelivery

        d = src_dict.copy()
        asin = d.pop("asin", UNSET)

        title = d.pop("title", UNSET)

        quantity = d.pop("quantity", UNSET)

        order_id = d.pop("orderId", UNSET)

        _item_status = d.pop("itemStatus", UNSET)
        item_status: Union[Unset, AssociatedItemItemStatus]
        if isinstance(_item_status, Unset):
            item_status = UNSET
        else:
            item_status = AssociatedItemItemStatus(_item_status)

        brand_name = d.pop("brandName", UNSET)

        _item_delivery = d.pop("itemDelivery", UNSET)
        item_delivery: Union[Unset, ItemDelivery]
        if isinstance(_item_delivery, Unset):
            item_delivery = UNSET
        else:
            item_delivery = ItemDelivery.from_dict(_item_delivery)

        result = cls(
            asin=asin,
            title=title,
            quantity=quantity,
            order_id=order_id,
            item_status=item_status,
            brand_name=brand_name,
            item_delivery=item_delivery,
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
