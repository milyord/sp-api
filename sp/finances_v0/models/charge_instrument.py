from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="ChargeInstrument")


@attr.s(auto_attribs=True)
class ChargeInstrument:
    r"""A payment instrument.

    Attributes:
        description (Union[Unset, str]): A short description of the charge instrument.
        tail (Union[Unset, str]): The account tail (trailing digits) of the charge instrument.
        amount (Union[Unset, Currency]): A currency type and amount.
    """

    description: Union[Unset, str] = UNSET
    tail: Union[Unset, str] = UNSET
    amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        tail = self.tail
        amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["Description"] = description
        if tail is not UNSET:
            field_dict["Tail"] = tail
        if amount is not UNSET:
            field_dict["Amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        description = d.pop("Description", UNSET)

        tail = d.pop("Tail", UNSET)

        _amount = d.pop("Amount", UNSET)
        amount: Union[Unset, Currency]
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        result = cls(
            description=description,
            tail=tail,
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
