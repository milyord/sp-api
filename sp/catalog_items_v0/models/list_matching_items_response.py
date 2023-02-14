from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item import Item


T = TypeVar("T", bound="ListMatchingItemsResponse")


@attr.s(auto_attribs=True)
class ListMatchingItemsResponse:
    r"""
    Attributes:
        items (Union[Unset, List['Item']]): A list of items.
    """

    items: Union[Unset, List["Item"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for componentsschemas_item_list_item_data in self.items:
                componentsschemas_item_list_item = componentsschemas_item_list_item_data.to_dict()

                items.append(componentsschemas_item_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item import Item

        d = src_dict.copy()
        items = []
        _items = d.pop("Items", UNSET)
        for componentsschemas_item_list_item_data in _items or []:
            componentsschemas_item_list_item = Item.from_dict(componentsschemas_item_list_item_data)

            items.append(componentsschemas_item_list_item)

        result = cls(
            items=items,
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
