from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.link_verb import LinkVerb
from ..types import UNSET, Unset

T = TypeVar("T", bound="Link")


@attr.s(auto_attribs=True)
class Link:
    r"""A link to resources related to a listing restriction.

    Attributes:
        resource (str): The URI of the related resource.
        verb (LinkVerb): The HTTP verb used to interact with the related resource.
        title (Union[Unset, str]): The title of the related resource.
        type (Union[Unset, str]): The media type of the related resource.
    """

    resource: str
    verb: LinkVerb
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource = self.resource
        verb = self.verb.value

        title = self.title
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "verb": verb,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resource = d.pop("resource")

        verb = LinkVerb(d.pop("verb"))

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        result = cls(
            resource=resource,
            verb=verb,
            title=title,
            type=type,
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
