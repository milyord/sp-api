from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReasonCodeDetails")


@attr.s(auto_attribs=True)
class ReasonCodeDetails:
    r"""A return reason code, a description, and an optional description translation.

    Attributes:
        return_reason_code (str): A code that indicates a valid return reason.
        description (str): A human readable description of the return reason code.
        translated_description (Union[Unset, str]): A translation of the description. The translation is in the language
            specified in the Language request parameter.
    """

    return_reason_code: str
    description: str
    translated_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_reason_code = self.return_reason_code
        description = self.description
        translated_description = self.translated_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnReasonCode": return_reason_code,
                "description": description,
            }
        )
        if translated_description is not UNSET:
            field_dict["translatedDescription"] = translated_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_reason_code = d.pop("returnReasonCode")

        description = d.pop("description")

        translated_description = d.pop("translatedDescription", UNSET)

        result = cls(
            return_reason_code=return_reason_code,
            description=description,
            translated_description=translated_description,
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
