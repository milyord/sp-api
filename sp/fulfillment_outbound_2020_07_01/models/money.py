from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Money")


@attr.s(auto_attribs=True)
class Money:
    r"""An amount of money, including units in the form of currency.

    Attributes:
        currency_code (str): Three digit currency code in ISO 4217 format.
        value (str): A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with
            currencies. Follows RFC7159 for number representation.
    """

    currency_code: str
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_code = self.currency_code
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyCode": currency_code,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency_code = d.pop("currencyCode")

        value = d.pop("value")

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
