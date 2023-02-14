from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.feed_document_encryption_details import FeedDocumentEncryptionDetails


T = TypeVar("T", bound="CreateFeedDocumentResult")


@attr.s(auto_attribs=True)
class CreateFeedDocumentResult:
    r"""Information required to encrypt and upload a feed document's contents.

    Attributes:
        feed_document_id (str): The identifier of the feed document.
        url (str): The presigned URL for uploading the feed contents. This URL expires after 5 minutes.
        encryption_details (FeedDocumentEncryptionDetails): Encryption details for required client-side encryption and
            decryption of document contents.
    """

    feed_document_id: str
    url: str
    encryption_details: "FeedDocumentEncryptionDetails"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feed_document_id = self.feed_document_id
        url = self.url
        encryption_details = self.encryption_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feedDocumentId": feed_document_id,
                "url": url,
                "encryptionDetails": encryption_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feed_document_encryption_details import FeedDocumentEncryptionDetails

        d = src_dict.copy()
        feed_document_id = d.pop("feedDocumentId")

        url = d.pop("url")

        encryption_details = FeedDocumentEncryptionDetails.from_dict(d.pop("encryptionDetails"))

        result = cls(
            feed_document_id=feed_document_id,
            url=url,
            encryption_details=encryption_details,
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
