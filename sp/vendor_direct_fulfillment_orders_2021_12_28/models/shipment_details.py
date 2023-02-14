from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_dates import ShipmentDates


T = TypeVar("T", bound="ShipmentDetails")


@attr.s(auto_attribs=True)
class ShipmentDetails:
    r"""Shipment details required for the shipment.

    Attributes:
        is_priority_shipment (bool): When true, this is a priority shipment.
        is_pslip_required (bool): When true, a packing slip is required to be sent to the customer.
        ship_method (str): Ship method to be used for shipping the order. Amazon defines ship method codes indicating
            the shipping carrier and shipment service level. To see the full list of ship methods in use, including both the
            code and the friendly name, search the 'Help' section on Vendor Central for 'ship methods'.
        shipment_dates (ShipmentDates): Shipment dates.
        message_to_customer (str): Message to customer for order status.
        is_scheduled_delivery_shipment (Union[Unset, bool]): When true, this order is part of a scheduled delivery
            program.
        is_gift (Union[Unset, bool]): When true, the order contain a gift. Include the gift message and gift wrap
            information.
    """

    is_priority_shipment: bool
    is_pslip_required: bool
    ship_method: str
    shipment_dates: "ShipmentDates"
    message_to_customer: str
    is_scheduled_delivery_shipment: Union[Unset, bool] = UNSET
    is_gift: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_priority_shipment = self.is_priority_shipment
        is_pslip_required = self.is_pslip_required
        ship_method = self.ship_method
        shipment_dates = self.shipment_dates.to_dict()

        message_to_customer = self.message_to_customer
        is_scheduled_delivery_shipment = self.is_scheduled_delivery_shipment
        is_gift = self.is_gift

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isPriorityShipment": is_priority_shipment,
                "isPslipRequired": is_pslip_required,
                "shipMethod": ship_method,
                "shipmentDates": shipment_dates,
                "messageToCustomer": message_to_customer,
            }
        )
        if is_scheduled_delivery_shipment is not UNSET:
            field_dict["isScheduledDeliveryShipment"] = is_scheduled_delivery_shipment
        if is_gift is not UNSET:
            field_dict["isGift"] = is_gift

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipment_dates import ShipmentDates

        d = src_dict.copy()
        is_priority_shipment = d.pop("isPriorityShipment")

        is_pslip_required = d.pop("isPslipRequired")

        ship_method = d.pop("shipMethod")

        shipment_dates = ShipmentDates.from_dict(d.pop("shipmentDates"))

        message_to_customer = d.pop("messageToCustomer")

        is_scheduled_delivery_shipment = d.pop("isScheduledDeliveryShipment", UNSET)

        is_gift = d.pop("isGift", UNSET)

        result = cls(
            is_priority_shipment=is_priority_shipment,
            is_pslip_required=is_pslip_required,
            ship_method=ship_method,
            shipment_dates=shipment_dates,
            message_to_customer=message_to_customer,
            is_scheduled_delivery_shipment=is_scheduled_delivery_shipment,
            is_gift=is_gift,
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
