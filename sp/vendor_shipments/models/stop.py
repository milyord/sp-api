import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stop_function_code import StopFunctionCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location import Location


T = TypeVar("T", bound="Stop")


@attr.s(auto_attribs=True)
class Stop:
    r"""Contractual or operational port or point relevant to the movement of the cargo.

    Attributes:
        function_code (StopFunctionCode): Provide the function code.
        location_identification (Union[Unset, Location]): Location identifier.
        arrival_time (Union[Unset, datetime.datetime]): Date and time of the arrival of the cargo.
        departure_time (Union[Unset, datetime.datetime]): Date and time of the departure of the cargo.
    """

    function_code: StopFunctionCode
    location_identification: Union[Unset, "Location"] = UNSET
    arrival_time: Union[Unset, datetime.datetime] = UNSET
    departure_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        function_code = self.function_code.value

        location_identification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location_identification, Unset):
            location_identification = self.location_identification.to_dict()

        arrival_time: Union[Unset, str] = UNSET
        if not isinstance(self.arrival_time, Unset):
            arrival_time = self.arrival_time.isoformat()

        departure_time: Union[Unset, str] = UNSET
        if not isinstance(self.departure_time, Unset):
            departure_time = self.departure_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "functionCode": function_code,
            }
        )
        if location_identification is not UNSET:
            field_dict["locationIdentification"] = location_identification
        if arrival_time is not UNSET:
            field_dict["arrivalTime"] = arrival_time
        if departure_time is not UNSET:
            field_dict["departureTime"] = departure_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location import Location

        d = src_dict.copy()
        function_code = StopFunctionCode(d.pop("functionCode"))

        _location_identification = d.pop("locationIdentification", UNSET)
        location_identification: Union[Unset, Location]
        if isinstance(_location_identification, Unset):
            location_identification = UNSET
        else:
            location_identification = Location.from_dict(_location_identification)

        _arrival_time = d.pop("arrivalTime", UNSET)
        arrival_time: Union[Unset, datetime.datetime]
        if isinstance(_arrival_time, Unset):
            arrival_time = UNSET
        else:
            arrival_time = isoparse(_arrival_time)

        _departure_time = d.pop("departureTime", UNSET)
        departure_time: Union[Unset, datetime.datetime]
        if isinstance(_departure_time, Unset):
            departure_time = UNSET
        else:
            departure_time = isoparse(_departure_time)

        result = cls(
            function_code=function_code,
            location_identification=location_identification,
            arrival_time=arrival_time,
            departure_time=departure_time,
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
