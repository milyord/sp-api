import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.box_contents_source import BoxContentsSource
from ..models.label_prep_type import LabelPrepType
from ..models.shipment_status import ShipmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.box_contents_fee_details import BoxContentsFeeDetails


T = TypeVar("T", bound="InboundShipmentInfo")


@attr.s(auto_attribs=True)
class InboundShipmentInfo:
    r"""Information about the seller's inbound shipments. Returned by the listInboundShipments operation.

    Attributes:
        ship_from_address (Address):
        are_cases_required (bool): Indicates whether or not an inbound shipment contains case-packed boxes. When
            AreCasesRequired = true for an inbound shipment, all items in the inbound shipment must be case packed.
        shipment_id (Union[Unset, str]): The shipment identifier submitted in the request.
        shipment_name (Union[Unset, str]): The name for the inbound shipment.
        destination_fulfillment_center_id (Union[Unset, str]): An Amazon fulfillment center identifier created by
            Amazon.
        shipment_status (Union[Unset, ShipmentStatus]): Indicates the status of the inbound shipment. When used with the
            createInboundShipment operation, WORKING is the only valid value. When used with the updateInboundShipment
            operation, possible values are WORKING, SHIPPED or CANCELLED.
        label_prep_type (Union[Unset, LabelPrepType]): The type of label preparation that is required for the inbound
            shipment.
        confirmed_need_by_date (Union[Unset, datetime.date]):
        box_contents_source (Union[Unset, BoxContentsSource]): Where the seller provided box contents information for a
            shipment.
        estimated_box_contents_fee (Union[Unset, BoxContentsFeeDetails]): The manual processing fee per unit and total
            fee for a shipment.
    """

    ship_from_address: "Address"
    are_cases_required: bool
    shipment_id: Union[Unset, str] = UNSET
    shipment_name: Union[Unset, str] = UNSET
    destination_fulfillment_center_id: Union[Unset, str] = UNSET
    shipment_status: Union[Unset, ShipmentStatus] = UNSET
    label_prep_type: Union[Unset, LabelPrepType] = UNSET
    confirmed_need_by_date: Union[Unset, datetime.date] = UNSET
    box_contents_source: Union[Unset, BoxContentsSource] = UNSET
    estimated_box_contents_fee: Union[Unset, "BoxContentsFeeDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ship_from_address = self.ship_from_address.to_dict()

        are_cases_required = self.are_cases_required
        shipment_id = self.shipment_id
        shipment_name = self.shipment_name
        destination_fulfillment_center_id = self.destination_fulfillment_center_id
        shipment_status: Union[Unset, str] = UNSET
        if not isinstance(self.shipment_status, Unset):
            shipment_status = self.shipment_status.value

        label_prep_type: Union[Unset, str] = UNSET
        if not isinstance(self.label_prep_type, Unset):
            label_prep_type = self.label_prep_type.value

        confirmed_need_by_date: Union[Unset, str] = UNSET
        if not isinstance(self.confirmed_need_by_date, Unset):
            confirmed_need_by_date = self.confirmed_need_by_date.isoformat()

        box_contents_source: Union[Unset, str] = UNSET
        if not isinstance(self.box_contents_source, Unset):
            box_contents_source = self.box_contents_source.value

        estimated_box_contents_fee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimated_box_contents_fee, Unset):
            estimated_box_contents_fee = self.estimated_box_contents_fee.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShipFromAddress": ship_from_address,
                "AreCasesRequired": are_cases_required,
            }
        )
        if shipment_id is not UNSET:
            field_dict["ShipmentId"] = shipment_id
        if shipment_name is not UNSET:
            field_dict["ShipmentName"] = shipment_name
        if destination_fulfillment_center_id is not UNSET:
            field_dict["DestinationFulfillmentCenterId"] = destination_fulfillment_center_id
        if shipment_status is not UNSET:
            field_dict["ShipmentStatus"] = shipment_status
        if label_prep_type is not UNSET:
            field_dict["LabelPrepType"] = label_prep_type
        if confirmed_need_by_date is not UNSET:
            field_dict["ConfirmedNeedByDate"] = confirmed_need_by_date
        if box_contents_source is not UNSET:
            field_dict["BoxContentsSource"] = box_contents_source
        if estimated_box_contents_fee is not UNSET:
            field_dict["EstimatedBoxContentsFee"] = estimated_box_contents_fee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.box_contents_fee_details import BoxContentsFeeDetails

        d = src_dict.copy()
        ship_from_address = Address.from_dict(d.pop("ShipFromAddress"))

        are_cases_required = d.pop("AreCasesRequired")

        shipment_id = d.pop("ShipmentId", UNSET)

        shipment_name = d.pop("ShipmentName", UNSET)

        destination_fulfillment_center_id = d.pop("DestinationFulfillmentCenterId", UNSET)

        _shipment_status = d.pop("ShipmentStatus", UNSET)
        shipment_status: Union[Unset, ShipmentStatus]
        if isinstance(_shipment_status, Unset):
            shipment_status = UNSET
        else:
            shipment_status = ShipmentStatus(_shipment_status)

        _label_prep_type = d.pop("LabelPrepType", UNSET)
        label_prep_type: Union[Unset, LabelPrepType]
        if isinstance(_label_prep_type, Unset):
            label_prep_type = UNSET
        else:
            label_prep_type = LabelPrepType(_label_prep_type)

        _confirmed_need_by_date = d.pop("ConfirmedNeedByDate", UNSET)
        confirmed_need_by_date: Union[Unset, datetime.date]
        if isinstance(_confirmed_need_by_date, Unset):
            confirmed_need_by_date = UNSET
        else:
            confirmed_need_by_date = isoparse(_confirmed_need_by_date).date()

        _box_contents_source = d.pop("BoxContentsSource", UNSET)
        box_contents_source: Union[Unset, BoxContentsSource]
        if isinstance(_box_contents_source, Unset):
            box_contents_source = UNSET
        else:
            box_contents_source = BoxContentsSource(_box_contents_source)

        _estimated_box_contents_fee = d.pop("EstimatedBoxContentsFee", UNSET)
        estimated_box_contents_fee: Union[Unset, BoxContentsFeeDetails]
        if isinstance(_estimated_box_contents_fee, Unset):
            estimated_box_contents_fee = UNSET
        else:
            estimated_box_contents_fee = BoxContentsFeeDetails.from_dict(_estimated_box_contents_fee)

        result = cls(
            ship_from_address=ship_from_address,
            are_cases_required=are_cases_required,
            shipment_id=shipment_id,
            shipment_name=shipment_name,
            destination_fulfillment_center_id=destination_fulfillment_center_id,
            shipment_status=shipment_status,
            label_prep_type=label_prep_type,
            confirmed_need_by_date=confirmed_need_by_date,
            box_contents_source=box_contents_source,
            estimated_box_contents_fee=estimated_box_contents_fee,
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
