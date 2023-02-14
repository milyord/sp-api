from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.issue_severity import IssueSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="Issue")


@attr.s(auto_attribs=True)
class Issue:
    r"""An issue with a listings item.

    Attributes:
        code (str): An issue code that identifies the type of issue.
        message (str): A message that describes the issue.
        severity (IssueSeverity): The severity of the issue.
        attribute_name (Union[Unset, str]): Name of the attribute associated with the issue, if applicable.
    """

    code: str
    message: str
    severity: IssueSeverity
    attribute_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        message = self.message
        severity = self.severity.value

        attribute_name = self.attribute_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "severity": severity,
            }
        )
        if attribute_name is not UNSET:
            field_dict["attributeName"] = attribute_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        message = d.pop("message")

        severity = IssueSeverity(d.pop("severity"))

        attribute_name = d.pop("attributeName", UNSET)

        result = cls(
            code=code,
            message=message,
            severity=severity,
            attribute_name=attribute_name,
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
