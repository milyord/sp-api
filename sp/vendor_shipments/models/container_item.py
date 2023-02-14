from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_details import ItemDetails
    from ..models.item_quantity import ItemQuantity


T = TypeVar("T", bound="ContainerItem")


@attr.s(auto_attribs=True)
class ContainerItem:
    r"""Carton/Pallet level details for the item.

    Attributes:
        item_reference (str): The reference number for the item. Please provide the itemSequenceNumber from the 'items'
            segment to refer to that item's details here.
        shipped_quantity (ItemQuantity): Details of item quantity.
        item_details (Union[Unset, ItemDetails]): Item details for be provided for every item in shipment at either the
            item or carton or pallet level, whichever is appropriate.
    """

    item_reference: str
    shipped_quantity: "ItemQuantity"
    item_details: Union[Unset, "ItemDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_reference = self.item_reference
        shipped_quantity = self.shipped_quantity.to_dict()

        item_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_details, Unset):
            item_details = self.item_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemReference": item_reference,
                "shippedQuantity": shipped_quantity,
            }
        )
        if item_details is not UNSET:
            field_dict["itemDetails"] = item_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_details import ItemDetails
        from ..models.item_quantity import ItemQuantity

        d = src_dict.copy()
        item_reference = d.pop("itemReference")

        shipped_quantity = ItemQuantity.from_dict(d.pop("shippedQuantity"))

        _item_details = d.pop("itemDetails", UNSET)
        item_details: Union[Unset, ItemDetails]
        if isinstance(_item_details, Unset):
            item_details = UNSET
        else:
            item_details = ItemDetails.from_dict(_item_details)

        result = cls(
            item_reference=item_reference,
            shipped_quantity=shipped_quantity,
            item_details=item_details,
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
