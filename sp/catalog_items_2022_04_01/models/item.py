from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_attributes import ItemAttributes
    from ..models.item_dimensions_by_marketplace import ItemDimensionsByMarketplace
    from ..models.item_identifiers_by_marketplace import ItemIdentifiersByMarketplace
    from ..models.item_images_by_marketplace import ItemImagesByMarketplace
    from ..models.item_product_type_by_marketplace import ItemProductTypeByMarketplace
    from ..models.item_relationships_by_marketplace import ItemRelationshipsByMarketplace
    from ..models.item_sales_ranks_by_marketplace import ItemSalesRanksByMarketplace
    from ..models.item_summary_by_marketplace import ItemSummaryByMarketplace
    from ..models.item_vendor_details_by_marketplace import ItemVendorDetailsByMarketplace


T = TypeVar("T", bound="Item")


@attr.s(auto_attribs=True)
class Item:
    r"""An item in the Amazon catalog.

    Attributes:
        asin (str): Amazon Standard Identification Number (ASIN) is the unique identifier for an item in the Amazon
            catalog.
        attributes (Union[Unset, ItemAttributes]): A JSON object that contains structured item attribute data keyed by
            attribute name. Catalog item attributes conform to the related product type definitions available in the Selling
            Partner API for Product Type Definitions.
        dimensions (Union[Unset, List['ItemDimensionsByMarketplace']]): Array of dimensions associated with the item in
            the Amazon catalog by Amazon marketplace.
        identifiers (Union[Unset, List['ItemIdentifiersByMarketplace']]): Identifiers associated with the item in the
            Amazon catalog, such as UPC and EAN identifiers.
        images (Union[Unset, List['ItemImagesByMarketplace']]): Images for an item in the Amazon catalog.
        product_types (Union[Unset, List['ItemProductTypeByMarketplace']]): Product types associated with the Amazon
            catalog item.
        relationships (Union[Unset, List['ItemRelationshipsByMarketplace']]): Relationships by marketplace for an Amazon
            catalog item (for example, variations).
        sales_ranks (Union[Unset, List['ItemSalesRanksByMarketplace']]): Sales ranks of an Amazon catalog item.
        summaries (Union[Unset, List['ItemSummaryByMarketplace']]): Summary details of an Amazon catalog item.
        vendor_details (Union[Unset, List['ItemVendorDetailsByMarketplace']]): Vendor details associated with an Amazon
            catalog item. Vendor details are available to vendors only.
    """

    asin: str
    attributes: Union[Unset, "ItemAttributes"] = UNSET
    dimensions: Union[Unset, List["ItemDimensionsByMarketplace"]] = UNSET
    identifiers: Union[Unset, List["ItemIdentifiersByMarketplace"]] = UNSET
    images: Union[Unset, List["ItemImagesByMarketplace"]] = UNSET
    product_types: Union[Unset, List["ItemProductTypeByMarketplace"]] = UNSET
    relationships: Union[Unset, List["ItemRelationshipsByMarketplace"]] = UNSET
    sales_ranks: Union[Unset, List["ItemSalesRanksByMarketplace"]] = UNSET
    summaries: Union[Unset, List["ItemSummaryByMarketplace"]] = UNSET
    vendor_details: Union[Unset, List["ItemVendorDetailsByMarketplace"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        dimensions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = []
            for componentsschemas_item_dimensions_item_data in self.dimensions:
                componentsschemas_item_dimensions_item = componentsschemas_item_dimensions_item_data.to_dict()

                dimensions.append(componentsschemas_item_dimensions_item)

        identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for componentsschemas_item_identifiers_item_data in self.identifiers:
                componentsschemas_item_identifiers_item = componentsschemas_item_identifiers_item_data.to_dict()

                identifiers.append(componentsschemas_item_identifiers_item)

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for componentsschemas_item_images_item_data in self.images:
                componentsschemas_item_images_item = componentsschemas_item_images_item_data.to_dict()

                images.append(componentsschemas_item_images_item)

        product_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_types, Unset):
            product_types = []
            for componentsschemas_item_product_types_item_data in self.product_types:
                componentsschemas_item_product_types_item = componentsschemas_item_product_types_item_data.to_dict()

                product_types.append(componentsschemas_item_product_types_item)

        relationships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for componentsschemas_item_relationships_item_data in self.relationships:
                componentsschemas_item_relationships_item = componentsschemas_item_relationships_item_data.to_dict()

                relationships.append(componentsschemas_item_relationships_item)

        sales_ranks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_ranks, Unset):
            sales_ranks = []
            for componentsschemas_item_sales_ranks_item_data in self.sales_ranks:
                componentsschemas_item_sales_ranks_item = componentsschemas_item_sales_ranks_item_data.to_dict()

                sales_ranks.append(componentsschemas_item_sales_ranks_item)

        summaries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.summaries, Unset):
            summaries = []
            for componentsschemas_item_summaries_item_data in self.summaries:
                componentsschemas_item_summaries_item = componentsschemas_item_summaries_item_data.to_dict()

                summaries.append(componentsschemas_item_summaries_item)

        vendor_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vendor_details, Unset):
            vendor_details = []
            for componentsschemas_item_vendor_details_item_data in self.vendor_details:
                componentsschemas_item_vendor_details_item = componentsschemas_item_vendor_details_item_data.to_dict()

                vendor_details.append(componentsschemas_item_vendor_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asin": asin,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if images is not UNSET:
            field_dict["images"] = images
        if product_types is not UNSET:
            field_dict["productTypes"] = product_types
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if sales_ranks is not UNSET:
            field_dict["salesRanks"] = sales_ranks
        if summaries is not UNSET:
            field_dict["summaries"] = summaries
        if vendor_details is not UNSET:
            field_dict["vendorDetails"] = vendor_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_attributes import ItemAttributes
        from ..models.item_dimensions_by_marketplace import ItemDimensionsByMarketplace
        from ..models.item_identifiers_by_marketplace import ItemIdentifiersByMarketplace
        from ..models.item_images_by_marketplace import ItemImagesByMarketplace
        from ..models.item_product_type_by_marketplace import ItemProductTypeByMarketplace
        from ..models.item_relationships_by_marketplace import ItemRelationshipsByMarketplace
        from ..models.item_sales_ranks_by_marketplace import ItemSalesRanksByMarketplace
        from ..models.item_summary_by_marketplace import ItemSummaryByMarketplace
        from ..models.item_vendor_details_by_marketplace import ItemVendorDetailsByMarketplace

        d = src_dict.copy()
        asin = d.pop("asin")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, ItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ItemAttributes.from_dict(_attributes)

        dimensions = []
        _dimensions = d.pop("dimensions", UNSET)
        for componentsschemas_item_dimensions_item_data in _dimensions or []:
            componentsschemas_item_dimensions_item = ItemDimensionsByMarketplace.from_dict(
                componentsschemas_item_dimensions_item_data
            )

            dimensions.append(componentsschemas_item_dimensions_item)

        identifiers = []
        _identifiers = d.pop("identifiers", UNSET)
        for componentsschemas_item_identifiers_item_data in _identifiers or []:
            componentsschemas_item_identifiers_item = ItemIdentifiersByMarketplace.from_dict(
                componentsschemas_item_identifiers_item_data
            )

            identifiers.append(componentsschemas_item_identifiers_item)

        images = []
        _images = d.pop("images", UNSET)
        for componentsschemas_item_images_item_data in _images or []:
            componentsschemas_item_images_item = ItemImagesByMarketplace.from_dict(
                componentsschemas_item_images_item_data
            )

            images.append(componentsschemas_item_images_item)

        product_types = []
        _product_types = d.pop("productTypes", UNSET)
        for componentsschemas_item_product_types_item_data in _product_types or []:
            componentsschemas_item_product_types_item = ItemProductTypeByMarketplace.from_dict(
                componentsschemas_item_product_types_item_data
            )

            product_types.append(componentsschemas_item_product_types_item)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for componentsschemas_item_relationships_item_data in _relationships or []:
            componentsschemas_item_relationships_item = ItemRelationshipsByMarketplace.from_dict(
                componentsschemas_item_relationships_item_data
            )

            relationships.append(componentsschemas_item_relationships_item)

        sales_ranks = []
        _sales_ranks = d.pop("salesRanks", UNSET)
        for componentsschemas_item_sales_ranks_item_data in _sales_ranks or []:
            componentsschemas_item_sales_ranks_item = ItemSalesRanksByMarketplace.from_dict(
                componentsschemas_item_sales_ranks_item_data
            )

            sales_ranks.append(componentsschemas_item_sales_ranks_item)

        summaries = []
        _summaries = d.pop("summaries", UNSET)
        for componentsschemas_item_summaries_item_data in _summaries or []:
            componentsschemas_item_summaries_item = ItemSummaryByMarketplace.from_dict(
                componentsschemas_item_summaries_item_data
            )

            summaries.append(componentsschemas_item_summaries_item)

        vendor_details = []
        _vendor_details = d.pop("vendorDetails", UNSET)
        for componentsschemas_item_vendor_details_item_data in _vendor_details or []:
            componentsschemas_item_vendor_details_item = ItemVendorDetailsByMarketplace.from_dict(
                componentsschemas_item_vendor_details_item_data
            )

            vendor_details.append(componentsschemas_item_vendor_details_item)

        result = cls(
            asin=asin,
            attributes=attributes,
            dimensions=dimensions,
            identifiers=identifiers,
            images=images,
            product_types=product_types,
            relationships=relationships,
            sales_ranks=sales_ranks,
            summaries=summaries,
            vendor_details=vendor_details,
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
