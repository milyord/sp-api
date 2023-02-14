from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.condition_type import ConditionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_identifier import ItemIdentifier
    from ..models.offer_detail import OfferDetail
    from ..models.summary import Summary


T = TypeVar("T", bound="GetOffersResult")


@attr.s(auto_attribs=True)
class GetOffersResult:
    r"""
    Attributes:
        marketplace_id (str): A marketplace identifier.
        item_condition (ConditionType): Indicates the condition of the item. Possible values: New, Used, Collectible,
            Refurbished, Club.
        status (str): The status of the operation.
        identifier (ItemIdentifier): Information that identifies an item.
        summary (Summary): Contains price information about the product, including the LowestPrices and BuyBoxPrices,
            the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.
        offers (List['OfferDetail']):
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
        sku (Union[Unset, str]): The stock keeping unit (SKU) of the item.
    """

    marketplace_id: str
    item_condition: ConditionType
    status: str
    identifier: "ItemIdentifier"
    summary: "Summary"
    offers: List["OfferDetail"]
    asin: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        item_condition = self.item_condition.value

        status = self.status
        identifier = self.identifier.to_dict()

        summary = self.summary.to_dict()

        offers = []
        for componentsschemas_offer_detail_list_item_data in self.offers:
            componentsschemas_offer_detail_list_item = componentsschemas_offer_detail_list_item_data.to_dict()

            offers.append(componentsschemas_offer_detail_list_item)

        asin = self.asin
        sku = self.sku

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "MarketplaceID": marketplace_id,
                "ItemCondition": item_condition,
                "status": status,
                "Identifier": identifier,
                "Summary": summary,
                "Offers": offers,
            }
        )
        if asin is not UNSET:
            field_dict["ASIN"] = asin
        if sku is not UNSET:
            field_dict["SKU"] = sku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_identifier import ItemIdentifier
        from ..models.offer_detail import OfferDetail
        from ..models.summary import Summary

        d = src_dict.copy()
        marketplace_id = d.pop("MarketplaceID")

        item_condition = ConditionType(d.pop("ItemCondition"))

        status = d.pop("status")

        identifier = ItemIdentifier.from_dict(d.pop("Identifier"))

        summary = Summary.from_dict(d.pop("Summary"))

        offers = []
        _offers = d.pop("Offers")
        for componentsschemas_offer_detail_list_item_data in _offers:
            componentsschemas_offer_detail_list_item = OfferDetail.from_dict(
                componentsschemas_offer_detail_list_item_data
            )

            offers.append(componentsschemas_offer_detail_list_item)

        asin = d.pop("ASIN", UNSET)

        sku = d.pop("SKU", UNSET)

        result = cls(
            marketplace_id=marketplace_id,
            item_condition=item_condition,
            status=status,
            identifier=identifier,
            summary=summary,
            offers=offers,
            asin=asin,
            sku=sku,
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
