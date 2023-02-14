from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.destination_resource import DestinationResource


T = TypeVar("T", bound="Destination")


@attr.s(auto_attribs=True)
class Destination:
    r"""Represents a destination created when you call the createDestination operation.

    Attributes:
        name (str): The developer-defined name for this destination.
        destination_id (str): The destination identifier generated when you created the destination.
        resource (DestinationResource): The destination resource types.
    """

    name: str
    destination_id: str
    resource: "DestinationResource"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        destination_id = self.destination_id
        resource = self.resource.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "destinationId": destination_id,
                "resource": resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.destination_resource import DestinationResource

        d = src_dict.copy()
        name = d.pop("name")

        destination_id = d.pop("destinationId")

        resource = DestinationResource.from_dict(d.pop("resource"))

        result = cls(
            name=name,
            destination_id=destination_id,
            resource=resource,
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
