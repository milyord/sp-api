from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_set_list_item import AttributeSetListItem
    from ..models.competitive_pricing_type import CompetitivePricingType
    from ..models.identifier_type import IdentifierType
    from ..models.offer_type import OfferType
    from ..models.relationship_list_item import RelationshipListItem
    from ..models.sales_rank_type import SalesRankType


T = TypeVar("T", bound="Product")


@attr.s(auto_attribs=True)
class Product:
    r"""An item.

    Attributes:
        identifiers (IdentifierType): Specifies the identifiers used to uniquely identify an item.
        attribute_sets (Union[Unset, List['AttributeSetListItem']]): A list of product attributes if they are applicable
            to the product that is returned.
        relationships (Union[Unset, List['RelationshipListItem']]): A list that contains product variation information,
            if applicable.
        competitive_pricing (Union[Unset, CompetitivePricingType]): Competitive pricing information for the item.
        sales_rankings (Union[Unset, List['SalesRankType']]): A list of sales rank information for the item, by
            category.
        offers (Union[Unset, List['OfferType']]): A list of offers.
    """

    identifiers: "IdentifierType"
    attribute_sets: Union[Unset, List["AttributeSetListItem"]] = UNSET
    relationships: Union[Unset, List["RelationshipListItem"]] = UNSET
    competitive_pricing: Union[Unset, "CompetitivePricingType"] = UNSET
    sales_rankings: Union[Unset, List["SalesRankType"]] = UNSET
    offers: Union[Unset, List["OfferType"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifiers = self.identifiers.to_dict()

        attribute_sets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_sets, Unset):
            attribute_sets = []
            for componentsschemas_attribute_set_list_item_data in self.attribute_sets:
                componentsschemas_attribute_set_list_item = componentsschemas_attribute_set_list_item_data.to_dict()

                attribute_sets.append(componentsschemas_attribute_set_list_item)

        relationships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for componentsschemas_relationship_list_item_data in self.relationships:
                componentsschemas_relationship_list_item = componentsschemas_relationship_list_item_data.to_dict()

                relationships.append(componentsschemas_relationship_list_item)

        competitive_pricing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competitive_pricing, Unset):
            competitive_pricing = self.competitive_pricing.to_dict()

        sales_rankings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_rankings, Unset):
            sales_rankings = []
            for componentsschemas_sales_rank_list_item_data in self.sales_rankings:
                componentsschemas_sales_rank_list_item = componentsschemas_sales_rank_list_item_data.to_dict()

                sales_rankings.append(componentsschemas_sales_rank_list_item)

        offers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.offers, Unset):
            offers = []
            for componentsschemas_offers_list_item_data in self.offers:
                componentsschemas_offers_list_item = componentsschemas_offers_list_item_data.to_dict()

                offers.append(componentsschemas_offers_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Identifiers": identifiers,
            }
        )
        if attribute_sets is not UNSET:
            field_dict["AttributeSets"] = attribute_sets
        if relationships is not UNSET:
            field_dict["Relationships"] = relationships
        if competitive_pricing is not UNSET:
            field_dict["CompetitivePricing"] = competitive_pricing
        if sales_rankings is not UNSET:
            field_dict["SalesRankings"] = sales_rankings
        if offers is not UNSET:
            field_dict["Offers"] = offers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_set_list_item import AttributeSetListItem
        from ..models.competitive_pricing_type import CompetitivePricingType
        from ..models.identifier_type import IdentifierType
        from ..models.offer_type import OfferType
        from ..models.relationship_list_item import RelationshipListItem
        from ..models.sales_rank_type import SalesRankType

        d = src_dict.copy()
        identifiers = IdentifierType.from_dict(d.pop("Identifiers"))

        attribute_sets = []
        _attribute_sets = d.pop("AttributeSets", UNSET)
        for componentsschemas_attribute_set_list_item_data in _attribute_sets or []:
            componentsschemas_attribute_set_list_item = AttributeSetListItem.from_dict(
                componentsschemas_attribute_set_list_item_data
            )

            attribute_sets.append(componentsschemas_attribute_set_list_item)

        relationships = []
        _relationships = d.pop("Relationships", UNSET)
        for componentsschemas_relationship_list_item_data in _relationships or []:
            componentsschemas_relationship_list_item = RelationshipListItem.from_dict(
                componentsschemas_relationship_list_item_data
            )

            relationships.append(componentsschemas_relationship_list_item)

        _competitive_pricing = d.pop("CompetitivePricing", UNSET)
        competitive_pricing: Union[Unset, CompetitivePricingType]
        if isinstance(_competitive_pricing, Unset):
            competitive_pricing = UNSET
        else:
            competitive_pricing = CompetitivePricingType.from_dict(_competitive_pricing)

        sales_rankings = []
        _sales_rankings = d.pop("SalesRankings", UNSET)
        for componentsschemas_sales_rank_list_item_data in _sales_rankings or []:
            componentsschemas_sales_rank_list_item = SalesRankType.from_dict(
                componentsschemas_sales_rank_list_item_data
            )

            sales_rankings.append(componentsschemas_sales_rank_list_item)

        offers = []
        _offers = d.pop("Offers", UNSET)
        for componentsschemas_offers_list_item_data in _offers or []:
            componentsschemas_offers_list_item = OfferType.from_dict(componentsschemas_offers_list_item_data)

            offers.append(componentsschemas_offers_list_item)

        result = cls(
            identifiers=identifiers,
            attribute_sets=attribute_sets,
            relationships=relationships,
            competitive_pricing=competitive_pricing,
            sales_rankings=sales_rankings,
            offers=offers,
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
