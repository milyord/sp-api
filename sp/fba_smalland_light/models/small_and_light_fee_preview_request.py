from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.item import Item


T = TypeVar("T", bound="SmallAndLightFeePreviewRequest")


@attr.s(auto_attribs=True)
class SmallAndLightFeePreviewRequest:
    r"""Request schema for submitting items for which to retrieve fee estimates.

    Attributes:
        marketplace_id (str): A marketplace identifier.
        items (List['Item']): A list of items for which to retrieve fee estimates (limit: 25).
    """

    marketplace_id: str
    items: List["Item"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item import Item

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Item.from_dict(items_item_data)

            items.append(items_item)

        result = cls(
            marketplace_id=marketplace_id,
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
