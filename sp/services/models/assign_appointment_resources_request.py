from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.appointment_resource import AppointmentResource


T = TypeVar("T", bound="AssignAppointmentResourcesRequest")


@attr.s(auto_attribs=True)
class AssignAppointmentResourcesRequest:
    r"""Request schema for the `assignAppointmentResources` operation.

    Attributes:
        resources (List['AppointmentResource']): List of resources that performs or performed job appointment
            fulfillment.
    """

    resources: List["AppointmentResource"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resources = []
        for componentsschemas_appointment_resources_item_data in self.resources:
            componentsschemas_appointment_resources_item = componentsschemas_appointment_resources_item_data.to_dict()

            resources.append(componentsschemas_appointment_resources_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resources": resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_resource import AppointmentResource

        d = src_dict.copy()
        resources = []
        _resources = d.pop("resources")
        for componentsschemas_appointment_resources_item_data in _resources:
            componentsschemas_appointment_resources_item = AppointmentResource.from_dict(
                componentsschemas_appointment_resources_item_data
            )

            resources.append(componentsschemas_appointment_resources_item)

        result = cls(
            resources=resources,
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
