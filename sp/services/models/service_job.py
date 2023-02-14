import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.service_job_service_job_status import ServiceJobServiceJobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment import Appointment
    from ..models.appointment_time import AppointmentTime
    from ..models.associated_item import AssociatedItem
    from ..models.buyer import Buyer
    from ..models.scope_of_work import ScopeOfWork
    from ..models.seller import Seller
    from ..models.service_job_provider import ServiceJobProvider
    from ..models.service_location import ServiceLocation


T = TypeVar("T", bound="ServiceJob")


@attr.s(auto_attribs=True)
class ServiceJob:
    r"""The job details of a service.

    Attributes:
        create_time (Union[Unset, datetime.datetime]): The date and time of the creation of the job in ISO 8601 format.
        service_job_id (Union[Unset, str]): Amazon identifier for the service job.
        service_job_status (Union[Unset, ServiceJobServiceJobStatus]): The status of the service job.
        scope_of_work (Union[Unset, ScopeOfWork]): The scope of work for the order.
        seller (Union[Unset, Seller]): Information about the seller of the service job.
        service_job_provider (Union[Unset, ServiceJobProvider]): Information about the service job provider.
        preferred_appointment_times (Union[Unset, List['AppointmentTime']]): A list of appointment windows preferred by
            the buyer. Included only if the buyer selected appointment windows when creating the order.
        appointments (Union[Unset, List['Appointment']]): A list of appointments.
        service_order_id (Union[Unset, str]): The Amazon-defined identifier for an order placed by the buyer, in 3-7-7
            format.
        marketplace_id (Union[Unset, str]): The marketplace identifier.
        store_id (Union[Unset, str]): The Amazon-defined identifier for the region scope.
        buyer (Union[Unset, Buyer]): Information about the buyer.
        associated_items (Union[Unset, List['AssociatedItem']]): A list of items associated with the service job.
        service_location (Union[Unset, ServiceLocation]): Information about the location of the service job.
    """

    create_time: Union[Unset, datetime.datetime] = UNSET
    service_job_id: Union[Unset, str] = UNSET
    service_job_status: Union[Unset, ServiceJobServiceJobStatus] = UNSET
    scope_of_work: Union[Unset, "ScopeOfWork"] = UNSET
    seller: Union[Unset, "Seller"] = UNSET
    service_job_provider: Union[Unset, "ServiceJobProvider"] = UNSET
    preferred_appointment_times: Union[Unset, List["AppointmentTime"]] = UNSET
    appointments: Union[Unset, List["Appointment"]] = UNSET
    service_order_id: Union[Unset, str] = UNSET
    marketplace_id: Union[Unset, str] = UNSET
    store_id: Union[Unset, str] = UNSET
    buyer: Union[Unset, "Buyer"] = UNSET
    associated_items: Union[Unset, List["AssociatedItem"]] = UNSET
    service_location: Union[Unset, "ServiceLocation"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        create_time: Union[Unset, str] = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        service_job_id = self.service_job_id
        service_job_status: Union[Unset, str] = UNSET
        if not isinstance(self.service_job_status, Unset):
            service_job_status = self.service_job_status.value

        scope_of_work: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scope_of_work, Unset):
            scope_of_work = self.scope_of_work.to_dict()

        seller: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seller, Unset):
            seller = self.seller.to_dict()

        service_job_provider: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_job_provider, Unset):
            service_job_provider = self.service_job_provider.to_dict()

        preferred_appointment_times: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.preferred_appointment_times, Unset):
            preferred_appointment_times = []
            for preferred_appointment_times_item_data in self.preferred_appointment_times:
                preferred_appointment_times_item = preferred_appointment_times_item_data.to_dict()

                preferred_appointment_times.append(preferred_appointment_times_item)

        appointments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.appointments, Unset):
            appointments = []
            for appointments_item_data in self.appointments:
                appointments_item = appointments_item_data.to_dict()

                appointments.append(appointments_item)

        service_order_id = self.service_order_id
        marketplace_id = self.marketplace_id
        store_id = self.store_id
        buyer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyer, Unset):
            buyer = self.buyer.to_dict()

        associated_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.associated_items, Unset):
            associated_items = []
            for associated_items_item_data in self.associated_items:
                associated_items_item = associated_items_item_data.to_dict()

                associated_items.append(associated_items_item)

        service_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_location, Unset):
            service_location = self.service_location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if service_job_id is not UNSET:
            field_dict["serviceJobId"] = service_job_id
        if service_job_status is not UNSET:
            field_dict["serviceJobStatus"] = service_job_status
        if scope_of_work is not UNSET:
            field_dict["scopeOfWork"] = scope_of_work
        if seller is not UNSET:
            field_dict["seller"] = seller
        if service_job_provider is not UNSET:
            field_dict["serviceJobProvider"] = service_job_provider
        if preferred_appointment_times is not UNSET:
            field_dict["preferredAppointmentTimes"] = preferred_appointment_times
        if appointments is not UNSET:
            field_dict["appointments"] = appointments
        if service_order_id is not UNSET:
            field_dict["serviceOrderId"] = service_order_id
        if marketplace_id is not UNSET:
            field_dict["marketplaceId"] = marketplace_id
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if buyer is not UNSET:
            field_dict["buyer"] = buyer
        if associated_items is not UNSET:
            field_dict["associatedItems"] = associated_items
        if service_location is not UNSET:
            field_dict["serviceLocation"] = service_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment import Appointment
        from ..models.appointment_time import AppointmentTime
        from ..models.associated_item import AssociatedItem
        from ..models.buyer import Buyer
        from ..models.scope_of_work import ScopeOfWork
        from ..models.seller import Seller
        from ..models.service_job_provider import ServiceJobProvider
        from ..models.service_location import ServiceLocation

        d = src_dict.copy()
        _create_time = d.pop("createTime", UNSET)
        create_time: Union[Unset, datetime.datetime]
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = isoparse(_create_time)

        service_job_id = d.pop("serviceJobId", UNSET)

        _service_job_status = d.pop("serviceJobStatus", UNSET)
        service_job_status: Union[Unset, ServiceJobServiceJobStatus]
        if isinstance(_service_job_status, Unset):
            service_job_status = UNSET
        else:
            service_job_status = ServiceJobServiceJobStatus(_service_job_status)

        _scope_of_work = d.pop("scopeOfWork", UNSET)
        scope_of_work: Union[Unset, ScopeOfWork]
        if isinstance(_scope_of_work, Unset):
            scope_of_work = UNSET
        else:
            scope_of_work = ScopeOfWork.from_dict(_scope_of_work)

        _seller = d.pop("seller", UNSET)
        seller: Union[Unset, Seller]
        if isinstance(_seller, Unset):
            seller = UNSET
        else:
            seller = Seller.from_dict(_seller)

        _service_job_provider = d.pop("serviceJobProvider", UNSET)
        service_job_provider: Union[Unset, ServiceJobProvider]
        if isinstance(_service_job_provider, Unset):
            service_job_provider = UNSET
        else:
            service_job_provider = ServiceJobProvider.from_dict(_service_job_provider)

        preferred_appointment_times = []
        _preferred_appointment_times = d.pop("preferredAppointmentTimes", UNSET)
        for preferred_appointment_times_item_data in _preferred_appointment_times or []:
            preferred_appointment_times_item = AppointmentTime.from_dict(preferred_appointment_times_item_data)

            preferred_appointment_times.append(preferred_appointment_times_item)

        appointments = []
        _appointments = d.pop("appointments", UNSET)
        for appointments_item_data in _appointments or []:
            appointments_item = Appointment.from_dict(appointments_item_data)

            appointments.append(appointments_item)

        service_order_id = d.pop("serviceOrderId", UNSET)

        marketplace_id = d.pop("marketplaceId", UNSET)

        store_id = d.pop("storeId", UNSET)

        _buyer = d.pop("buyer", UNSET)
        buyer: Union[Unset, Buyer]
        if isinstance(_buyer, Unset):
            buyer = UNSET
        else:
            buyer = Buyer.from_dict(_buyer)

        associated_items = []
        _associated_items = d.pop("associatedItems", UNSET)
        for associated_items_item_data in _associated_items or []:
            associated_items_item = AssociatedItem.from_dict(associated_items_item_data)

            associated_items.append(associated_items_item)

        _service_location = d.pop("serviceLocation", UNSET)
        service_location: Union[Unset, ServiceLocation]
        if isinstance(_service_location, Unset):
            service_location = UNSET
        else:
            service_location = ServiceLocation.from_dict(_service_location)

        result = cls(
            create_time=create_time,
            service_job_id=service_job_id,
            service_job_status=service_job_status,
            scope_of_work=scope_of_work,
            seller=seller,
            service_job_provider=service_job_provider,
            preferred_appointment_times=preferred_appointment_times,
            appointments=appointments,
            service_order_id=service_order_id,
            marketplace_id=marketplace_id,
            store_id=store_id,
            buyer=buyer,
            associated_items=associated_items,
            service_location=service_location,
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
