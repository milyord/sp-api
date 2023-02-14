from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.availability_record import AvailabilityRecord


T = TypeVar("T", bound="UpdateScheduleRequest")


@attr.s(auto_attribs=True)
class UpdateScheduleRequest:
    r"""Request schema for the `updateSchedule` operation.

    Attributes:
        schedules (List['AvailabilityRecord']): List of `AvailabilityRecord`s to represent the capacity of a resource
            over a time range.
    """

    schedules: List["AvailabilityRecord"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedules = []
        for componentsschemas_availability_records_item_data in self.schedules:
            componentsschemas_availability_records_item = componentsschemas_availability_records_item_data.to_dict()

            schedules.append(componentsschemas_availability_records_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedules": schedules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.availability_record import AvailabilityRecord

        d = src_dict.copy()
        schedules = []
        _schedules = d.pop("schedules")
        for componentsschemas_availability_records_item_data in _schedules:
            componentsschemas_availability_records_item = AvailabilityRecord.from_dict(
                componentsschemas_availability_records_item_data
            )

            schedules.append(componentsschemas_availability_records_item)

        result = cls(
            schedules=schedules,
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
