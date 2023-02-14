import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipmentDates")


@attr.s(auto_attribs=True)
class ShipmentDates:
    r"""Shipment dates.

    Attributes:
        required_ship_date (datetime.datetime): Time by which the vendor is required to ship the order.
        promised_delivery_date (Union[Unset, datetime.datetime]): Delivery date promised to the Amazon customer.
    """

    required_ship_date: datetime.datetime
    promised_delivery_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        required_ship_date = self.required_ship_date.isoformat()

        promised_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.promised_delivery_date, Unset):
            promised_delivery_date = self.promised_delivery_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requiredShipDate": required_ship_date,
            }
        )
        if promised_delivery_date is not UNSET:
            field_dict["promisedDeliveryDate"] = promised_delivery_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        required_ship_date = isoparse(d.pop("requiredShipDate"))

        _promised_delivery_date = d.pop("promisedDeliveryDate", UNSET)
        promised_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_promised_delivery_date, Unset):
            promised_delivery_date = UNSET
        else:
            promised_delivery_date = isoparse(_promised_delivery_date)

        result = cls(
            required_ship_date=required_ship_date,
            promised_delivery_date=promised_delivery_date,
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
