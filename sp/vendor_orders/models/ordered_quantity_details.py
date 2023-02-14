import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_quantity import ItemQuantity


T = TypeVar("T", bound="OrderedQuantityDetails")


@attr.s(auto_attribs=True)
class OrderedQuantityDetails:
    r"""Details of item quantity ordered

    Attributes:
        updated_date (Union[Unset, datetime.datetime]): The date when the line item quantity was updated by buyer. Must
            be in ISO-8601 date/time format.
        ordered_quantity (Union[Unset, ItemQuantity]): Details of quantity ordered.
        cancelled_quantity (Union[Unset, ItemQuantity]): Details of quantity ordered.
    """

    updated_date: Union[Unset, datetime.datetime] = UNSET
    ordered_quantity: Union[Unset, "ItemQuantity"] = UNSET
    cancelled_quantity: Union[Unset, "ItemQuantity"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.updated_date, Unset):
            updated_date = self.updated_date.isoformat()

        ordered_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ordered_quantity, Unset):
            ordered_quantity = self.ordered_quantity.to_dict()

        cancelled_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cancelled_quantity, Unset):
            cancelled_quantity = self.cancelled_quantity.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated_date is not UNSET:
            field_dict["updatedDate"] = updated_date
        if ordered_quantity is not UNSET:
            field_dict["orderedQuantity"] = ordered_quantity
        if cancelled_quantity is not UNSET:
            field_dict["cancelledQuantity"] = cancelled_quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_quantity import ItemQuantity

        d = src_dict.copy()
        _updated_date = d.pop("updatedDate", UNSET)
        updated_date: Union[Unset, datetime.datetime]
        if isinstance(_updated_date, Unset):
            updated_date = UNSET
        else:
            updated_date = isoparse(_updated_date)

        _ordered_quantity = d.pop("orderedQuantity", UNSET)
        ordered_quantity: Union[Unset, ItemQuantity]
        if isinstance(_ordered_quantity, Unset):
            ordered_quantity = UNSET
        else:
            ordered_quantity = ItemQuantity.from_dict(_ordered_quantity)

        _cancelled_quantity = d.pop("cancelledQuantity", UNSET)
        cancelled_quantity: Union[Unset, ItemQuantity]
        if isinstance(_cancelled_quantity, Unset):
            cancelled_quantity = UNSET
        else:
            cancelled_quantity = ItemQuantity.from_dict(_cancelled_quantity)

        result = cls(
            updated_date=updated_date,
            ordered_quantity=ordered_quantity,
            cancelled_quantity=cancelled_quantity,
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
