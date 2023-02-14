from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateFeedDocumentSpecification")


@attr.s(auto_attribs=True)
class CreateFeedDocumentSpecification:
    r"""Specifies the content type for the createFeedDocument operation.

    Attributes:
        content_type (str): The content type of the feed.
    """

    content_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_type = self.content_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentType": content_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_type = d.pop("contentType")

        result = cls(
            content_type=content_type,
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
