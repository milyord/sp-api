from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemSummaryByMarketplace")


@attr.s(auto_attribs=True)
class ItemSummaryByMarketplace:
    r"""Summary details of an Amazon catalog item for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        brand_name (Union[Unset, str]): Name of the brand associated with an Amazon catalog item.
        browse_node (Union[Unset, str]): Identifier of the browse node associated with an Amazon catalog item.
        color_name (Union[Unset, str]): Name of the color associated with an Amazon catalog item.
        item_name (Union[Unset, str]): Name, or title, associated with an Amazon catalog item.
        manufacturer (Union[Unset, str]): Name of the manufacturer associated with an Amazon catalog item.
        model_number (Union[Unset, str]): Model number associated with an Amazon catalog item.
        size_name (Union[Unset, str]): Name of the size associated with an Amazon catalog item.
        style_name (Union[Unset, str]): Name of the style associated with an Amazon catalog item.
    """

    marketplace_id: str
    brand_name: Union[Unset, str] = UNSET
    browse_node: Union[Unset, str] = UNSET
    color_name: Union[Unset, str] = UNSET
    item_name: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    model_number: Union[Unset, str] = UNSET
    size_name: Union[Unset, str] = UNSET
    style_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        brand_name = self.brand_name
        browse_node = self.browse_node
        color_name = self.color_name
        item_name = self.item_name
        manufacturer = self.manufacturer
        model_number = self.model_number
        size_name = self.size_name
        style_name = self.style_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
            }
        )
        if brand_name is not UNSET:
            field_dict["brandName"] = brand_name
        if browse_node is not UNSET:
            field_dict["browseNode"] = browse_node
        if color_name is not UNSET:
            field_dict["colorName"] = color_name
        if item_name is not UNSET:
            field_dict["itemName"] = item_name
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model_number is not UNSET:
            field_dict["modelNumber"] = model_number
        if size_name is not UNSET:
            field_dict["sizeName"] = size_name
        if style_name is not UNSET:
            field_dict["styleName"] = style_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        brand_name = d.pop("brandName", UNSET)

        browse_node = d.pop("browseNode", UNSET)

        color_name = d.pop("colorName", UNSET)

        item_name = d.pop("itemName", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        model_number = d.pop("modelNumber", UNSET)

        size_name = d.pop("sizeName", UNSET)

        style_name = d.pop("styleName", UNSET)

        result = cls(
            marketplace_id=marketplace_id,
            brand_name=brand_name,
            browse_node=browse_node,
            color_name=color_name,
            item_name=item_name,
            manufacturer=manufacturer,
            model_number=model_number,
            size_name=size_name,
            style_name=style_name,
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
