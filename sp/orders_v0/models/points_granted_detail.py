from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="PointsGrantedDetail")


@attr.s(auto_attribs=True)
class PointsGrantedDetail:
    r"""The number of Amazon Points offered with the purchase of an item, and their monetary value.

    Attributes:
        points_number (Union[Unset, int]): The number of Amazon Points granted with the purchase of an item.
        points_monetary_value (Union[Unset, Money]): The monetary value of the order.
    """

    points_number: Union[Unset, int] = UNSET
    points_monetary_value: Union[Unset, "Money"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        points_number = self.points_number
        points_monetary_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.points_monetary_value, Unset):
            points_monetary_value = self.points_monetary_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if points_number is not UNSET:
            field_dict["PointsNumber"] = points_number
        if points_monetary_value is not UNSET:
            field_dict["PointsMonetaryValue"] = points_monetary_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        points_number = d.pop("PointsNumber", UNSET)

        _points_monetary_value = d.pop("PointsMonetaryValue", UNSET)
        points_monetary_value: Union[Unset, Money]
        if isinstance(_points_monetary_value, Unset):
            points_monetary_value = UNSET
        else:
            points_monetary_value = Money.from_dict(_points_monetary_value)

        result = cls(
            points_number=points_number,
            points_monetary_value=points_monetary_value,
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
