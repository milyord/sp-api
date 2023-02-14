from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.additional_details_type import AdditionalDetailsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdditionalDetails")


@attr.s(auto_attribs=True)
class AdditionalDetails:
    r"""Additional information provided by the selling party for tax-related or any other purpose.

    Attributes:
        type (AdditionalDetailsType): The type of the additional information provided by the selling party.
        detail (str): The detail of the additional information provided by the selling party.
        language_code (Union[Unset, str]): The language code of the additional information detail.
    """

    type: AdditionalDetailsType
    detail: str
    language_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        detail = self.detail
        language_code = self.language_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "detail": detail,
            }
        )
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = AdditionalDetailsType(d.pop("type"))

        detail = d.pop("detail")

        language_code = d.pop("languageCode", UNSET)

        result = cls(
            type=type,
            detail=detail,
            language_code=language_code,
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
