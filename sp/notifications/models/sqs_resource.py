from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SqsResource")


@attr.s(auto_attribs=True)
class SqsResource:
    r"""The information required to create an Amazon Simple Queue Service (Amazon SQS) queue destination.

    Attributes:
        arn (str): The Amazon Resource Name (ARN) associated with the SQS queue.
    """

    arn: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        arn = self.arn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "arn": arn,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        arn = d.pop("arn")

        result = cls(
            arn=arn,
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
