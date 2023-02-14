from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reservation_type import ReservationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.availability_record import AvailabilityRecord


T = TypeVar("T", bound="Reservation")


@attr.s(auto_attribs=True)
class Reservation:
    r"""Reservation object reduces the capacity of a resource.

    Attributes:
        type (ReservationType): Type of reservation.
        availability (AvailabilityRecord): `AvailabilityRecord` to represent the capacity of a resource over a time
            range.
        reservation_id (Union[Unset, str]): Unique identifier for a reservation. If present, it is treated as an update
            reservation request and will update the corresponding reservation. Otherwise, it is treated as a new create
            reservation request.
    """

    type: ReservationType
    availability: "AvailabilityRecord"
    reservation_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        availability = self.availability.to_dict()

        reservation_id = self.reservation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "availability": availability,
            }
        )
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.availability_record import AvailabilityRecord

        d = src_dict.copy()
        type = ReservationType(d.pop("type"))

        availability = AvailabilityRecord.from_dict(d.pop("availability"))

        reservation_id = d.pop("reservationId", UNSET)

        result = cls(
            type=type,
            availability=availability,
            reservation_id=reservation_id,
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
