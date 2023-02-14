import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_item_acknowledgement_acknowledgement_code import OrderItemAcknowledgementAcknowledgementCode
from ..models.order_item_acknowledgement_rejection_reason import OrderItemAcknowledgementRejectionReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_quantity import ItemQuantity


T = TypeVar("T", bound="OrderItemAcknowledgement")


@attr.s(auto_attribs=True)
class OrderItemAcknowledgement:
    r"""
    Attributes:
        acknowledgement_code (OrderItemAcknowledgementAcknowledgementCode): This indicates the acknowledgement code.
        acknowledged_quantity (ItemQuantity): Details of quantity ordered.
        scheduled_ship_date (Union[Unset, datetime.datetime]): Estimated ship date per line item. Must be in ISO-8601
            date/time format.
        scheduled_delivery_date (Union[Unset, datetime.datetime]): Estimated delivery date per line item. Must be in
            ISO-8601 date/time format.
        rejection_reason (Union[Unset, OrderItemAcknowledgementRejectionReason]): Indicates the reason for rejection.
    """

    acknowledgement_code: OrderItemAcknowledgementAcknowledgementCode
    acknowledged_quantity: "ItemQuantity"
    scheduled_ship_date: Union[Unset, datetime.datetime] = UNSET
    scheduled_delivery_date: Union[Unset, datetime.datetime] = UNSET
    rejection_reason: Union[Unset, OrderItemAcknowledgementRejectionReason] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acknowledgement_code = self.acknowledgement_code.value

        acknowledged_quantity = self.acknowledged_quantity.to_dict()

        scheduled_ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_ship_date, Unset):
            scheduled_ship_date = self.scheduled_ship_date.isoformat()

        scheduled_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_delivery_date, Unset):
            scheduled_delivery_date = self.scheduled_delivery_date.isoformat()

        rejection_reason: Union[Unset, str] = UNSET
        if not isinstance(self.rejection_reason, Unset):
            rejection_reason = self.rejection_reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acknowledgementCode": acknowledgement_code,
                "acknowledgedQuantity": acknowledged_quantity,
            }
        )
        if scheduled_ship_date is not UNSET:
            field_dict["scheduledShipDate"] = scheduled_ship_date
        if scheduled_delivery_date is not UNSET:
            field_dict["scheduledDeliveryDate"] = scheduled_delivery_date
        if rejection_reason is not UNSET:
            field_dict["rejectionReason"] = rejection_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_quantity import ItemQuantity

        d = src_dict.copy()
        acknowledgement_code = OrderItemAcknowledgementAcknowledgementCode(d.pop("acknowledgementCode"))

        acknowledged_quantity = ItemQuantity.from_dict(d.pop("acknowledgedQuantity"))

        _scheduled_ship_date = d.pop("scheduledShipDate", UNSET)
        scheduled_ship_date: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_ship_date, Unset):
            scheduled_ship_date = UNSET
        else:
            scheduled_ship_date = isoparse(_scheduled_ship_date)

        _scheduled_delivery_date = d.pop("scheduledDeliveryDate", UNSET)
        scheduled_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_delivery_date, Unset):
            scheduled_delivery_date = UNSET
        else:
            scheduled_delivery_date = isoparse(_scheduled_delivery_date)

        _rejection_reason = d.pop("rejectionReason", UNSET)
        rejection_reason: Union[Unset, OrderItemAcknowledgementRejectionReason]
        if isinstance(_rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = OrderItemAcknowledgementRejectionReason(_rejection_reason)

        result = cls(
            acknowledgement_code=acknowledgement_code,
            acknowledged_quantity=acknowledged_quantity,
            scheduled_ship_date=scheduled_ship_date,
            scheduled_delivery_date=scheduled_delivery_date,
            rejection_reason=rejection_reason,
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
