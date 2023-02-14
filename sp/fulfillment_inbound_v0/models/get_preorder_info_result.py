import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPreorderInfoResult")


@attr.s(auto_attribs=True)
class GetPreorderInfoResult:
    r"""
    Attributes:
        shipment_contains_preorderable_items (Union[Unset, bool]): Indicates whether the shipment contains items that
            have been enabled for pre-order. For more information about enabling items for pre-order, see the Seller Central
            Help.
        shipment_confirmed_for_preorder (Union[Unset, bool]): Indicates whether this shipment has been confirmed for
            pre-order.
        need_by_date (Union[Unset, datetime.date]):
        confirmed_fulfillable_date (Union[Unset, datetime.date]):
    """

    shipment_contains_preorderable_items: Union[Unset, bool] = UNSET
    shipment_confirmed_for_preorder: Union[Unset, bool] = UNSET
    need_by_date: Union[Unset, datetime.date] = UNSET
    confirmed_fulfillable_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_contains_preorderable_items = self.shipment_contains_preorderable_items
        shipment_confirmed_for_preorder = self.shipment_confirmed_for_preorder
        need_by_date: Union[Unset, str] = UNSET
        if not isinstance(self.need_by_date, Unset):
            need_by_date = self.need_by_date.isoformat()

        confirmed_fulfillable_date: Union[Unset, str] = UNSET
        if not isinstance(self.confirmed_fulfillable_date, Unset):
            confirmed_fulfillable_date = self.confirmed_fulfillable_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment_contains_preorderable_items is not UNSET:
            field_dict["ShipmentContainsPreorderableItems"] = shipment_contains_preorderable_items
        if shipment_confirmed_for_preorder is not UNSET:
            field_dict["ShipmentConfirmedForPreorder"] = shipment_confirmed_for_preorder
        if need_by_date is not UNSET:
            field_dict["NeedByDate"] = need_by_date
        if confirmed_fulfillable_date is not UNSET:
            field_dict["ConfirmedFulfillableDate"] = confirmed_fulfillable_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        shipment_contains_preorderable_items = d.pop("ShipmentContainsPreorderableItems", UNSET)

        shipment_confirmed_for_preorder = d.pop("ShipmentConfirmedForPreorder", UNSET)

        _need_by_date = d.pop("NeedByDate", UNSET)
        need_by_date: Union[Unset, datetime.date]
        if isinstance(_need_by_date, Unset):
            need_by_date = UNSET
        else:
            need_by_date = isoparse(_need_by_date).date()

        _confirmed_fulfillable_date = d.pop("ConfirmedFulfillableDate", UNSET)
        confirmed_fulfillable_date: Union[Unset, datetime.date]
        if isinstance(_confirmed_fulfillable_date, Unset):
            confirmed_fulfillable_date = UNSET
        else:
            confirmed_fulfillable_date = isoparse(_confirmed_fulfillable_date).date()

        result = cls(
            shipment_contains_preorderable_items=shipment_contains_preorderable_items,
            shipment_confirmed_for_preorder=shipment_confirmed_for_preorder,
            need_by_date=need_by_date,
            confirmed_fulfillable_date=confirmed_fulfillable_date,
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
