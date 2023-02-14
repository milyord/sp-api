import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.additional_location_info import AdditionalLocationInfo
from ..models.current_status import CurrentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracking_address import TrackingAddress
    from ..models.tracking_event import TrackingEvent


T = TypeVar("T", bound="PackageTrackingDetails")


@attr.s(auto_attribs=True)
class PackageTrackingDetails:
    r"""
    Attributes:
        package_number (int): The package identifier.
        tracking_number (Union[Unset, str]): The tracking number for the package.
        customer_tracking_link (Union[Unset, str]): Link on swiship.com that allows customers to track the package.
        carrier_code (Union[Unset, str]): The name of the carrier.
        carrier_phone_number (Union[Unset, str]): The phone number of the carrier.
        carrier_url (Union[Unset, str]): The URL of the carrier’s website.
        ship_date (Union[Unset, datetime.datetime]):
        estimated_arrival_date (Union[Unset, datetime.datetime]):
        ship_to_address (Union[Unset, TrackingAddress]): Address information for tracking the package.
        current_status (Union[Unset, CurrentStatus]): The current delivery status of the package.
        current_status_description (Union[Unset, str]): Description corresponding to the CurrentStatus value.
        signed_for_by (Union[Unset, str]): The name of the person who signed for the package.
        additional_location_info (Union[Unset, AdditionalLocationInfo]): Additional location information.
        tracking_events (Union[Unset, List['TrackingEvent']]): An array of tracking event information.
    """

    package_number: int
    tracking_number: Union[Unset, str] = UNSET
    customer_tracking_link: Union[Unset, str] = UNSET
    carrier_code: Union[Unset, str] = UNSET
    carrier_phone_number: Union[Unset, str] = UNSET
    carrier_url: Union[Unset, str] = UNSET
    ship_date: Union[Unset, datetime.datetime] = UNSET
    estimated_arrival_date: Union[Unset, datetime.datetime] = UNSET
    ship_to_address: Union[Unset, "TrackingAddress"] = UNSET
    current_status: Union[Unset, CurrentStatus] = UNSET
    current_status_description: Union[Unset, str] = UNSET
    signed_for_by: Union[Unset, str] = UNSET
    additional_location_info: Union[Unset, AdditionalLocationInfo] = UNSET
    tracking_events: Union[Unset, List["TrackingEvent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_number = self.package_number
        tracking_number = self.tracking_number
        customer_tracking_link = self.customer_tracking_link
        carrier_code = self.carrier_code
        carrier_phone_number = self.carrier_phone_number
        carrier_url = self.carrier_url
        ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.ship_date, Unset):
            ship_date = self.ship_date.isoformat()

        estimated_arrival_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_arrival_date, Unset):
            estimated_arrival_date = self.estimated_arrival_date.isoformat()

        ship_to_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_address, Unset):
            ship_to_address = self.ship_to_address.to_dict()

        current_status: Union[Unset, str] = UNSET
        if not isinstance(self.current_status, Unset):
            current_status = self.current_status.value

        current_status_description = self.current_status_description
        signed_for_by = self.signed_for_by
        additional_location_info: Union[Unset, str] = UNSET
        if not isinstance(self.additional_location_info, Unset):
            additional_location_info = self.additional_location_info.value

        tracking_events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_events, Unset):
            tracking_events = []
            for componentsschemas_tracking_event_list_item_data in self.tracking_events:
                componentsschemas_tracking_event_list_item = componentsschemas_tracking_event_list_item_data.to_dict()

                tracking_events.append(componentsschemas_tracking_event_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageNumber": package_number,
            }
        )
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if customer_tracking_link is not UNSET:
            field_dict["customerTrackingLink"] = customer_tracking_link
        if carrier_code is not UNSET:
            field_dict["carrierCode"] = carrier_code
        if carrier_phone_number is not UNSET:
            field_dict["carrierPhoneNumber"] = carrier_phone_number
        if carrier_url is not UNSET:
            field_dict["carrierURL"] = carrier_url
        if ship_date is not UNSET:
            field_dict["shipDate"] = ship_date
        if estimated_arrival_date is not UNSET:
            field_dict["estimatedArrivalDate"] = estimated_arrival_date
        if ship_to_address is not UNSET:
            field_dict["shipToAddress"] = ship_to_address
        if current_status is not UNSET:
            field_dict["currentStatus"] = current_status
        if current_status_description is not UNSET:
            field_dict["currentStatusDescription"] = current_status_description
        if signed_for_by is not UNSET:
            field_dict["signedForBy"] = signed_for_by
        if additional_location_info is not UNSET:
            field_dict["additionalLocationInfo"] = additional_location_info
        if tracking_events is not UNSET:
            field_dict["trackingEvents"] = tracking_events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tracking_address import TrackingAddress
        from ..models.tracking_event import TrackingEvent

        d = src_dict.copy()
        package_number = d.pop("packageNumber")

        tracking_number = d.pop("trackingNumber", UNSET)

        customer_tracking_link = d.pop("customerTrackingLink", UNSET)

        carrier_code = d.pop("carrierCode", UNSET)

        carrier_phone_number = d.pop("carrierPhoneNumber", UNSET)

        carrier_url = d.pop("carrierURL", UNSET)

        _ship_date = d.pop("shipDate", UNSET)
        ship_date: Union[Unset, datetime.datetime]
        if isinstance(_ship_date, Unset):
            ship_date = UNSET
        else:
            ship_date = isoparse(_ship_date)

        _estimated_arrival_date = d.pop("estimatedArrivalDate", UNSET)
        estimated_arrival_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_arrival_date, Unset):
            estimated_arrival_date = UNSET
        else:
            estimated_arrival_date = isoparse(_estimated_arrival_date)

        _ship_to_address = d.pop("shipToAddress", UNSET)
        ship_to_address: Union[Unset, TrackingAddress]
        if isinstance(_ship_to_address, Unset):
            ship_to_address = UNSET
        else:
            ship_to_address = TrackingAddress.from_dict(_ship_to_address)

        _current_status = d.pop("currentStatus", UNSET)
        current_status: Union[Unset, CurrentStatus]
        if isinstance(_current_status, Unset):
            current_status = UNSET
        else:
            current_status = CurrentStatus(_current_status)

        current_status_description = d.pop("currentStatusDescription", UNSET)

        signed_for_by = d.pop("signedForBy", UNSET)

        _additional_location_info = d.pop("additionalLocationInfo", UNSET)
        additional_location_info: Union[Unset, AdditionalLocationInfo]
        if isinstance(_additional_location_info, Unset):
            additional_location_info = UNSET
        else:
            additional_location_info = AdditionalLocationInfo(_additional_location_info)

        tracking_events = []
        _tracking_events = d.pop("trackingEvents", UNSET)
        for componentsschemas_tracking_event_list_item_data in _tracking_events or []:
            componentsschemas_tracking_event_list_item = TrackingEvent.from_dict(
                componentsschemas_tracking_event_list_item_data
            )

            tracking_events.append(componentsschemas_tracking_event_list_item)

        result = cls(
            package_number=package_number,
            tracking_number=tracking_number,
            customer_tracking_link=customer_tracking_link,
            carrier_code=carrier_code,
            carrier_phone_number=carrier_phone_number,
            carrier_url=carrier_url,
            ship_date=ship_date,
            estimated_arrival_date=estimated_arrival_date,
            ship_to_address=ship_to_address,
            current_status=current_status,
            current_status_description=current_status_description,
            signed_for_by=signed_for_by,
            additional_location_info=additional_location_info,
            tracking_events=tracking_events,
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
