from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error


T = TypeVar("T", bound="ValidateContentDocumentAsinRelationsResponse")


@attr.s(auto_attribs=True)
class ValidateContentDocumentAsinRelationsResponse:
    r"""
    Attributes:
        errors (List['Error']): A list of error responses returned when a request is unsuccessful.
        warnings (Union[Unset, List['Error']]): A set of messages to the user, such as warnings or comments.
    """

    errors: List["Error"]
    warnings: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

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
                "errors": errors,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error

        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = Error.from_dict(errors_item_data)

            errors.append(errors_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for componentsschemas_message_set_item_data in _warnings or []:
            componentsschemas_message_set_item = Error.from_dict(componentsschemas_message_set_item_data)

            warnings.append(componentsschemas_message_set_item)

        result = cls(
            errors=errors,
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
