from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_quantity import ItemQuantity


T = TypeVar("T", bound="PackedItem")


@attr.s(auto_attribs=True)
class PackedItem:
    r"""
    Attributes:
        item_sequence_number (int): Item Sequence Number for the item. This must be the same value as sent in the order
            for a given item.
        packed_quantity (ItemQuantity): Details of item quantity.
        buyer_product_identifier (Union[Unset, str]): Buyer's Standard Identification Number (ASIN) of an item. Either
            buyerProductIdentifier or vendorProductIdentifier is required.
        vendor_product_identifier (Union[Unset, str]): The vendor selected product identification of the item. Should be
            the same as was sent in the Purchase Order, like SKU Number.
    """

    item_sequence_number: int
    packed_quantity: "ItemQuantity"
    buyer_product_identifier: Union[Unset, str] = UNSET
    vendor_product_identifier: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_sequence_number = self.item_sequence_number
        packed_quantity = self.packed_quantity.to_dict()

        buyer_product_identifier = self.buyer_product_identifier
        vendor_product_identifier = self.vendor_product_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemSequenceNumber": item_sequence_number,
                "packedQuantity": packed_quantity,
            }
        )
        if buyer_product_identifier is not UNSET:
            field_dict["buyerProductIdentifier"] = buyer_product_identifier
        if vendor_product_identifier is not UNSET:
            field_dict["vendorProductIdentifier"] = vendor_product_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_quantity import ItemQuantity

        d = src_dict.copy()
        item_sequence_number = d.pop("itemSequenceNumber")

        packed_quantity = ItemQuantity.from_dict(d.pop("packedQuantity"))

        buyer_product_identifier = d.pop("buyerProductIdentifier", UNSET)

        vendor_product_identifier = d.pop("vendorProductIdentifier", UNSET)

        result = cls(
            item_sequence_number=item_sequence_number,
            packed_quantity=packed_quantity,
            buyer_product_identifier=buyer_product_identifier,
            vendor_product_identifier=vendor_product_identifier,
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
