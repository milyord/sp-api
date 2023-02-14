from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.scheduled_package_id import ScheduledPackageId
    from ..models.time_slot import TimeSlot


T = TypeVar("T", bound="UpdatePackageDetails")


@attr.s(auto_attribs=True)
class UpdatePackageDetails:
    r"""Request to update the time slot of a package.

    Attributes:
        scheduled_package_id (ScheduledPackageId): Identifies the scheduled package to be updated.
        package_time_slot (TimeSlot): A time window to hand over an Easy Ship package to Amazon Logistics.
    """

    scheduled_package_id: "ScheduledPackageId"
    package_time_slot: "TimeSlot"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheduled_package_id = self.scheduled_package_id.to_dict()

        package_time_slot = self.package_time_slot.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduledPackageId": scheduled_package_id,
                "packageTimeSlot": package_time_slot,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scheduled_package_id import ScheduledPackageId
        from ..models.time_slot import TimeSlot

        d = src_dict.copy()
        scheduled_package_id = ScheduledPackageId.from_dict(d.pop("scheduledPackageId"))

        package_time_slot = TimeSlot.from_dict(d.pop("packageTimeSlot"))

        result = cls(
            scheduled_package_id=scheduled_package_id,
            package_time_slot=package_time_slot,
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
