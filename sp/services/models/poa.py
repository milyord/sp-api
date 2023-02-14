import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.poa_poa_type import PoaPoaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment_time import AppointmentTime
    from ..models.technician import Technician


T = TypeVar("T", bound="Poa")


@attr.s(auto_attribs=True)
class Poa:
    r"""Proof of Appointment (POA) details.

    Attributes:
        appointment_time (Union[Unset, AppointmentTime]): The time of the appointment window.
        technicians (Union[Unset, List['Technician']]): A list of technicians.
        uploading_technician (Union[Unset, str]): The identifier of the technician who uploaded the POA.
        upload_time (Union[Unset, datetime.datetime]): The date and time when the POA was uploaded in ISO 8601 format.
        poa_type (Union[Unset, PoaPoaType]): The type of POA uploaded.
    """

    appointment_time: Union[Unset, "AppointmentTime"] = UNSET
    technicians: Union[Unset, List["Technician"]] = UNSET
    uploading_technician: Union[Unset, str] = UNSET
    upload_time: Union[Unset, datetime.datetime] = UNSET
    poa_type: Union[Unset, PoaPoaType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointment_time, Unset):
            appointment_time = self.appointment_time.to_dict()

        technicians: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.technicians, Unset):
            technicians = []
            for technicians_item_data in self.technicians:
                technicians_item = technicians_item_data.to_dict()

                technicians.append(technicians_item)

        uploading_technician = self.uploading_technician
        upload_time: Union[Unset, str] = UNSET
        if not isinstance(self.upload_time, Unset):
            upload_time = self.upload_time.isoformat()

        poa_type: Union[Unset, str] = UNSET
        if not isinstance(self.poa_type, Unset):
            poa_type = self.poa_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_time is not UNSET:
            field_dict["appointmentTime"] = appointment_time
        if technicians is not UNSET:
            field_dict["technicians"] = technicians
        if uploading_technician is not UNSET:
            field_dict["uploadingTechnician"] = uploading_technician
        if upload_time is not UNSET:
            field_dict["uploadTime"] = upload_time
        if poa_type is not UNSET:
            field_dict["poaType"] = poa_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_time import AppointmentTime
        from ..models.technician import Technician

        d = src_dict.copy()
        _appointment_time = d.pop("appointmentTime", UNSET)
        appointment_time: Union[Unset, AppointmentTime]
        if isinstance(_appointment_time, Unset):
            appointment_time = UNSET
        else:
            appointment_time = AppointmentTime.from_dict(_appointment_time)

        technicians = []
        _technicians = d.pop("technicians", UNSET)
        for technicians_item_data in _technicians or []:
            technicians_item = Technician.from_dict(technicians_item_data)

            technicians.append(technicians_item)

        uploading_technician = d.pop("uploadingTechnician", UNSET)

        _upload_time = d.pop("uploadTime", UNSET)
        upload_time: Union[Unset, datetime.datetime]
        if isinstance(_upload_time, Unset):
            upload_time = UNSET
        else:
            upload_time = isoparse(_upload_time)

        _poa_type = d.pop("poaType", UNSET)
        poa_type: Union[Unset, PoaPoaType]
        if isinstance(_poa_type, Unset):
            poa_type = UNSET
        else:
            poa_type = PoaPoaType(_poa_type)

        result = cls(
            appointment_time=appointment_time,
            technicians=technicians,
            uploading_technician=uploading_technician,
            upload_time=upload_time,
            poa_type=poa_type,
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
