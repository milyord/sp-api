from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_quantity import ItemQuantity


T = TypeVar("T", bound="ItemDetails")


@attr.s(auto_attribs=True)
class ItemDetails:
    r"""Updated inventory details for an item.

    Attributes:
        available_quantity (ItemQuantity): Details of item quantity.
        buyer_product_identifier (Union[Unset, str]): The buyer selected product identification of the item. Either
            buyerProductIdentifier or vendorProductIdentifier should be submitted.
        vendor_product_identifier (Union[Unset, str]): The vendor selected product identification of the item. Either
            buyerProductIdentifier or vendorProductIdentifier should be submitted.
        is_obsolete (Union[Unset, bool]): When true, the item is permanently unavailable.
    """

    available_quantity: "ItemQuantity"
    buyer_product_identifier: Union[Unset, str] = UNSET
    vendor_product_identifier: Union[Unset, str] = UNSET
    is_obsolete: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_quantity = self.available_quantity.to_dict()

        buyer_product_identifier = self.buyer_product_identifier
        vendor_product_identifier = self.vendor_product_identifier
        is_obsolete = self.is_obsolete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availableQuantity": available_quantity,
            }
        )
        if buyer_product_identifier is not UNSET:
            field_dict["buyerProductIdentifier"] = buyer_product_identifier
        if vendor_product_identifier is not UNSET:
            field_dict["vendorProductIdentifier"] = vendor_product_identifier
        if is_obsolete is not UNSET:
            field_dict["isObsolete"] = is_obsolete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_quantity import ItemQuantity

        d = src_dict.copy()
        available_quantity = ItemQuantity.from_dict(d.pop("availableQuantity"))

        buyer_product_identifier = d.pop("buyerProductIdentifier", UNSET)

        vendor_product_identifier = d.pop("vendorProductIdentifier", UNSET)

        is_obsolete = d.pop("isObsolete", UNSET)

        result = cls(
            available_quantity=available_quantity,
            buyer_product_identifier=buyer_product_identifier,
            vendor_product_identifier=vendor_product_identifier,
            is_obsolete=is_obsolete,
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
