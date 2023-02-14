from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.file_type import FileType

T = TypeVar("T", bound="FileContents")


@attr.s(auto_attribs=True)
class FileContents:
    r"""The document data and checksum.

    Attributes:
        contents (str): Data for printing labels, in the form of a Base64-encoded, GZip-compressed string.
        file_type (FileType): The file type for a label.
        checksum (str): An MD5 hash to validate the PDF document data, in the form of a Base64-encoded string.
    """

    contents: str
    file_type: FileType
    checksum: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contents = self.contents
        file_type = self.file_type.value

        checksum = self.checksum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Contents": contents,
                "FileType": file_type,
                "Checksum": checksum,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contents = d.pop("Contents")

        file_type = FileType(d.pop("FileType"))

        checksum = d.pop("Checksum")

        result = cls(
            contents=contents,
            file_type=file_type,
            checksum=checksum,
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
