from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimensions import Dimensions
    from ..models.weight import Weight


T = TypeVar("T", bound="Pallet")


@attr.s(auto_attribs=True)
class Pallet:
    r"""Pallet information.

    Attributes:
        dimensions (Dimensions): The dimension values and unit of measurement.
        is_stacked (bool): Indicates whether pallets will be stacked when carrier arrives for pick-up.
        weight (Union[Unset, Weight]): The weight of the package.
    """

    dimensions: "Dimensions"
    is_stacked: bool
    weight: Union[Unset, "Weight"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dimensions = self.dimensions.to_dict()

        is_stacked = self.is_stacked
        weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Dimensions": dimensions,
                "IsStacked": is_stacked,
            }
        )
        if weight is not UNSET:
            field_dict["Weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dimensions import Dimensions
        from ..models.weight import Weight

        d = src_dict.copy()
        dimensions = Dimensions.from_dict(d.pop("Dimensions"))

        is_stacked = d.pop("IsStacked")

        _weight = d.pop("Weight", UNSET)
        weight: Union[Unset, Weight]
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = Weight.from_dict(_weight)

        result = cls(
            dimensions=dimensions,
            is_stacked=is_stacked,
            weight=weight,
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
