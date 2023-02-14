from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.content_document import ContentDocument


T = TypeVar("T", bound="PostContentDocumentRequest")


@attr.s(auto_attribs=True)
class PostContentDocumentRequest:
    r"""
    Attributes:
        content_document (ContentDocument): The A+ Content document. This is the enhanced content that is published to
            product detail pages.
    """

    content_document: "ContentDocument"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_document = self.content_document.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentDocument": content_document,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_document import ContentDocument

        d = src_dict.copy()
        content_document = ContentDocument.from_dict(d.pop("contentDocument"))

        result = cls(
            content_document=content_document,
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
