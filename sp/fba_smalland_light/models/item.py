from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.money_type import MoneyType


T = TypeVar("T", bound="Item")


@attr.s(auto_attribs=True)
class Item:
    r"""An item to be sold.

    Attributes:
        asin (str): The Amazon Standard Identification Number (ASIN) value used to identify the item.
        price (MoneyType):
    """

    asin: str
    price: "MoneyType"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        price = self.price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asin": asin,
                "price": price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_type import MoneyType

        d = src_dict.copy()
        asin = d.pop("asin")

        price = MoneyType.from_dict(d.pop("price"))

        result = cls(
            asin=asin,
            price=price,
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
