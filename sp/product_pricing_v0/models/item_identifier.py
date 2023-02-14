from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.condition_type import ConditionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemIdentifier")


@attr.s(auto_attribs=True)
class ItemIdentifier:
    r"""Information that identifies an item.

    Attributes:
        marketplace_id (str): A marketplace identifier. Specifies the marketplace from which prices are returned.
        item_condition (ConditionType): Indicates the condition of the item. Possible values: New, Used, Collectible,
            Refurbished, Club.
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
        seller_sku (Union[Unset, str]): The seller stock keeping unit (SKU) of the item.
    """

    marketplace_id: str
    item_condition: ConditionType
    asin: Union[Unset, str] = UNSET
    seller_sku: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        item_condition = self.item_condition.value

        asin = self.asin
        seller_sku = self.seller_sku

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "MarketplaceId": marketplace_id,
                "ItemCondition": item_condition,
            }
        )
        if asin is not UNSET:
            field_dict["ASIN"] = asin
        if seller_sku is not UNSET:
            field_dict["SellerSKU"] = seller_sku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("MarketplaceId")

        item_condition = ConditionType(d.pop("ItemCondition"))

        asin = d.pop("ASIN", UNSET)

        seller_sku = d.pop("SellerSKU", UNSET)

        result = cls(
            marketplace_id=marketplace_id,
            item_condition=item_condition,
            asin=asin,
            seller_sku=seller_sku,
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
