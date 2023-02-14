from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.destination_resource_specification import DestinationResourceSpecification


T = TypeVar("T", bound="CreateDestinationRequest")


@attr.s(auto_attribs=True)
class CreateDestinationRequest:
    r"""The request schema for the createDestination operation.

    Attributes:
        resource_specification (DestinationResourceSpecification): The information required to create a destination
            resource. Applications should use one resource type (sqs or eventBridge) per destination.
        name (str): A developer-defined name to help identify this destination.
    """

    resource_specification: "DestinationResourceSpecification"
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_specification = self.resource_specification.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceSpecification": resource_specification,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.destination_resource_specification import DestinationResourceSpecification

        d = src_dict.copy()
        resource_specification = DestinationResourceSpecification.from_dict(d.pop("resourceSpecification"))

        name = d.pop("name")

        result = cls(
            resource_specification=resource_specification,
            name=name,
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
