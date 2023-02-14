from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.currency_code import CurrencyCode

T = TypeVar("T", bound="Amount")


@attr.s(auto_attribs=True)
class Amount:
    r"""The monetary value.

    Attributes:
        currency_code (CurrencyCode): The currency code.
        value (float):
    """

    currency_code: CurrencyCode
    value: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_code = self.currency_code.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CurrencyCode": currency_code,
                "Value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency_code = CurrencyCode(d.pop("CurrencyCode"))

        value = d.pop("Value")

        result = cls(
            currency_code=currency_code,
            value=value,
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
