from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_acknowledgement_item import OrderAcknowledgementItem


T = TypeVar("T", bound="SubmitAcknowledgementRequest")


@attr.s(auto_attribs=True)
class SubmitAcknowledgementRequest:
    r"""The request schema for the submitAcknowledgement operation.

    Attributes:
        order_acknowledgements (Union[Unset, List['OrderAcknowledgementItem']]): A list of one or more purchase orders.
    """

    order_acknowledgements: Union[Unset, List["OrderAcknowledgementItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_acknowledgements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_acknowledgements, Unset):
            order_acknowledgements = []
            for order_acknowledgements_item_data in self.order_acknowledgements:
                order_acknowledgements_item = order_acknowledgements_item_data.to_dict()

                order_acknowledgements.append(order_acknowledgements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_acknowledgements is not UNSET:
            field_dict["orderAcknowledgements"] = order_acknowledgements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_acknowledgement_item import OrderAcknowledgementItem

        d = src_dict.copy()
        order_acknowledgements = []
        _order_acknowledgements = d.pop("orderAcknowledgements", UNSET)
        for order_acknowledgements_item_data in _order_acknowledgements or []:
            order_acknowledgements_item = OrderAcknowledgementItem.from_dict(order_acknowledgements_item_data)

            order_acknowledgements.append(order_acknowledgements_item)

        result = cls(
            order_acknowledgements=order_acknowledgements,
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
