from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_vendor_details_by_marketplace_replenishment_category import (
    ItemVendorDetailsByMarketplaceReplenishmentCategory,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_vendor_details_category import ItemVendorDetailsCategory


T = TypeVar("T", bound="ItemVendorDetailsByMarketplace")


@attr.s(auto_attribs=True)
class ItemVendorDetailsByMarketplace:
    r"""Vendor details associated with an Amazon catalog item for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        brand_code (Union[Unset, str]): Brand code associated with an Amazon catalog item.
        manufacturer_code (Union[Unset, str]): Manufacturer code associated with an Amazon catalog item.
        manufacturer_code_parent (Union[Unset, str]): Parent vendor code of the manufacturer code.
        product_category (Union[Unset, ItemVendorDetailsCategory]): Product category or subcategory associated with an
            Amazon catalog item.
        product_group (Union[Unset, str]): Product group associated with an Amazon catalog item.
        product_subcategory (Union[Unset, ItemVendorDetailsCategory]): Product category or subcategory associated with
            an Amazon catalog item.
        replenishment_category (Union[Unset, ItemVendorDetailsByMarketplaceReplenishmentCategory]): Replenishment
            category associated with an Amazon catalog item.
    """

    marketplace_id: str
    brand_code: Union[Unset, str] = UNSET
    manufacturer_code: Union[Unset, str] = UNSET
    manufacturer_code_parent: Union[Unset, str] = UNSET
    product_category: Union[Unset, "ItemVendorDetailsCategory"] = UNSET
    product_group: Union[Unset, str] = UNSET
    product_subcategory: Union[Unset, "ItemVendorDetailsCategory"] = UNSET
    replenishment_category: Union[Unset, ItemVendorDetailsByMarketplaceReplenishmentCategory] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        brand_code = self.brand_code
        manufacturer_code = self.manufacturer_code
        manufacturer_code_parent = self.manufacturer_code_parent
        product_category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_category, Unset):
            product_category = self.product_category.to_dict()

        product_group = self.product_group
        product_subcategory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_subcategory, Unset):
            product_subcategory = self.product_subcategory.to_dict()

        replenishment_category: Union[Unset, str] = UNSET
        if not isinstance(self.replenishment_category, Unset):
            replenishment_category = self.replenishment_category.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
            }
        )
        if brand_code is not UNSET:
            field_dict["brandCode"] = brand_code
        if manufacturer_code is not UNSET:
            field_dict["manufacturerCode"] = manufacturer_code
        if manufacturer_code_parent is not UNSET:
            field_dict["manufacturerCodeParent"] = manufacturer_code_parent
        if product_category is not UNSET:
            field_dict["productCategory"] = product_category
        if product_group is not UNSET:
            field_dict["productGroup"] = product_group
        if product_subcategory is not UNSET:
            field_dict["productSubcategory"] = product_subcategory
        if replenishment_category is not UNSET:
            field_dict["replenishmentCategory"] = replenishment_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_vendor_details_category import ItemVendorDetailsCategory

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        brand_code = d.pop("brandCode", UNSET)

        manufacturer_code = d.pop("manufacturerCode", UNSET)

        manufacturer_code_parent = d.pop("manufacturerCodeParent", UNSET)

        _product_category = d.pop("productCategory", UNSET)
        product_category: Union[Unset, ItemVendorDetailsCategory]
        if isinstance(_product_category, Unset):
            product_category = UNSET
        else:
            product_category = ItemVendorDetailsCategory.from_dict(_product_category)

        product_group = d.pop("productGroup", UNSET)

        _product_subcategory = d.pop("productSubcategory", UNSET)
        product_subcategory: Union[Unset, ItemVendorDetailsCategory]
        if isinstance(_product_subcategory, Unset):
            product_subcategory = UNSET
        else:
            product_subcategory = ItemVendorDetailsCategory.from_dict(_product_subcategory)

        _replenishment_category = d.pop("replenishmentCategory", UNSET)
        replenishment_category: Union[Unset, ItemVendorDetailsByMarketplaceReplenishmentCategory]
        if isinstance(_replenishment_category, Unset):
            replenishment_category = UNSET
        else:
            replenishment_category = ItemVendorDetailsByMarketplaceReplenishmentCategory(_replenishment_category)

        result = cls(
            marketplace_id=marketplace_id,
            brand_code=brand_code,
            manufacturer_code=manufacturer_code,
            manufacturer_code_parent=manufacturer_code_parent,
            product_category=product_category,
            product_group=product_group,
            product_subcategory=product_subcategory,
            replenishment_category=replenishment_category,
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
