from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_metadata_record import ContentMetadataRecord
    from ..models.error import Error


T = TypeVar("T", bound="SearchContentDocumentsResponse")


@attr.s(auto_attribs=True)
class SearchContentDocumentsResponse:
    r"""
    Attributes:
        content_metadata_records (List['ContentMetadataRecord']): A list of A+ Content metadata records.
        warnings (Union[Unset, List['Error']]): A set of messages to the user, such as warnings or comments.
        next_page_token (Union[Unset, str]): A page token that is returned when the results of the call exceed the page
            size. To get another page of results, call the operation again, passing in this value with the pageToken
            parameter.
    """

    content_metadata_records: List["ContentMetadataRecord"]
    warnings: Union[Unset, List["Error"]] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_metadata_records = []
        for componentsschemas_content_metadata_record_list_item_data in self.content_metadata_records:
            componentsschemas_content_metadata_record_list_item = (
                componentsschemas_content_metadata_record_list_item_data.to_dict()
            )

            content_metadata_records.append(componentsschemas_content_metadata_record_list_item)

        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemas_message_set_item_data in self.warnings:
                componentsschemas_message_set_item = componentsschemas_message_set_item_data.to_dict()

                warnings.append(componentsschemas_message_set_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentMetadataRecords": content_metadata_records,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_metadata_record import ContentMetadataRecord
        from ..models.error import Error

        d = src_dict.copy()
        content_metadata_records = []
        _content_metadata_records = d.pop("contentMetadataRecords")
        for componentsschemas_content_metadata_record_list_item_data in _content_metadata_records:
            componentsschemas_content_metadata_record_list_item = ContentMetadataRecord.from_dict(
                componentsschemas_content_metadata_record_list_item_data
            )

            content_metadata_records.append(componentsschemas_content_metadata_record_list_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for componentsschemas_message_set_item_data in _warnings or []:
            componentsschemas_message_set_item = Error.from_dict(componentsschemas_message_set_item_data)

            warnings.append(componentsschemas_message_set_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        result = cls(
            content_metadata_records=content_metadata_records,
            warnings=warnings,
            next_page_token=next_page_token,
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
