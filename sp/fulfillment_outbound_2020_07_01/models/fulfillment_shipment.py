import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.fulfillment_shipment_fulfillment_shipment_status import FulfillmentShipmentFulfillmentShipmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fulfillment_shipment_item import FulfillmentShipmentItem
    from ..models.fulfillment_shipment_package import FulfillmentShipmentPackage


T = TypeVar("T", bound="FulfillmentShipment")


@attr.s(auto_attribs=True)
class FulfillmentShipment:
    r"""Delivery and item information for a shipment in a fulfillment order.

    Attributes:
        amazon_shipment_id (str): A shipment identifier assigned by Amazon.
        fulfillment_center_id (str): An identifier for the fulfillment center that the shipment will be sent from.
        fulfillment_shipment_status (FulfillmentShipmentFulfillmentShipmentStatus): The current status of the shipment.
        fulfillment_shipment_item (List['FulfillmentShipmentItem']): An array of fulfillment shipment item information.
        shipping_date (Union[Unset, datetime.datetime]):
        estimated_arrival_date (Union[Unset, datetime.datetime]):
        shipping_notes (Union[Unset, List[str]]): Provides additional insight into shipment timeline. Primairly used to
            communicate that actual delivery dates aren't available.
        fulfillment_shipment_package (Union[Unset, List['FulfillmentShipmentPackage']]): An array of fulfillment
            shipment package information.
    """

    amazon_shipment_id: str
    fulfillment_center_id: str
    fulfillment_shipment_status: FulfillmentShipmentFulfillmentShipmentStatus
    fulfillment_shipment_item: List["FulfillmentShipmentItem"]
    shipping_date: Union[Unset, datetime.datetime] = UNSET
    estimated_arrival_date: Union[Unset, datetime.datetime] = UNSET
    shipping_notes: Union[Unset, List[str]] = UNSET
    fulfillment_shipment_package: Union[Unset, List["FulfillmentShipmentPackage"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_shipment_id = self.amazon_shipment_id
        fulfillment_center_id = self.fulfillment_center_id
        fulfillment_shipment_status = self.fulfillment_shipment_status.value

        fulfillment_shipment_item = []
        for componentsschemas_fulfillment_shipment_item_list_item_data in self.fulfillment_shipment_item:
            componentsschemas_fulfillment_shipment_item_list_item = (
                componentsschemas_fulfillment_shipment_item_list_item_data.to_dict()
            )

            fulfillment_shipment_item.append(componentsschemas_fulfillment_shipment_item_list_item)

        shipping_date: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_date, Unset):
            shipping_date = self.shipping_date.isoformat()

        estimated_arrival_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_arrival_date, Unset):
            estimated_arrival_date = self.estimated_arrival_date.isoformat()

        shipping_notes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.shipping_notes, Unset):
            shipping_notes = self.shipping_notes

        fulfillment_shipment_package: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulfillment_shipment_package, Unset):
            fulfillment_shipment_package = []
            for componentsschemas_fulfillment_shipment_package_list_item_data in self.fulfillment_shipment_package:
                componentsschemas_fulfillment_shipment_package_list_item = (
                    componentsschemas_fulfillment_shipment_package_list_item_data.to_dict()
                )

                fulfillment_shipment_package.append(componentsschemas_fulfillment_shipment_package_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amazonShipmentId": amazon_shipment_id,
                "fulfillmentCenterId": fulfillment_center_id,
                "fulfillmentShipmentStatus": fulfillment_shipment_status,
                "fulfillmentShipmentItem": fulfillment_shipment_item,
            }
        )
        if shipping_date is not UNSET:
            field_dict["shippingDate"] = shipping_date
        if estimated_arrival_date is not UNSET:
            field_dict["estimatedArrivalDate"] = estimated_arrival_date
        if shipping_notes is not UNSET:
            field_dict["shippingNotes"] = shipping_notes
        if fulfillment_shipment_package is not UNSET:
            field_dict["fulfillmentShipmentPackage"] = fulfillment_shipment_package

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fulfillment_shipment_item import FulfillmentShipmentItem
        from ..models.fulfillment_shipment_package import FulfillmentShipmentPackage

        d = src_dict.copy()
        amazon_shipment_id = d.pop("amazonShipmentId")

        fulfillment_center_id = d.pop("fulfillmentCenterId")

        fulfillment_shipment_status = FulfillmentShipmentFulfillmentShipmentStatus(d.pop("fulfillmentShipmentStatus"))

        fulfillment_shipment_item = []
        _fulfillment_shipment_item = d.pop("fulfillmentShipmentItem")
        for componentsschemas_fulfillment_shipment_item_list_item_data in _fulfillment_shipment_item:
            componentsschemas_fulfillment_shipment_item_list_item = FulfillmentShipmentItem.from_dict(
                componentsschemas_fulfillment_shipment_item_list_item_data
            )

            fulfillment_shipment_item.append(componentsschemas_fulfillment_shipment_item_list_item)

        _shipping_date = d.pop("shippingDate", UNSET)
        shipping_date: Union[Unset, datetime.datetime]
        if isinstance(_shipping_date, Unset):
            shipping_date = UNSET
        else:
            shipping_date = isoparse(_shipping_date)

        _estimated_arrival_date = d.pop("estimatedArrivalDate", UNSET)
        estimated_arrival_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_arrival_date, Unset):
            estimated_arrival_date = UNSET
        else:
            estimated_arrival_date = isoparse(_estimated_arrival_date)

        shipping_notes = cast(List[str], d.pop("shippingNotes", UNSET))

        fulfillment_shipment_package = []
        _fulfillment_shipment_package = d.pop("fulfillmentShipmentPackage", UNSET)
        for componentsschemas_fulfillment_shipment_package_list_item_data in _fulfillment_shipment_package or []:
            componentsschemas_fulfillment_shipment_package_list_item = FulfillmentShipmentPackage.from_dict(
                componentsschemas_fulfillment_shipment_package_list_item_data
            )

            fulfillment_shipment_package.append(componentsschemas_fulfillment_shipment_package_list_item)

        result = cls(
            amazon_shipment_id=amazon_shipment_id,
            fulfillment_center_id=fulfillment_center_id,
            fulfillment_shipment_status=fulfillment_shipment_status,
            fulfillment_shipment_item=fulfillment_shipment_item,
            shipping_date=shipping_date,
            estimated_arrival_date=estimated_arrival_date,
            shipping_notes=shipping_notes,
            fulfillment_shipment_package=fulfillment_shipment_package,
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
