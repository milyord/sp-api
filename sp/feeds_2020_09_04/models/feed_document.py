from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.feed_document_compression_algorithm import FeedDocumentCompressionAlgorithm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feed_document_encryption_details import FeedDocumentEncryptionDetails


T = TypeVar("T", bound="FeedDocument")


@attr.s(auto_attribs=True)
class FeedDocument:
    r"""
    Attributes:
        feed_document_id (str): The identifier for the feed document. This identifier is unique only in combination with
            a seller ID.
        url (str): A presigned URL for the feed document. If `compressionAlgorithm` is not returned, you can download
            the feed directly from this URL. This URL expires after 5 minutes.
        encryption_details (FeedDocumentEncryptionDetails): Encryption details for required client-side encryption and
            decryption of document contents.
        compression_algorithm (Union[Unset, FeedDocumentCompressionAlgorithm]): If the feed document contents have been
            compressed, the compression algorithm used is returned in this property and you must decompress the feed when
            you download. Otherwise, you can download the feed directly. Refer to [Step 6. Download and decrypt the feed
            processing report](doc:feeds-api-v2020-09-04-use-case-guide#step-6-download-and-decrypt-the-feed-processing-
            report) in the use case guide, where sample code is provided.
    """

    feed_document_id: str
    url: str
    encryption_details: "FeedDocumentEncryptionDetails"
    compression_algorithm: Union[Unset, FeedDocumentCompressionAlgorithm] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feed_document_id = self.feed_document_id
        url = self.url
        encryption_details = self.encryption_details.to_dict()

        compression_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.compression_algorithm, Unset):
            compression_algorithm = self.compression_algorithm.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feedDocumentId": feed_document_id,
                "url": url,
                "encryptionDetails": encryption_details,
            }
        )
        if compression_algorithm is not UNSET:
            field_dict["compressionAlgorithm"] = compression_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feed_document_encryption_details import FeedDocumentEncryptionDetails

        d = src_dict.copy()
        feed_document_id = d.pop("feedDocumentId")

        url = d.pop("url")

        encryption_details = FeedDocumentEncryptionDetails.from_dict(d.pop("encryptionDetails"))

        _compression_algorithm = d.pop("compressionAlgorithm", UNSET)
        compression_algorithm: Union[Unset, FeedDocumentCompressionAlgorithm]
        if isinstance(_compression_algorithm, Unset):
            compression_algorithm = UNSET
        else:
            compression_algorithm = FeedDocumentCompressionAlgorithm(_compression_algorithm)

        result = cls(
            feed_document_id=feed_document_id,
            url=url,
            encryption_details=encryption_details,
            compression_algorithm=compression_algorithm,
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
