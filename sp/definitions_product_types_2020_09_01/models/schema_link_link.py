from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.schema_link_link_verb import SchemaLinkLinkVerb

T = TypeVar("T", bound="SchemaLinkLink")


@attr.s(auto_attribs=True)
class SchemaLinkLink:
    r"""Link to retrieve the schema.

    Attributes:
        resource (str): URI resource for the link.
        verb (SchemaLinkLinkVerb): HTTP method for the link operation.
    """

    resource: str
    verb: SchemaLinkLinkVerb
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource = self.resource
        verb = self.verb.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "verb": verb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resource = d.pop("resource")

        verb = SchemaLinkLinkVerb(d.pop("verb"))

        result = cls(
            resource=resource,
            verb=verb,
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
