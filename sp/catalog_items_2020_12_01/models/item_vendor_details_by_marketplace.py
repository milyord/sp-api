from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_vendor_details_by_marketplace_replenishment_category import (
    ItemVendorDetailsByMarketplaceReplenishmentCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemVendorDetailsByMarketplace")


@attr.s(auto_attribs=True)
class ItemVendorDetailsByMarketplace:
    r"""Vendor details associated with an Amazon catalog item for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        brand_code (Union[Unset, str]): Brand code associated with an Amazon catalog item.
        category_code (Union[Unset, str]): Product category associated with an Amazon catalog item.
        manufacturer_code (Union[Unset, str]): Manufacturer code associated with an Amazon catalog item.
        manufacturer_code_parent (Union[Unset, str]): Parent vendor code of the manufacturer code.
        product_group (Union[Unset, str]): Product group associated with an Amazon catalog item.
        replenishment_category (Union[Unset, ItemVendorDetailsByMarketplaceReplenishmentCategory]): Replenishment
            category associated with an Amazon catalog item.
        subcategory_code (Union[Unset, str]): Product subcategory associated with an Amazon catalog item.
    """

    marketplace_id: str
    brand_code: Union[Unset, str] = UNSET
    category_code: Union[Unset, str] = UNSET
    manufacturer_code: Union[Unset, str] = UNSET
    manufacturer_code_parent: Union[Unset, str] = UNSET
    product_group: Union[Unset, str] = UNSET
    replenishment_category: Union[Unset, ItemVendorDetailsByMarketplaceReplenishmentCategory] = UNSET
    subcategory_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        brand_code = self.brand_code
        category_code = self.category_code
        manufacturer_code = self.manufacturer_code
        manufacturer_code_parent = self.manufacturer_code_parent
        product_group = self.product_group
        replenishment_category: Union[Unset, str] = UNSET
        if not isinstance(self.replenishment_category, Unset):
            replenishment_category = self.replenishment_category.value

        subcategory_code = self.subcategory_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
            }
        )
        if brand_code is not UNSET:
            field_dict["brandCode"] = brand_code
        if category_code is not UNSET:
            field_dict["categoryCode"] = category_code
        if manufacturer_code is not UNSET:
            field_dict["manufacturerCode"] = manufacturer_code
        if manufacturer_code_parent is not UNSET:
            field_dict["manufacturerCodeParent"] = manufacturer_code_parent
        if product_group is not UNSET:
            field_dict["productGroup"] = product_group
        if replenishment_category is not UNSET:
            field_dict["replenishmentCategory"] = replenishment_category
        if subcategory_code is not UNSET:
            field_dict["subcategoryCode"] = subcategory_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        brand_code = d.pop("brandCode", UNSET)

        category_code = d.pop("categoryCode", UNSET)

        manufacturer_code = d.pop("manufacturerCode", UNSET)

        manufacturer_code_parent = d.pop("manufacturerCodeParent", UNSET)

        product_group = d.pop("productGroup", UNSET)

        _replenishment_category = d.pop("replenishmentCategory", UNSET)
        replenishment_category: Union[Unset, ItemVendorDetailsByMarketplaceReplenishmentCategory]
        if isinstance(_replenishment_category, Unset):
            replenishment_category = UNSET
        else:
            replenishment_category = ItemVendorDetailsByMarketplaceReplenishmentCategory(_replenishment_category)

        subcategory_code = d.pop("subcategoryCode", UNSET)

        result = cls(
            marketplace_id=marketplace_id,
            brand_code=brand_code,
            category_code=category_code,
            manufacturer_code=manufacturer_code,
            manufacturer_code_parent=manufacturer_code_parent,
            product_group=product_group,
            replenishment_category=replenishment_category,
            subcategory_code=subcategory_code,
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
