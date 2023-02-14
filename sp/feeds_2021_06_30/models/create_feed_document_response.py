from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateFeedDocumentResponse")


@attr.s(auto_attribs=True)
class CreateFeedDocumentResponse:
    r"""Information required to upload a feed document's contents.

    Attributes:
        feed_document_id (str): The identifier of the feed document.
        url (str): The presigned URL for uploading the feed contents. This URL expires after 5 minutes.
    """

    feed_document_id: str
    url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feed_document_id = self.feed_document_id
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feedDocumentId": feed_document_id,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feed_document_id = d.pop("feedDocumentId")

        url = d.pop("url")

        result = cls(
            feed_document_id=feed_document_id,
            url=url,
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
