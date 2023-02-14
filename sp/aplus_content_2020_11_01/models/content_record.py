from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_document import ContentDocument
    from ..models.content_metadata import ContentMetadata


T = TypeVar("T", bound="ContentRecord")


@attr.s(auto_attribs=True)
class ContentRecord:
    r"""A content document with additional information for content management.

    Attributes:
        content_reference_key (str): A unique reference key for the A+ Content document. A content reference key cannot
            form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content
            identifier.
        content_metadata (Union[Unset, ContentMetadata]): The metadata of an A+ Content document.
        content_document (Union[Unset, ContentDocument]): The A+ Content document. This is the enhanced content that is
            published to product detail pages.
    """

    content_reference_key: str
    content_metadata: Union[Unset, "ContentMetadata"] = UNSET
    content_document: Union[Unset, "ContentDocument"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_reference_key = self.content_reference_key
        content_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content_metadata, Unset):
            content_metadata = self.content_metadata.to_dict()

        content_document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content_document, Unset):
            content_document = self.content_document.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentReferenceKey": content_reference_key,
            }
        )
        if content_metadata is not UNSET:
            field_dict["contentMetadata"] = content_metadata
        if content_document is not UNSET:
            field_dict["contentDocument"] = content_document

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_document import ContentDocument
        from ..models.content_metadata import ContentMetadata

        d = src_dict.copy()
        content_reference_key = d.pop("contentReferenceKey")

        _content_metadata = d.pop("contentMetadata", UNSET)
        content_metadata: Union[Unset, ContentMetadata]
        if isinstance(_content_metadata, Unset):
            content_metadata = UNSET
        else:
            content_metadata = ContentMetadata.from_dict(_content_metadata)

        _content_document = d.pop("contentDocument", UNSET)
        content_document: Union[Unset, ContentDocument]
        if isinstance(_content_document, Unset):
            content_document = UNSET
        else:
            content_document = ContentDocument.from_dict(_content_document)

        result = cls(
            content_reference_key=content_reference_key,
            content_metadata=content_metadata,
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
