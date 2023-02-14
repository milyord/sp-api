from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.item_variations_by_marketplace_variation_type import ItemVariationsByMarketplaceVariationType

T = TypeVar("T", bound="ItemVariationsByMarketplace")


@attr.s(auto_attribs=True)
class ItemVariationsByMarketplace:
    r"""Variation details for the Amazon catalog item for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        asins (List[str]): Identifiers (ASINs) of the related items.
        variation_type (ItemVariationsByMarketplaceVariationType): Type of variation relationship of the Amazon catalog
            item in the request to the related item(s): "PARENT" or "CHILD". Example: PARENT.
    """

    marketplace_id: str
    asins: List[str]
    variation_type: ItemVariationsByMarketplaceVariationType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        asins = self.asins

        variation_type = self.variation_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "asins": asins,
                "variationType": variation_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        asins = cast(List[str], d.pop("asins"))

        variation_type = ItemVariationsByMarketplaceVariationType(d.pop("variationType"))

        result = cls(
            marketplace_id=marketplace_id,
            asins=asins,
            variation_type=variation_type,
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
