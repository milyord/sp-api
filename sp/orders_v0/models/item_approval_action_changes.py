from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_identifier import ItemIdentifier
    from ..models.money import Money


T = TypeVar("T", bound="ItemApprovalActionChanges")


@attr.s(auto_attribs=True)
class ItemApprovalActionChanges:
    r"""Changes required for the approval. Each approval type defines the allowed changes valid sub-set in its specific
    schema.

        Attributes:
            item_price (Union[Unset, Money]): The monetary value of the order.
            quantity (Union[Unset, int]): Quantity approved. If substitutedBy is specified, this value applies to the
                substitution item.
            substituted_by (Union[Unset, ItemIdentifier]): Item identifiers used in the context of approvals operations.
    """

    item_price: Union[Unset, "Money"] = UNSET
    quantity: Union[Unset, int] = UNSET
    substituted_by: Union[Unset, "ItemIdentifier"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_price, Unset):
            item_price = self.item_price.to_dict()

        quantity = self.quantity
        substituted_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.substituted_by, Unset):
            substituted_by = self.substituted_by.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_price is not UNSET:
            field_dict["ItemPrice"] = item_price
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if substituted_by is not UNSET:
            field_dict["SubstitutedBy"] = substituted_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_identifier import ItemIdentifier
        from ..models.money import Money

        d = src_dict.copy()
        _item_price = d.pop("ItemPrice", UNSET)
        item_price: Union[Unset, Money]
        if isinstance(_item_price, Unset):
            item_price = UNSET
        else:
            item_price = Money.from_dict(_item_price)

        quantity = d.pop("Quantity", UNSET)

        _substituted_by = d.pop("SubstitutedBy", UNSET)
        substituted_by: Union[Unset, ItemIdentifier]
        if isinstance(_substituted_by, Unset):
            substituted_by = UNSET
        else:
            substituted_by = ItemIdentifier.from_dict(_substituted_by)

        result = cls(
            item_price=item_price,
            quantity=quantity,
            substituted_by=substituted_by,
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
