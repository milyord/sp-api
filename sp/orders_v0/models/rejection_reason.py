from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RejectionReason")


@attr.s(auto_attribs=True)
class RejectionReason:
    r"""The reason for rejecting the order's regulated information. Not present if the order isn't rejected.

    Attributes:
        rejection_reason_id (str): The unique identifier for the rejection reason.
        rejection_reason_description (str): The description of this rejection reason.
    """

    rejection_reason_id: str
    rejection_reason_description: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rejection_reason_id = self.rejection_reason_id
        rejection_reason_description = self.rejection_reason_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "RejectionReasonId": rejection_reason_id,
                "RejectionReasonDescription": rejection_reason_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rejection_reason_id = d.pop("RejectionReasonId")

        rejection_reason_description = d.pop("RejectionReasonDescription")

        result = cls(
            rejection_reason_id=rejection_reason_id,
            rejection_reason_description=rejection_reason_description,
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
