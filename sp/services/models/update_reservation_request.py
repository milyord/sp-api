from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.reservation import Reservation


T = TypeVar("T", bound="UpdateReservationRequest")


@attr.s(auto_attribs=True)
class UpdateReservationRequest:
    r"""Request schema for the `updateReservation` operation.

    Attributes:
        resource_id (str): Resource (store) identifier.
        reservation (Reservation): Reservation object reduces the capacity of a resource.
    """

    resource_id: str
    reservation: "Reservation"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_id = self.resource_id
        reservation = self.reservation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceId": resource_id,
                "reservation": reservation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reservation import Reservation

        d = src_dict.copy()
        resource_id = d.pop("resourceId")

        reservation = Reservation.from_dict(d.pop("reservation"))

        result = cls(
            resource_id=resource_id,
            reservation=reservation,
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
