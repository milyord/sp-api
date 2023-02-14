from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Price")


@attr.s(auto_attribs=True)
class Price:
    r"""The price attribute of the item.

    Attributes:
        amount (Union[Unset, float]): The amount.
        currency_code (Union[Unset, str]): The currency code of the amount.
    """

    amount: Union[Unset, float] = UNSET
    currency_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        currency_code = self.currency_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["Amount"] = amount
        if currency_code is not UNSET:
            field_dict["CurrencyCode"] = currency_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("Amount", UNSET)

        currency_code = d.pop("CurrencyCode", UNSET)

        result = cls(
            amount=amount,
            currency_code=currency_code,
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
