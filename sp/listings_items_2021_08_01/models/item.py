from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fulfillment_availability import FulfillmentAvailability
    from ..models.issue import Issue
    from ..models.item_attributes import ItemAttributes
    from ..models.item_offer_by_marketplace import ItemOfferByMarketplace
    from ..models.item_procurement import ItemProcurement
    from ..models.item_summary_by_marketplace import ItemSummaryByMarketplace


T = TypeVar("T", bound="Item")


@attr.s(auto_attribs=True)
class Item:
    r"""A listings item.

    Attributes:
        sku (str): A selling partner provided identifier for an Amazon listing.
        summaries (Union[Unset, List['ItemSummaryByMarketplace']]): Summary details of a listings item.
        attributes (Union[Unset, ItemAttributes]): JSON object containing structured listings item attribute data keyed
            by attribute name.
        issues (Union[Unset, List['Issue']]): Issues associated with the listings item.
        offers (Union[Unset, List['ItemOfferByMarketplace']]): Offer details for the listings item.
        fulfillment_availability (Union[Unset, List['FulfillmentAvailability']]): Fulfillment availability for the
            listings item.
        procurement (Union[Unset, ItemProcurement]): Vendor procurement information for the listings item.
    """

    sku: str
    summaries: Union[Unset, List["ItemSummaryByMarketplace"]] = UNSET
    attributes: Union[Unset, "ItemAttributes"] = UNSET
    issues: Union[Unset, List["Issue"]] = UNSET
    offers: Union[Unset, List["ItemOfferByMarketplace"]] = UNSET
    fulfillment_availability: Union[Unset, List["FulfillmentAvailability"]] = UNSET
    procurement: Union[Unset, "ItemProcurement"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku = self.sku
        summaries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.summaries, Unset):
            summaries = []
            for componentsschemas_item_summaries_item_data in self.summaries:
                componentsschemas_item_summaries_item = componentsschemas_item_summaries_item_data.to_dict()

                summaries.append(componentsschemas_item_summaries_item)

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        issues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for componentsschemas_item_issues_item_data in self.issues:
                componentsschemas_item_issues_item = componentsschemas_item_issues_item_data.to_dict()

                issues.append(componentsschemas_item_issues_item)

        offers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.offers, Unset):
            offers = []
            for componentsschemas_item_offers_item_data in self.offers:
                componentsschemas_item_offers_item = componentsschemas_item_offers_item_data.to_dict()

                offers.append(componentsschemas_item_offers_item)

        fulfillment_availability: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulfillment_availability, Unset):
            fulfillment_availability = []
            for fulfillment_availability_item_data in self.fulfillment_availability:
                fulfillment_availability_item = fulfillment_availability_item_data.to_dict()

                fulfillment_availability.append(fulfillment_availability_item)

        procurement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.procurement, Unset):
            procurement = self.procurement.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sku": sku,
            }
        )
        if summaries is not UNSET:
            field_dict["summaries"] = summaries
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if issues is not UNSET:
            field_dict["issues"] = issues
        if offers is not UNSET:
            field_dict["offers"] = offers
        if fulfillment_availability is not UNSET:
            field_dict["fulfillmentAvailability"] = fulfillment_availability
        if procurement is not UNSET:
            field_dict["procurement"] = procurement

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fulfillment_availability import FulfillmentAvailability
        from ..models.issue import Issue
        from ..models.item_attributes import ItemAttributes
        from ..models.item_offer_by_marketplace import ItemOfferByMarketplace
        from ..models.item_procurement import ItemProcurement
        from ..models.item_summary_by_marketplace import ItemSummaryByMarketplace

        d = src_dict.copy()
        sku = d.pop("sku")

        summaries = []
        _summaries = d.pop("summaries", UNSET)
        for componentsschemas_item_summaries_item_data in _summaries or []:
            componentsschemas_item_summaries_item = ItemSummaryByMarketplace.from_dict(
                componentsschemas_item_summaries_item_data
            )

            summaries.append(componentsschemas_item_summaries_item)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, ItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ItemAttributes.from_dict(_attributes)

        issues = []
        _issues = d.pop("issues", UNSET)
        for componentsschemas_item_issues_item_data in _issues or []:
            componentsschemas_item_issues_item = Issue.from_dict(componentsschemas_item_issues_item_data)

            issues.append(componentsschemas_item_issues_item)

        offers = []
        _offers = d.pop("offers", UNSET)
        for componentsschemas_item_offers_item_data in _offers or []:
            componentsschemas_item_offers_item = ItemOfferByMarketplace.from_dict(
                componentsschemas_item_offers_item_data
            )

            offers.append(componentsschemas_item_offers_item)

        fulfillment_availability = []
        _fulfillment_availability = d.pop("fulfillmentAvailability", UNSET)
        for fulfillment_availability_item_data in _fulfillment_availability or []:
            fulfillment_availability_item = FulfillmentAvailability.from_dict(fulfillment_availability_item_data)

            fulfillment_availability.append(fulfillment_availability_item)

        _procurement = d.pop("procurement", UNSET)
        procurement: Union[Unset, ItemProcurement]
        if isinstance(_procurement, Unset):
            procurement = UNSET
        else:
            procurement = ItemProcurement.from_dict(_procurement)

        result = cls(
            sku=sku,
            summaries=summaries,
            attributes=attributes,
            issues=issues,
            offers=offers,
            fulfillment_availability=fulfillment_availability,
            procurement=procurement,
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
