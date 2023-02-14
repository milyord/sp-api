from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.weight import Weight


T = TypeVar("T", bound="ContainerItem")


@attr.s(auto_attribs=True)
class ContainerItem:
    r"""Item in the container.

    Attributes:
        quantity (float): The quantity of the items of this type in the container.
        unit_price (Currency): The total value of all items in the container.
        unit_weight (Weight): The weight.
        title (str): A descriptive title of the item.
    """

    quantity: float
    unit_price: "Currency"
    unit_weight: "Weight"
    title: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        unit_price = self.unit_price.to_dict()

        unit_weight = self.unit_weight.to_dict()

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "unitPrice": unit_price,
                "unitWeight": unit_weight,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.weight import Weight

        d = src_dict.copy()
        quantity = d.pop("quantity")

        unit_price = Currency.from_dict(d.pop("unitPrice"))

        unit_weight = Weight.from_dict(d.pop("unitWeight"))

        title = d.pop("title")

        result = cls(
            quantity=quantity,
            unit_price=unit_price,
            unit_weight=unit_weight,
            title=title,
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
