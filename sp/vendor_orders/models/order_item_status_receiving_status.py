import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_item_status_receiving_status_receive_status import OrderItemStatusReceivingStatusReceiveStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_quantity import ItemQuantity


T = TypeVar("T", bound="OrderItemStatusReceivingStatus")


@attr.s(auto_attribs=True)
class OrderItemStatusReceivingStatus:
    r"""Item receive status at the buyer's warehouse.

    Attributes:
        receive_status (Union[Unset, OrderItemStatusReceivingStatusReceiveStatus]): Receive status of the line item.
        received_quantity (Union[Unset, ItemQuantity]): Details of quantity ordered.
        last_receive_date (Union[Unset, datetime.datetime]): The date when the most recent item was received at the
            buyer's warehouse. Must be in ISO-8601 date/time format.
    """

    receive_status: Union[Unset, OrderItemStatusReceivingStatusReceiveStatus] = UNSET
    received_quantity: Union[Unset, "ItemQuantity"] = UNSET
    last_receive_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        receive_status: Union[Unset, str] = UNSET
        if not isinstance(self.receive_status, Unset):
            receive_status = self.receive_status.value

        received_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.received_quantity, Unset):
            received_quantity = self.received_quantity.to_dict()

        last_receive_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_receive_date, Unset):
            last_receive_date = self.last_receive_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if receive_status is not UNSET:
            field_dict["receiveStatus"] = receive_status
        if received_quantity is not UNSET:
            field_dict["receivedQuantity"] = received_quantity
        if last_receive_date is not UNSET:
            field_dict["lastReceiveDate"] = last_receive_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_quantity import ItemQuantity

        d = src_dict.copy()
        _receive_status = d.pop("receiveStatus", UNSET)
        receive_status: Union[Unset, OrderItemStatusReceivingStatusReceiveStatus]
        if isinstance(_receive_status, Unset):
            receive_status = UNSET
        else:
            receive_status = OrderItemStatusReceivingStatusReceiveStatus(_receive_status)

        _received_quantity = d.pop("receivedQuantity", UNSET)
        received_quantity: Union[Unset, ItemQuantity]
        if isinstance(_received_quantity, Unset):
            received_quantity = UNSET
        else:
            received_quantity = ItemQuantity.from_dict(_received_quantity)

        _last_receive_date = d.pop("lastReceiveDate", UNSET)
        last_receive_date: Union[Unset, datetime.datetime]
        if isinstance(_last_receive_date, Unset):
            last_receive_date = UNSET
        else:
            last_receive_date = isoparse(_last_receive_date)

        result = cls(
            receive_status=receive_status,
            received_quantity=received_quantity,
            last_receive_date=last_receive_date,
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
