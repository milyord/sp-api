import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fulfillment_preview_item import FulfillmentPreviewItem


T = TypeVar("T", bound="FulfillmentPreviewShipment")


@attr.s(auto_attribs=True)
class FulfillmentPreviewShipment:
    r"""Delivery and item information for a shipment in a fulfillment order preview.

    Attributes:
        fulfillment_preview_items (List['FulfillmentPreviewItem']): An array of fulfillment preview item information.
        earliest_ship_date (Union[Unset, datetime.datetime]):
        latest_ship_date (Union[Unset, datetime.datetime]):
        earliest_arrival_date (Union[Unset, datetime.datetime]):
        latest_arrival_date (Union[Unset, datetime.datetime]):
        shipping_notes (Union[Unset, List[str]]): Provides additional insight into the shipment timeline when exact
            delivery dates are not able to be precomputed.
    """

    fulfillment_preview_items: List["FulfillmentPreviewItem"]
    earliest_ship_date: Union[Unset, datetime.datetime] = UNSET
    latest_ship_date: Union[Unset, datetime.datetime] = UNSET
    earliest_arrival_date: Union[Unset, datetime.datetime] = UNSET
    latest_arrival_date: Union[Unset, datetime.datetime] = UNSET
    shipping_notes: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fulfillment_preview_items = []
        for componentsschemas_fulfillment_preview_item_list_item_data in self.fulfillment_preview_items:
            componentsschemas_fulfillment_preview_item_list_item = (
                componentsschemas_fulfillment_preview_item_list_item_data.to_dict()
            )

            fulfillment_preview_items.append(componentsschemas_fulfillment_preview_item_list_item)

        earliest_ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.earliest_ship_date, Unset):
            earliest_ship_date = self.earliest_ship_date.isoformat()

        latest_ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_ship_date, Unset):
            latest_ship_date = self.latest_ship_date.isoformat()

        earliest_arrival_date: Union[Unset, str] = UNSET
        if not isinstance(self.earliest_arrival_date, Unset):
            earliest_arrival_date = self.earliest_arrival_date.isoformat()

        latest_arrival_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_arrival_date, Unset):
            latest_arrival_date = self.latest_arrival_date.isoformat()

        shipping_notes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.shipping_notes, Unset):
            shipping_notes = self.shipping_notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fulfillmentPreviewItems": fulfillment_preview_items,
            }
        )
        if earliest_ship_date is not UNSET:
            field_dict["earliestShipDate"] = earliest_ship_date
        if latest_ship_date is not UNSET:
            field_dict["latestShipDate"] = latest_ship_date
        if earliest_arrival_date is not UNSET:
            field_dict["earliestArrivalDate"] = earliest_arrival_date
        if latest_arrival_date is not UNSET:
            field_dict["latestArrivalDate"] = latest_arrival_date
        if shipping_notes is not UNSET:
            field_dict["shippingNotes"] = shipping_notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fulfillment_preview_item import FulfillmentPreviewItem

        d = src_dict.copy()
        fulfillment_preview_items = []
        _fulfillment_preview_items = d.pop("fulfillmentPreviewItems")
        for componentsschemas_fulfillment_preview_item_list_item_data in _fulfillment_preview_items:
            componentsschemas_fulfillment_preview_item_list_item = FulfillmentPreviewItem.from_dict(
                componentsschemas_fulfillment_preview_item_list_item_data
            )

            fulfillment_preview_items.append(componentsschemas_fulfillment_preview_item_list_item)

        _earliest_ship_date = d.pop("earliestShipDate", UNSET)
        earliest_ship_date: Union[Unset, datetime.datetime]
        if isinstance(_earliest_ship_date, Unset):
            earliest_ship_date = UNSET
        else:
            earliest_ship_date = isoparse(_earliest_ship_date)

        _latest_ship_date = d.pop("latestShipDate", UNSET)
        latest_ship_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_ship_date, Unset):
            latest_ship_date = UNSET
        else:
            latest_ship_date = isoparse(_latest_ship_date)

        _earliest_arrival_date = d.pop("earliestArrivalDate", UNSET)
        earliest_arrival_date: Union[Unset, datetime.datetime]
        if isinstance(_earliest_arrival_date, Unset):
            earliest_arrival_date = UNSET
        else:
            earliest_arrival_date = isoparse(_earliest_arrival_date)

        _latest_arrival_date = d.pop("latestArrivalDate", UNSET)
        latest_arrival_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_arrival_date, Unset):
            latest_arrival_date = UNSET
        else:
            latest_arrival_date = isoparse(_latest_arrival_date)

        shipping_notes = cast(List[str], d.pop("shippingNotes", UNSET))

        result = cls(
            fulfillment_preview_items=fulfillment_preview_items,
            earliest_ship_date=earliest_ship_date,
            latest_ship_date=latest_ship_date,
            earliest_arrival_date=earliest_arrival_date,
            latest_arrival_date=latest_arrival_date,
            shipping_notes=shipping_notes,
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
