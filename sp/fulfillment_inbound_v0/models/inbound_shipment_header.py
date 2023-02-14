from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.intended_box_contents_source import IntendedBoxContentsSource
from ..models.label_prep_preference import LabelPrepPreference
from ..models.shipment_status import ShipmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="InboundShipmentHeader")


@attr.s(auto_attribs=True)
class InboundShipmentHeader:
    r"""Inbound shipment information used to create and update inbound shipments.

    Attributes:
        shipment_name (str): The name for the shipment. Use a naming convention that helps distinguish between shipments
            over time, such as the date the shipment was created.
        ship_from_address (Address):
        destination_fulfillment_center_id (str): The identifier for the fulfillment center to which the shipment will be
            shipped. Get this value from the InboundShipmentPlan object in the response returned by the
            createInboundShipmentPlan operation.
        shipment_status (ShipmentStatus): Indicates the status of the inbound shipment. When used with the
            createInboundShipment operation, WORKING is the only valid value. When used with the updateInboundShipment
            operation, possible values are WORKING, SHIPPED or CANCELLED.
        label_prep_preference (LabelPrepPreference): The preference for label preparation for an inbound shipment.
        are_cases_required (Union[Unset, bool]): Indicates whether or not an inbound shipment contains case-packed
            boxes. Note: A shipment must contain either all case-packed boxes or all individually packed boxes.

            Possible values:

            true - All boxes in the shipment must be case packed.

            false - All boxes in the shipment must be individually packed.

            Note: If AreCasesRequired = true for an inbound shipment, then the value of QuantityInCase must be greater than
            zero for every item in the shipment. Otherwise the service returns an error.
        intended_box_contents_source (Union[Unset, IntendedBoxContentsSource]): How the seller intends to provide box
            contents information for a shipment.
    """

    shipment_name: str
    ship_from_address: "Address"
    destination_fulfillment_center_id: str
    shipment_status: ShipmentStatus
    label_prep_preference: LabelPrepPreference
    are_cases_required: Union[Unset, bool] = UNSET
    intended_box_contents_source: Union[Unset, IntendedBoxContentsSource] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_name = self.shipment_name
        ship_from_address = self.ship_from_address.to_dict()

        destination_fulfillment_center_id = self.destination_fulfillment_center_id
        shipment_status = self.shipment_status.value

        label_prep_preference = self.label_prep_preference.value

        are_cases_required = self.are_cases_required
        intended_box_contents_source: Union[Unset, str] = UNSET
        if not isinstance(self.intended_box_contents_source, Unset):
            intended_box_contents_source = self.intended_box_contents_source.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShipmentName": shipment_name,
                "ShipFromAddress": ship_from_address,
                "DestinationFulfillmentCenterId": destination_fulfillment_center_id,
                "ShipmentStatus": shipment_status,
                "LabelPrepPreference": label_prep_preference,
            }
        )
        if are_cases_required is not UNSET:
            field_dict["AreCasesRequired"] = are_cases_required
        if intended_box_contents_source is not UNSET:
            field_dict["IntendedBoxContentsSource"] = intended_box_contents_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        shipment_name = d.pop("ShipmentName")

        ship_from_address = Address.from_dict(d.pop("ShipFromAddress"))

        destination_fulfillment_center_id = d.pop("DestinationFulfillmentCenterId")

        shipment_status = ShipmentStatus(d.pop("ShipmentStatus"))

        label_prep_preference = LabelPrepPreference(d.pop("LabelPrepPreference"))

        are_cases_required = d.pop("AreCasesRequired", UNSET)

        _intended_box_contents_source = d.pop("IntendedBoxContentsSource", UNSET)
        intended_box_contents_source: Union[Unset, IntendedBoxContentsSource]
        if isinstance(_intended_box_contents_source, Unset):
            intended_box_contents_source = UNSET
        else:
            intended_box_contents_source = IntendedBoxContentsSource(_intended_box_contents_source)

        result = cls(
            shipment_name=shipment_name,
            ship_from_address=ship_from_address,
            destination_fulfillment_center_id=destination_fulfillment_center_id,
            shipment_status=shipment_status,
            label_prep_preference=label_prep_preference,
            are_cases_required=are_cases_required,
            intended_box_contents_source=intended_box_contents_source,
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
