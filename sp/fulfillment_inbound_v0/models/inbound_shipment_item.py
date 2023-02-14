import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prep_details import PrepDetails


T = TypeVar("T", bound="InboundShipmentItem")


@attr.s(auto_attribs=True)
class InboundShipmentItem:
    r"""Item information for an inbound shipment. Submitted with a call to the createInboundShipment or
    updateInboundShipment operation.

        Attributes:
            seller_sku (str): The seller SKU of the item.
            quantity_shipped (int): The item quantity.
            shipment_id (Union[Unset, str]): A shipment identifier originally returned by the createInboundShipmentPlan
                operation.
            fulfillment_network_sku (Union[Unset, str]): Amazon's fulfillment network SKU of the item.
            quantity_received (Union[Unset, int]): The item quantity.
            quantity_in_case (Union[Unset, int]): The item quantity.
            release_date (Union[Unset, datetime.date]):
            prep_details_list (Union[Unset, List['PrepDetails']]): A list of preparation instructions and who is responsible
                for that preparation.
    """

    seller_sku: str
    quantity_shipped: int
    shipment_id: Union[Unset, str] = UNSET
    fulfillment_network_sku: Union[Unset, str] = UNSET
    quantity_received: Union[Unset, int] = UNSET
    quantity_in_case: Union[Unset, int] = UNSET
    release_date: Union[Unset, datetime.date] = UNSET
    prep_details_list: Union[Unset, List["PrepDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        quantity_shipped = self.quantity_shipped
        shipment_id = self.shipment_id
        fulfillment_network_sku = self.fulfillment_network_sku
        quantity_received = self.quantity_received
        quantity_in_case = self.quantity_in_case
        release_date: Union[Unset, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        prep_details_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.prep_details_list, Unset):
            prep_details_list = []
            for componentsschemas_prep_details_list_item_data in self.prep_details_list:
                componentsschemas_prep_details_list_item = componentsschemas_prep_details_list_item_data.to_dict()

                prep_details_list.append(componentsschemas_prep_details_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SellerSKU": seller_sku,
                "QuantityShipped": quantity_shipped,
            }
        )
        if shipment_id is not UNSET:
            field_dict["ShipmentId"] = shipment_id
        if fulfillment_network_sku is not UNSET:
            field_dict["FulfillmentNetworkSKU"] = fulfillment_network_sku
        if quantity_received is not UNSET:
            field_dict["QuantityReceived"] = quantity_received
        if quantity_in_case is not UNSET:
            field_dict["QuantityInCase"] = quantity_in_case
        if release_date is not UNSET:
            field_dict["ReleaseDate"] = release_date
        if prep_details_list is not UNSET:
            field_dict["PrepDetailsList"] = prep_details_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.prep_details import PrepDetails

        d = src_dict.copy()
        seller_sku = d.pop("SellerSKU")

        quantity_shipped = d.pop("QuantityShipped")

        shipment_id = d.pop("ShipmentId", UNSET)

        fulfillment_network_sku = d.pop("FulfillmentNetworkSKU", UNSET)

        quantity_received = d.pop("QuantityReceived", UNSET)

        quantity_in_case = d.pop("QuantityInCase", UNSET)

        _release_date = d.pop("ReleaseDate", UNSET)
        release_date: Union[Unset, datetime.date]
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        prep_details_list = []
        _prep_details_list = d.pop("PrepDetailsList", UNSET)
        for componentsschemas_prep_details_list_item_data in _prep_details_list or []:
            componentsschemas_prep_details_list_item = PrepDetails.from_dict(
                componentsschemas_prep_details_list_item_data
            )

            prep_details_list.append(componentsschemas_prep_details_list_item)

        result = cls(
            seller_sku=seller_sku,
            quantity_shipped=quantity_shipped,
            shipment_id=shipment_id,
            fulfillment_network_sku=fulfillment_network_sku,
            quantity_received=quantity_received,
            quantity_in_case=quantity_in_case,
            release_date=release_date,
            prep_details_list=prep_details_list,
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
