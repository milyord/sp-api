from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.feed_document_encryption_details_standard import FeedDocumentEncryptionDetailsStandard

T = TypeVar("T", bound="FeedDocumentEncryptionDetails")


@attr.s(auto_attribs=True)
class FeedDocumentEncryptionDetails:
    r"""Encryption details for required client-side encryption and decryption of document contents.

    Attributes:
        standard (FeedDocumentEncryptionDetailsStandard): The encryption standard required to encrypt or decrypt the
            document contents.
        initialization_vector (str): The vector to encrypt or decrypt the document contents using Cipher Block Chaining
            (CBC).
        key (str): The encryption key used to encrypt or decrypt the document contents.
    """

    standard: FeedDocumentEncryptionDetailsStandard
    initialization_vector: str
    key: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        standard = self.standard.value

        initialization_vector = self.initialization_vector
        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "standard": standard,
                "initializationVector": initialization_vector,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        standard = FeedDocumentEncryptionDetailsStandard(d.pop("standard"))

        initialization_vector = d.pop("initializationVector")

        key = d.pop("key")

        result = cls(
            standard=standard,
            initialization_vector=initialization_vector,
            key=key,
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
