from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.invalid_item_reason_code import InvalidItemReasonCode

T = TypeVar("T", bound="InvalidItemReason")


@attr.s(auto_attribs=True)
class InvalidItemReason:
    r"""The reason that the item is invalid for return.

    Attributes:
        invalid_item_reason_code (InvalidItemReasonCode): A code for why the item is invalid for return.
        description (str): A human readable description of the invalid item reason code.
    """

    invalid_item_reason_code: InvalidItemReasonCode
    description: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invalid_item_reason_code = self.invalid_item_reason_code.value

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invalidItemReasonCode": invalid_item_reason_code,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invalid_item_reason_code = InvalidItemReasonCode(d.pop("invalidItemReasonCode"))

        description = d.pop("description")

        result = cls(
            invalid_item_reason_code=invalid_item_reason_code,
            description=description,
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
