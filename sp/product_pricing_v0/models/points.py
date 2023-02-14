from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money_type import MoneyType


T = TypeVar("T", bound="Points")


@attr.s(auto_attribs=True)
class Points:
    r"""
    Attributes:
        points_number (Union[Unset, int]): The number of points.
        points_monetary_value (Union[Unset, MoneyType]):
    """

    points_number: Union[Unset, int] = UNSET
    points_monetary_value: Union[Unset, "MoneyType"] = UNSET
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
        from ..models.money_type import MoneyType

        d = src_dict.copy()
        points_number = d.pop("PointsNumber", UNSET)

        _points_monetary_value = d.pop("PointsMonetaryValue", UNSET)
        points_monetary_value: Union[Unset, MoneyType]
        if isinstance(_points_monetary_value, Unset):
            points_monetary_value = UNSET
        else:
            points_monetary_value = MoneyType.from_dict(_points_monetary_value)

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
