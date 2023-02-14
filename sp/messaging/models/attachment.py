from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Attachment")


@attr.s(auto_attribs=True)
class Attachment:
    r"""Represents a file uploaded to a destination that was created by the
    [createUploadDestinationForResource](doc:uploads-api-reference#post-uploads2020-11-01uploaddestinationsresource)
    operation of the Selling Partner API for Uploads.

        Attributes:
            upload_destination_id (str): The identifier of the upload destination. Get this value by calling the
                [createUploadDestinationForResource](doc:uploads-api-reference#post-uploads2020-11-01uploaddestinationsresource)
                operation of the Uploads API.
            file_name (str): The name of the file, including the extension. This is the file name that will appear in the
                message. This does not need to match the file name of the file that you uploaded.
    """

    upload_destination_id: str
    file_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upload_destination_id = self.upload_destination_id
        file_name = self.file_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadDestinationId": upload_destination_id,
                "fileName": file_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        upload_destination_id = d.pop("uploadDestinationId")

        file_name = d.pop("fileName")

        result = cls(
            upload_destination_id=upload_destination_id,
            file_name=file_name,
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
