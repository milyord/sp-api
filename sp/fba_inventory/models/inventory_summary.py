import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_details import InventoryDetails


T = TypeVar("T", bound="InventorySummary")


@attr.s(auto_attribs=True)
class InventorySummary:
    r"""Inventory summary for a specific item.

    Attributes:
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of an item.
        fn_sku (Union[Unset, str]): Amazon's fulfillment network SKU identifier.
        seller_sku (Union[Unset, str]): The seller SKU of the item.
        condition (Union[Unset, str]): The condition of the item as described by the seller (for example, New Item).
        inventory_details (Union[Unset, InventoryDetails]): Summarized inventory details. This object will not appear if
            the details parameter in the request is false.
        last_updated_time (Union[Unset, datetime.datetime]): The date and time that any quantity was last updated.
        product_name (Union[Unset, str]): The localized language product title of the item within the specific
            marketplace.
        total_quantity (Union[Unset, int]): The total number of units in an inbound shipment or in Amazon fulfillment
            centers.
    """

    asin: Union[Unset, str] = UNSET
    fn_sku: Union[Unset, str] = UNSET
    seller_sku: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET
    inventory_details: Union[Unset, "InventoryDetails"] = UNSET
    last_updated_time: Union[Unset, datetime.datetime] = UNSET
    product_name: Union[Unset, str] = UNSET
    total_quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        fn_sku = self.fn_sku
        seller_sku = self.seller_sku
        condition = self.condition
        inventory_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_details, Unset):
            inventory_details = self.inventory_details.to_dict()

        last_updated_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_time, Unset):
            last_updated_time = self.last_updated_time.isoformat()

        product_name = self.product_name
        total_quantity = self.total_quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asin is not UNSET:
            field_dict["asin"] = asin
        if fn_sku is not UNSET:
            field_dict["fnSku"] = fn_sku
        if seller_sku is not UNSET:
            field_dict["sellerSku"] = seller_sku
        if condition is not UNSET:
            field_dict["condition"] = condition
        if inventory_details is not UNSET:
            field_dict["inventoryDetails"] = inventory_details
        if last_updated_time is not UNSET:
            field_dict["lastUpdatedTime"] = last_updated_time
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inventory_details import InventoryDetails

        d = src_dict.copy()
        asin = d.pop("asin", UNSET)

        fn_sku = d.pop("fnSku", UNSET)

        seller_sku = d.pop("sellerSku", UNSET)

        condition = d.pop("condition", UNSET)

        _inventory_details = d.pop("inventoryDetails", UNSET)
        inventory_details: Union[Unset, InventoryDetails]
        if isinstance(_inventory_details, Unset):
            inventory_details = UNSET
        else:
            inventory_details = InventoryDetails.from_dict(_inventory_details)

        _last_updated_time = d.pop("lastUpdatedTime", UNSET)
        last_updated_time: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_time, Unset):
            last_updated_time = UNSET
        else:
            last_updated_time = isoparse(_last_updated_time)

        product_name = d.pop("productName", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        result = cls(
            asin=asin,
            fn_sku=fn_sku,
            seller_sku=seller_sku,
            condition=condition,
            inventory_details=inventory_details,
            last_updated_time=last_updated_time,
            product_name=product_name,
            total_quantity=total_quantity,
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
