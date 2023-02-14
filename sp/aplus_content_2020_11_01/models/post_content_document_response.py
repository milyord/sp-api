from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error


T = TypeVar("T", bound="PostContentDocumentResponse")


@attr.s(auto_attribs=True)
class PostContentDocumentResponse:
    r"""
    Attributes:
        content_reference_key (str): A unique reference key for the A+ Content document. A content reference key cannot
            form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content
            identifier.
        warnings (Union[Unset, List['Error']]): A set of messages to the user, such as warnings or comments.
    """

    content_reference_key: str
    warnings: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_reference_key = self.content_reference_key
        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemas_message_set_item_data in self.warnings:
                componentsschemas_message_set_item = componentsschemas_message_set_item_data.to_dict()

                warnings.append(componentsschemas_message_set_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentReferenceKey": content_reference_key,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error

        d = src_dict.copy()
        content_reference_key = d.pop("contentReferenceKey")

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for componentsschemas_message_set_item_data in _warnings or []:
            componentsschemas_message_set_item = Error.from_dict(componentsschemas_message_set_item_data)

            warnings.append(componentsschemas_message_set_item)

        result = cls(
            content_reference_key=content_reference_key,
            warnings=warnings,
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
