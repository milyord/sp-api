from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.fee_name import FeeName

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="Fee")


@attr.s(auto_attribs=True)
class Fee:
    r"""Fee type and cost.

    Attributes:
        name (FeeName): The type of fee.
        amount (Money): An amount of money, including units in the form of currency.
    """

    name: FeeName
    amount: "Money"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name.value

        amount = self.amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        name = FeeName(d.pop("name"))

        amount = Money.from_dict(d.pop("amount"))

        result = cls(
            name=name,
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
