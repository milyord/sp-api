import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.item_summary_by_marketplace_item_classification import ItemSummaryByMarketplaceItemClassification
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_browse_classification import ItemBrowseClassification
    from ..models.item_contributor import ItemContributor


T = TypeVar("T", bound="ItemSummaryByMarketplace")


@attr.s(auto_attribs=True)
class ItemSummaryByMarketplace:
    r"""Summary details of an Amazon catalog item for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        adult_product (Union[Unset, bool]): Identifies an Amazon catalog item is intended for an adult audience or is
            sexual in nature.
        autographed (Union[Unset, bool]): Identifies an Amazon catalog item is autographed by a player or celebrity.
        brand (Union[Unset, str]): Name of the brand associated with an Amazon catalog item.
        browse_classification (Union[Unset, ItemBrowseClassification]): Classification (browse node) associated with an
            Amazon catalog item.
        color (Union[Unset, str]): Name of the color associated with an Amazon catalog item.
        contributors (Union[Unset, List['ItemContributor']]): Individual contributors to the creation of an item, such
            as the authors or actors.
        item_classification (Union[Unset, ItemSummaryByMarketplaceItemClassification]): Classification type associated
            with the Amazon catalog item.
        item_name (Union[Unset, str]): Name, or title, associated with an Amazon catalog item.
        manufacturer (Union[Unset, str]): Name of the manufacturer associated with an Amazon catalog item.
        memorabilia (Union[Unset, bool]): Identifies an Amazon catalog item is memorabilia valued for its connection
            with historical events, culture, or entertainment.
        model_number (Union[Unset, str]): Model number associated with an Amazon catalog item.
        package_quantity (Union[Unset, int]): Quantity of an Amazon catalog item in one package.
        part_number (Union[Unset, str]): Part number associated with an Amazon catalog item.
        release_date (Union[Unset, datetime.date]): First date on which an Amazon catalog item is shippable to
            customers.
        size (Union[Unset, str]): Name of the size associated with an Amazon catalog item.
        style (Union[Unset, str]): Name of the style associated with an Amazon catalog item.
        trade_in_eligible (Union[Unset, bool]): Identifies an Amazon catalog item is eligible for trade-in.
        website_display_group (Union[Unset, str]): Identifier of the website display group associated with an Amazon
            catalog item.
        website_display_group_name (Union[Unset, str]): Display name of the website display group associated with an
            Amazon catalog item.
    """

    marketplace_id: str
    adult_product: Union[Unset, bool] = UNSET
    autographed: Union[Unset, bool] = UNSET
    brand: Union[Unset, str] = UNSET
    browse_classification: Union[Unset, "ItemBrowseClassification"] = UNSET
    color: Union[Unset, str] = UNSET
    contributors: Union[Unset, List["ItemContributor"]] = UNSET
    item_classification: Union[Unset, ItemSummaryByMarketplaceItemClassification] = UNSET
    item_name: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    memorabilia: Union[Unset, bool] = UNSET
    model_number: Union[Unset, str] = UNSET
    package_quantity: Union[Unset, int] = UNSET
    part_number: Union[Unset, str] = UNSET
    release_date: Union[Unset, datetime.date] = UNSET
    size: Union[Unset, str] = UNSET
    style: Union[Unset, str] = UNSET
    trade_in_eligible: Union[Unset, bool] = UNSET
    website_display_group: Union[Unset, str] = UNSET
    website_display_group_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        adult_product = self.adult_product
        autographed = self.autographed
        brand = self.brand
        browse_classification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.browse_classification, Unset):
            browse_classification = self.browse_classification.to_dict()

        color = self.color
        contributors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contributors, Unset):
            contributors = []
            for contributors_item_data in self.contributors:
                contributors_item = contributors_item_data.to_dict()

                contributors.append(contributors_item)

        item_classification: Union[Unset, str] = UNSET
        if not isinstance(self.item_classification, Unset):
            item_classification = self.item_classification.value

        item_name = self.item_name
        manufacturer = self.manufacturer
        memorabilia = self.memorabilia
        model_number = self.model_number
        package_quantity = self.package_quantity
        part_number = self.part_number
        release_date: Union[Unset, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        size = self.size
        style = self.style
        trade_in_eligible = self.trade_in_eligible
        website_display_group = self.website_display_group
        website_display_group_name = self.website_display_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
            }
        )
        if adult_product is not UNSET:
            field_dict["adultProduct"] = adult_product
        if autographed is not UNSET:
            field_dict["autographed"] = autographed
        if brand is not UNSET:
            field_dict["brand"] = brand
        if browse_classification is not UNSET:
            field_dict["browseClassification"] = browse_classification
        if color is not UNSET:
            field_dict["color"] = color
        if contributors is not UNSET:
            field_dict["contributors"] = contributors
        if item_classification is not UNSET:
            field_dict["itemClassification"] = item_classification
        if item_name is not UNSET:
            field_dict["itemName"] = item_name
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if memorabilia is not UNSET:
            field_dict["memorabilia"] = memorabilia
        if model_number is not UNSET:
            field_dict["modelNumber"] = model_number
        if package_quantity is not UNSET:
            field_dict["packageQuantity"] = package_quantity
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if size is not UNSET:
            field_dict["size"] = size
        if style is not UNSET:
            field_dict["style"] = style
        if trade_in_eligible is not UNSET:
            field_dict["tradeInEligible"] = trade_in_eligible
        if website_display_group is not UNSET:
            field_dict["websiteDisplayGroup"] = website_display_group
        if website_display_group_name is not UNSET:
            field_dict["websiteDisplayGroupName"] = website_display_group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_browse_classification import ItemBrowseClassification
        from ..models.item_contributor import ItemContributor

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        adult_product = d.pop("adultProduct", UNSET)

        autographed = d.pop("autographed", UNSET)

        brand = d.pop("brand", UNSET)

        _browse_classification = d.pop("browseClassification", UNSET)
        browse_classification: Union[Unset, ItemBrowseClassification]
        if isinstance(_browse_classification, Unset):
            browse_classification = UNSET
        else:
            browse_classification = ItemBrowseClassification.from_dict(_browse_classification)

        color = d.pop("color", UNSET)

        contributors = []
        _contributors = d.pop("contributors", UNSET)
        for contributors_item_data in _contributors or []:
            contributors_item = ItemContributor.from_dict(contributors_item_data)

            contributors.append(contributors_item)

        _item_classification = d.pop("itemClassification", UNSET)
        item_classification: Union[Unset, ItemSummaryByMarketplaceItemClassification]
        if isinstance(_item_classification, Unset):
            item_classification = UNSET
        else:
            item_classification = ItemSummaryByMarketplaceItemClassification(_item_classification)

        item_name = d.pop("itemName", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        memorabilia = d.pop("memorabilia", UNSET)

        model_number = d.pop("modelNumber", UNSET)

        package_quantity = d.pop("packageQuantity", UNSET)

        part_number = d.pop("partNumber", UNSET)

        _release_date = d.pop("releaseDate", UNSET)
        release_date: Union[Unset, datetime.date]
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        size = d.pop("size", UNSET)

        style = d.pop("style", UNSET)

        trade_in_eligible = d.pop("tradeInEligible", UNSET)

        website_display_group = d.pop("websiteDisplayGroup", UNSET)

        website_display_group_name = d.pop("websiteDisplayGroupName", UNSET)

        result = cls(
            marketplace_id=marketplace_id,
            adult_product=adult_product,
            autographed=autographed,
            brand=brand,
            browse_classification=browse_classification,
            color=color,
            contributors=contributors,
            item_classification=item_classification,
            item_name=item_name,
            manufacturer=manufacturer,
            memorabilia=memorabilia,
            model_number=model_number,
            package_quantity=package_quantity,
            part_number=part_number,
            release_date=release_date,
            size=size,
            style=style,
            trade_in_eligible=trade_in_eligible,
            website_display_group=website_display_group,
            website_display_group_name=website_display_group_name,
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
