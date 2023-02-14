from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.label_prep_type import LabelPrepType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.box_contents_fee_details import BoxContentsFeeDetails
    from ..models.inbound_shipment_plan_item import InboundShipmentPlanItem


T = TypeVar("T", bound="InboundShipmentPlan")


@attr.s(auto_attribs=True)
class InboundShipmentPlan:
    r"""Inbound shipment information used to create an inbound shipment. Returned by the createInboundShipmentPlan
    operation.

        Attributes:
            shipment_id (str): A shipment identifier originally returned by the createInboundShipmentPlan operation.
            destination_fulfillment_center_id (str): An Amazon fulfillment center identifier created by Amazon.
            ship_to_address (Address):
            label_prep_type (LabelPrepType): The type of label preparation that is required for the inbound shipment.
            items (List['InboundShipmentPlanItem']): A list of inbound shipment plan item information.
            estimated_box_contents_fee (Union[Unset, BoxContentsFeeDetails]): The manual processing fee per unit and total
                fee for a shipment.
    """

    shipment_id: str
    destination_fulfillment_center_id: str
    ship_to_address: "Address"
    label_prep_type: LabelPrepType
    items: List["InboundShipmentPlanItem"]
    estimated_box_contents_fee: Union[Unset, "BoxContentsFeeDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_id = self.shipment_id
        destination_fulfillment_center_id = self.destination_fulfillment_center_id
        ship_to_address = self.ship_to_address.to_dict()

        label_prep_type = self.label_prep_type.value

        items = []
        for componentsschemas_inbound_shipment_plan_item_list_item_data in self.items:
            componentsschemas_inbound_shipment_plan_item_list_item = (
                componentsschemas_inbound_shipment_plan_item_list_item_data.to_dict()
            )

            items.append(componentsschemas_inbound_shipment_plan_item_list_item)

        estimated_box_contents_fee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimated_box_contents_fee, Unset):
            estimated_box_contents_fee = self.estimated_box_contents_fee.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShipmentId": shipment_id,
                "DestinationFulfillmentCenterId": destination_fulfillment_center_id,
                "ShipToAddress": ship_to_address,
                "LabelPrepType": label_prep_type,
                "Items": items,
            }
        )
        if estimated_box_contents_fee is not UNSET:
            field_dict["EstimatedBoxContentsFee"] = estimated_box_contents_fee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.box_contents_fee_details import BoxContentsFeeDetails
        from ..models.inbound_shipment_plan_item import InboundShipmentPlanItem

        d = src_dict.copy()
        shipment_id = d.pop("ShipmentId")

        destination_fulfillment_center_id = d.pop("DestinationFulfillmentCenterId")

        ship_to_address = Address.from_dict(d.pop("ShipToAddress"))

        label_prep_type = LabelPrepType(d.pop("LabelPrepType"))

        items = []
        _items = d.pop("Items")
        for componentsschemas_inbound_shipment_plan_item_list_item_data in _items:
            componentsschemas_inbound_shipment_plan_item_list_item = InboundShipmentPlanItem.from_dict(
                componentsschemas_inbound_shipment_plan_item_list_item_data
            )

            items.append(componentsschemas_inbound_shipment_plan_item_list_item)

        _estimated_box_contents_fee = d.pop("EstimatedBoxContentsFee", UNSET)
        estimated_box_contents_fee: Union[Unset, BoxContentsFeeDetails]
        if isinstance(_estimated_box_contents_fee, Unset):
            estimated_box_contents_fee = UNSET
        else:
            estimated_box_contents_fee = BoxContentsFeeDetails.from_dict(_estimated_box_contents_fee)

        result = cls(
            shipment_id=shipment_id,
            destination_fulfillment_center_id=destination_fulfillment_center_id,
            ship_to_address=ship_to_address,
            label_prep_type=label_prep_type,
            items=items,
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
