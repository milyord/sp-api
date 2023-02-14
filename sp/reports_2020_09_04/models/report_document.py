from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.report_document_compression_algorithm import ReportDocumentCompressionAlgorithm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_document_encryption_details import ReportDocumentEncryptionDetails


T = TypeVar("T", bound="ReportDocument")


@attr.s(auto_attribs=True)
class ReportDocument:
    r"""
    Attributes:
        report_document_id (str): The identifier for the report document. This identifier is unique only in combination
            with a seller ID.
        url (str): A presigned URL for the report document. If `compressionAlgorithm` is not returned, you can download
            the report directly from this URL. This URL expires after 5 minutes.
        encryption_details (ReportDocumentEncryptionDetails): Encryption details required for decryption of a report
            document's contents.
        compression_algorithm (Union[Unset, ReportDocumentCompressionAlgorithm]): If the report document contents have
            been compressed, the compression algorithm used is returned in this property and you must decompress the report
            when you download. Otherwise, you can download the report directly. Refer to [Step 2. Download and decrypt the
            report](doc:reports-api-v2020-09-04-use-case-guide#step-2-download-and-decrypt-the-report) in the use case
            guide, where sample code is provided.
    """

    report_document_id: str
    url: str
    encryption_details: "ReportDocumentEncryptionDetails"
    compression_algorithm: Union[Unset, ReportDocumentCompressionAlgorithm] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_document_id = self.report_document_id
        url = self.url
        encryption_details = self.encryption_details.to_dict()

        compression_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.compression_algorithm, Unset):
            compression_algorithm = self.compression_algorithm.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportDocumentId": report_document_id,
                "url": url,
                "encryptionDetails": encryption_details,
            }
        )
        if compression_algorithm is not UNSET:
            field_dict["compressionAlgorithm"] = compression_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_document_encryption_details import ReportDocumentEncryptionDetails

        d = src_dict.copy()
        report_document_id = d.pop("reportDocumentId")

        url = d.pop("url")

        encryption_details = ReportDocumentEncryptionDetails.from_dict(d.pop("encryptionDetails"))

        _compression_algorithm = d.pop("compressionAlgorithm", UNSET)
        compression_algorithm: Union[Unset, ReportDocumentCompressionAlgorithm]
        if isinstance(_compression_algorithm, Unset):
            compression_algorithm = UNSET
        else:
            compression_algorithm = ReportDocumentCompressionAlgorithm(_compression_algorithm)

        result = cls(
            report_document_id=report_document_id,
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
