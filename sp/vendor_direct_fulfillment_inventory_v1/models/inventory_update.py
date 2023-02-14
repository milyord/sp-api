from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.item_details import ItemDetails
    from ..models.party_identification import PartyIdentification


T = TypeVar("T", bound="InventoryUpdate")


@attr.s(auto_attribs=True)
class InventoryUpdate:
    r"""
    Attributes:
        selling_party (PartyIdentification):
        is_full_update (bool): When true, this request contains a full feed. Otherwise, this request contains a partial
            feed. When sending a full feed, you must send information about all items in the warehouse. Any items not in the
            full feed are updated as not available. When sending a partial feed, only include the items that need an update
            to inventory. The status of other items will remain unchanged.
        items (List['ItemDetails']): A list of inventory items with updated details, including quantity available.
    """

    selling_party: "PartyIdentification"
    is_full_update: bool
    items: List["ItemDetails"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        selling_party = self.selling_party.to_dict()

        is_full_update = self.is_full_update
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellingParty": selling_party,
                "isFullUpdate": is_full_update,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_details import ItemDetails
        from ..models.party_identification import PartyIdentification

        d = src_dict.copy()
        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        is_full_update = d.pop("isFullUpdate")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ItemDetails.from_dict(items_item_data)

            items.append(items_item)

        result = cls(
            selling_party=selling_party,
            is_full_update=is_full_update,
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
