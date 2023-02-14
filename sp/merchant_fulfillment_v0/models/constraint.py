from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Constraint")


@attr.s(auto_attribs=True)
class Constraint:
    r"""A validation constraint.

    Attributes:
        validation_string (str): A validation string.
        validation_reg_ex (Union[Unset, str]): A regular expression.
    """

    validation_string: str
    validation_reg_ex: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        validation_string = self.validation_string
        validation_reg_ex = self.validation_reg_ex

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ValidationString": validation_string,
            }
        )
        if validation_reg_ex is not UNSET:
            field_dict["ValidationRegEx"] = validation_reg_ex

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        validation_string = d.pop("ValidationString")

        validation_reg_ex = d.pop("ValidationRegEx", UNSET)

        result = cls(
            validation_string=validation_string,
            validation_reg_ex=validation_reg_ex,
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
