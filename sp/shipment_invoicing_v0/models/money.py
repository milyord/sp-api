from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Money")


@attr.s(auto_attribs=True)
class Money:
    r"""The currency type and amount.

    Attributes:
        currency_code (Union[Unset, str]): Three-digit currency code in ISO 4217 format.
        amount (Union[Unset, str]): The currency amount.
    """

    currency_code: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_code = self.currency_code
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["CurrencyCode"] = currency_code
        if amount is not UNSET:
            field_dict["Amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency_code = d.pop("CurrencyCode", UNSET)

        amount = d.pop("Amount", UNSET)

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
