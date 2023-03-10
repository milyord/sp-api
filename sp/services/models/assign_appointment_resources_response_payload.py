from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.warning import Warning_


T = TypeVar("T", bound="AssignAppointmentResourcesResponsePayload")


@attr.s(auto_attribs=True)
class AssignAppointmentResourcesResponsePayload:
    r"""The payload for the `assignAppointmentResource` operation.

    Attributes:
        warnings (Union[Unset, List['Warning_']]): A list of warnings returned in the sucessful execution response of an
            API request.
    """

    warnings: Union[Unset, List["Warning_"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemas_warning_list_item_data in self.warnings:
                componentsschemas_warning_list_item = componentsschemas_warning_list_item_data.to_dict()

                warnings.append(componentsschemas_warning_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.warning import Warning_

        d = src_dict.copy()
        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for componentsschemas_warning_list_item_data in _warnings or []:
            componentsschemas_warning_list_item = Warning_.from_dict(componentsschemas_warning_list_item_data)

            warnings.append(componentsschemas_warning_list_item)

        result = cls(
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
