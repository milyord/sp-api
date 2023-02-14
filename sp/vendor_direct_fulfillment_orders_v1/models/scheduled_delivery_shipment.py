import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduledDeliveryShipment")


@attr.s(auto_attribs=True)
class ScheduledDeliveryShipment:
    r"""Dates for the scheduled delivery shipments.

    Attributes:
        scheduled_delivery_service_type (Union[Unset, str]): Scheduled delivery service type.
        earliest_nominated_delivery_date (Union[Unset, datetime.datetime]): Earliest nominated delivery date for the
            scheduled delivery.
        latest_nominated_delivery_date (Union[Unset, datetime.datetime]): Latest nominated delivery date for the
            scheduled delivery.
    """

    scheduled_delivery_service_type: Union[Unset, str] = UNSET
    earliest_nominated_delivery_date: Union[Unset, datetime.datetime] = UNSET
    latest_nominated_delivery_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheduled_delivery_service_type = self.scheduled_delivery_service_type
        earliest_nominated_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.earliest_nominated_delivery_date, Unset):
            earliest_nominated_delivery_date = self.earliest_nominated_delivery_date.isoformat()

        latest_nominated_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_nominated_delivery_date, Unset):
            latest_nominated_delivery_date = self.latest_nominated_delivery_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scheduled_delivery_service_type is not UNSET:
            field_dict["scheduledDeliveryServiceType"] = scheduled_delivery_service_type
        if earliest_nominated_delivery_date is not UNSET:
            field_dict["earliestNominatedDeliveryDate"] = earliest_nominated_delivery_date
        if latest_nominated_delivery_date is not UNSET:
            field_dict["latestNominatedDeliveryDate"] = latest_nominated_delivery_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scheduled_delivery_service_type = d.pop("scheduledDeliveryServiceType", UNSET)

        _earliest_nominated_delivery_date = d.pop("earliestNominatedDeliveryDate", UNSET)
        earliest_nominated_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_earliest_nominated_delivery_date, Unset):
            earliest_nominated_delivery_date = UNSET
        else:
            earliest_nominated_delivery_date = isoparse(_earliest_nominated_delivery_date)

        _latest_nominated_delivery_date = d.pop("latestNominatedDeliveryDate", UNSET)
        latest_nominated_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_nominated_delivery_date, Unset):
            latest_nominated_delivery_date = UNSET
        else:
            latest_nominated_delivery_date = isoparse(_latest_nominated_delivery_date)

        result = cls(
            scheduled_delivery_service_type=scheduled_delivery_service_type,
            earliest_nominated_delivery_date=earliest_nominated_delivery_date,
            latest_nominated_delivery_date=latest_nominated_delivery_date,
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
