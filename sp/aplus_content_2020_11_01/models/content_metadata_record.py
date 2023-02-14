from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.content_metadata import ContentMetadata


T = TypeVar("T", bound="ContentMetadataRecord")


@attr.s(auto_attribs=True)
class ContentMetadataRecord:
    r"""The metadata for an A+ Content document, with additional information for content management.

    Attributes:
        content_reference_key (str): A unique reference key for the A+ Content document. A content reference key cannot
            form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content
            identifier.
        content_metadata (ContentMetadata): The metadata of an A+ Content document.
    """

    content_reference_key: str
    content_metadata: "ContentMetadata"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_reference_key = self.content_reference_key
        content_metadata = self.content_metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentReferenceKey": content_reference_key,
                "contentMetadata": content_metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_metadata import ContentMetadata

        d = src_dict.copy()
        content_reference_key = d.pop("contentReferenceKey")

        content_metadata = ContentMetadata.from_dict(d.pop("contentMetadata"))

        result = cls(
            content_reference_key=content_reference_key,
            content_metadata=content_metadata,
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
