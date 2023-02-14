from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_details import ItemDetails
    from ..models.item_quantity import ItemQuantity


T = TypeVar("T", bound="Item")


@attr.s(auto_attribs=True)
class Item:
    r"""Details of the item being shipped.

    Attributes:
        item_sequence_number (str): Item sequence number for the item. The first item will be 001, the second 002, and
            so on. This number is used as a reference to refer to this item from the carton or pallet level.
        shipped_quantity (ItemQuantity): Details of item quantity.
        amazon_product_identifier (Union[Unset, str]): Amazon Standard Identification Number (ASIN) of an item.
        vendor_product_identifier (Union[Unset, str]): The vendor selected product identification of the item. Should be
            the same as was sent in the purchase order.
        item_details (Union[Unset, ItemDetails]): Item details for be provided for every item in shipment at either the
            item or carton or pallet level, whichever is appropriate.
    """

    item_sequence_number: str
    shipped_quantity: "ItemQuantity"
    amazon_product_identifier: Union[Unset, str] = UNSET
    vendor_product_identifier: Union[Unset, str] = UNSET
    item_details: Union[Unset, "ItemDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_sequence_number = self.item_sequence_number
        shipped_quantity = self.shipped_quantity.to_dict()

        amazon_product_identifier = self.amazon_product_identifier
        vendor_product_identifier = self.vendor_product_identifier
        item_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_details, Unset):
            item_details = self.item_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemSequenceNumber": item_sequence_number,
                "shippedQuantity": shipped_quantity,
            }
        )
        if amazon_product_identifier is not UNSET:
            field_dict["amazonProductIdentifier"] = amazon_product_identifier
        if vendor_product_identifier is not UNSET:
            field_dict["vendorProductIdentifier"] = vendor_product_identifier
        if item_details is not UNSET:
            field_dict["itemDetails"] = item_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_details import ItemDetails
        from ..models.item_quantity import ItemQuantity

        d = src_dict.copy()
        item_sequence_number = d.pop("itemSequenceNumber")

        shipped_quantity = ItemQuantity.from_dict(d.pop("shippedQuantity"))

        amazon_product_identifier = d.pop("amazonProductIdentifier", UNSET)

        vendor_product_identifier = d.pop("vendorProductIdentifier", UNSET)

        _item_details = d.pop("itemDetails", UNSET)
        item_details: Union[Unset, ItemDetails]
        if isinstance(_item_details, Unset):
            item_details = UNSET
        else:
            item_details = ItemDetails.from_dict(_item_details)

        result = cls(
            item_sequence_number=item_sequence_number,
            shipped_quantity=shipped_quantity,
            amazon_product_identifier=amazon_product_identifier,
            vendor_product_identifier=vendor_product_identifier,
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
