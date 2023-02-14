import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_delivery_promise import ItemDeliveryPromise


T = TypeVar("T", bound="ItemDelivery")


@attr.s(auto_attribs=True)
class ItemDelivery:
    r"""Delivery information for the item.

    Attributes:
        estimated_delivery_date (Union[Unset, datetime.datetime]): The date and time of the latest Estimated Delivery
            Date (EDD) of all the items with an EDD. In ISO 8601 format.
        item_delivery_promise (Union[Unset, ItemDeliveryPromise]): Promised delivery information for the item.
    """

    estimated_delivery_date: Union[Unset, datetime.datetime] = UNSET
    item_delivery_promise: Union[Unset, "ItemDeliveryPromise"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        estimated_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_delivery_date, Unset):
            estimated_delivery_date = self.estimated_delivery_date.isoformat()

        item_delivery_promise: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_delivery_promise, Unset):
            item_delivery_promise = self.item_delivery_promise.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if estimated_delivery_date is not UNSET:
            field_dict["estimatedDeliveryDate"] = estimated_delivery_date
        if item_delivery_promise is not UNSET:
            field_dict["itemDeliveryPromise"] = item_delivery_promise

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_delivery_promise import ItemDeliveryPromise

        d = src_dict.copy()
        _estimated_delivery_date = d.pop("estimatedDeliveryDate", UNSET)
        estimated_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_delivery_date, Unset):
            estimated_delivery_date = UNSET
        else:
            estimated_delivery_date = isoparse(_estimated_delivery_date)

        _item_delivery_promise = d.pop("itemDeliveryPromise", UNSET)
        item_delivery_promise: Union[Unset, ItemDeliveryPromise]
        if isinstance(_item_delivery_promise, Unset):
            item_delivery_promise = UNSET
        else:
            item_delivery_promise = ItemDeliveryPromise.from_dict(_item_delivery_promise)

        result = cls(
            estimated_delivery_date=estimated_delivery_date,
            item_delivery_promise=item_delivery_promise,
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
