from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_quantity import ItemQuantity
    from ..models.ordered_quantity_details import OrderedQuantityDetails


T = TypeVar("T", bound="OrderItemStatusOrderedQuantity")


@attr.s(auto_attribs=True)
class OrderItemStatusOrderedQuantity:
    r"""Ordered quantity information.

    Attributes:
        ordered_quantity (Union[Unset, ItemQuantity]): Details of quantity ordered.
        ordered_quantity_details (Union[Unset, List['OrderedQuantityDetails']]): Details of item quantity ordered.
    """

    ordered_quantity: Union[Unset, "ItemQuantity"] = UNSET
    ordered_quantity_details: Union[Unset, List["OrderedQuantityDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ordered_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ordered_quantity, Unset):
            ordered_quantity = self.ordered_quantity.to_dict()

        ordered_quantity_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ordered_quantity_details, Unset):
            ordered_quantity_details = []
            for ordered_quantity_details_item_data in self.ordered_quantity_details:
                ordered_quantity_details_item = ordered_quantity_details_item_data.to_dict()

                ordered_quantity_details.append(ordered_quantity_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordered_quantity is not UNSET:
            field_dict["orderedQuantity"] = ordered_quantity
        if ordered_quantity_details is not UNSET:
            field_dict["orderedQuantityDetails"] = ordered_quantity_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_quantity import ItemQuantity
        from ..models.ordered_quantity_details import OrderedQuantityDetails

        d = src_dict.copy()
        _ordered_quantity = d.pop("orderedQuantity", UNSET)
        ordered_quantity: Union[Unset, ItemQuantity]
        if isinstance(_ordered_quantity, Unset):
            ordered_quantity = UNSET
        else:
            ordered_quantity = ItemQuantity.from_dict(_ordered_quantity)

        ordered_quantity_details = []
        _ordered_quantity_details = d.pop("orderedQuantityDetails", UNSET)
        for ordered_quantity_details_item_data in _ordered_quantity_details or []:
            ordered_quantity_details_item = OrderedQuantityDetails.from_dict(ordered_quantity_details_item_data)

            ordered_quantity_details.append(ordered_quantity_details_item)

        result = cls(
            ordered_quantity=ordered_quantity,
            ordered_quantity_details=ordered_quantity_details,
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
