from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Money")


@attr.s(auto_attribs=True)
class Money:
    r"""The currency type and the amount.

    Attributes:
        currency_code (str): Three-digit currency code. In ISO 4217 format.
        amount (str): A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with
            currencies. Follows RFC7159 for number representation.
    """

    currency_code: str
    amount: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_code = self.currency_code
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyCode": currency_code,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency_code = d.pop("currencyCode")

        amount = d.pop("amount")

        result = cls(
            currency_code=currency_code,
            amount=amount,
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
