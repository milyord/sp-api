from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.product_type_definition_requirements import ProductTypeDefinitionRequirements
from ..models.product_type_definition_requirements_enforced import ProductTypeDefinitionRequirementsEnforced
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_type_definition_property_groups import ProductTypeDefinitionPropertyGroups
    from ..models.product_type_version import ProductTypeVersion
    from ..models.schema_link import SchemaLink


T = TypeVar("T", bound="ProductTypeDefinition")


@attr.s(auto_attribs=True)
class ProductTypeDefinition:
    r"""A product type definition represents the attributes and data requirements for a product type in the Amazon catalog.
    Product type definitions are used interchangeably between the Selling Partner API for Listings Items, Selling
    Partner API for Catalog Items, and JSON-based listings feeds in the Selling Partner API for Feeds.

        Attributes:
            schema (SchemaLink):
            requirements (ProductTypeDefinitionRequirements): Name of the requirements set represented in this product type
                definition.
            requirements_enforced (ProductTypeDefinitionRequirementsEnforced): Identifies if the required attributes for a
                requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural
                validation of individual attributes without all of the required attributes being present (such as for partial
                updates).
            property_groups (ProductTypeDefinitionPropertyGroups): Mapping of property group names to property groups.
                Property groups represent logical groupings of schema properties that can be used for display or informational
                purposes.
            locale (str): Locale of the display elements contained in the product type definition.
            marketplace_ids (List[str]): Amazon marketplace identifiers for which the product type definition is applicable.
            product_type (str): The name of the Amazon product type that this product type definition applies to.
            product_type_version (ProductTypeVersion): The version details for an Amazon product type.
            meta_schema (Union[Unset, SchemaLink]):
    """

    schema: "SchemaLink"
    requirements: ProductTypeDefinitionRequirements
    requirements_enforced: ProductTypeDefinitionRequirementsEnforced
    property_groups: "ProductTypeDefinitionPropertyGroups"
    locale: str
    marketplace_ids: List[str]
    product_type: str
    product_type_version: "ProductTypeVersion"
    meta_schema: Union[Unset, "SchemaLink"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schema = self.schema.to_dict()

        requirements = self.requirements.value

        requirements_enforced = self.requirements_enforced.value

        property_groups = self.property_groups.to_dict()

        locale = self.locale
        marketplace_ids = self.marketplace_ids

        product_type = self.product_type
        product_type_version = self.product_type_version.to_dict()

        meta_schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_schema, Unset):
            meta_schema = self.meta_schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema": schema,
                "requirements": requirements,
                "requirementsEnforced": requirements_enforced,
                "propertyGroups": property_groups,
                "locale": locale,
                "marketplaceIds": marketplace_ids,
                "productType": product_type,
                "productTypeVersion": product_type_version,
            }
        )
        if meta_schema is not UNSET:
            field_dict["metaSchema"] = meta_schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_type_definition_property_groups import ProductTypeDefinitionPropertyGroups
        from ..models.product_type_version import ProductTypeVersion
        from ..models.schema_link import SchemaLink

        d = src_dict.copy()
        schema = SchemaLink.from_dict(d.pop("schema"))

        requirements = ProductTypeDefinitionRequirements(d.pop("requirements"))

        requirements_enforced = ProductTypeDefinitionRequirementsEnforced(d.pop("requirementsEnforced"))

        property_groups = ProductTypeDefinitionPropertyGroups.from_dict(d.pop("propertyGroups"))

        locale = d.pop("locale")

        marketplace_ids = cast(List[str], d.pop("marketplaceIds"))

        product_type = d.pop("productType")

        product_type_version = ProductTypeVersion.from_dict(d.pop("productTypeVersion"))

        _meta_schema = d.pop("metaSchema", UNSET)
        meta_schema: Union[Unset, SchemaLink]
        if isinstance(_meta_schema, Unset):
            meta_schema = UNSET
        else:
            meta_schema = SchemaLink.from_dict(_meta_schema)

        result = cls(
            schema=schema,
            requirements=requirements,
            requirements_enforced=requirements_enforced,
            property_groups=property_groups,
            locale=locale,
            marketplace_ids=marketplace_ids,
            product_type=product_type,
            product_type_version=product_type_version,
            meta_schema=meta_schema,
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
