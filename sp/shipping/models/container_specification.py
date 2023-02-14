from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.dimensions import Dimensions
    from ..models.weight import Weight


T = TypeVar("T", bound="ContainerSpecification")


@attr.s(auto_attribs=True)
class ContainerSpecification:
    r"""Container specification for checking the service rate.

    Attributes:
        dimensions (Dimensions): A set of measurements for a three-dimensional object.
        weight (Weight): The weight.
    """

    dimensions: "Dimensions"
    weight: "Weight"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dimensions = self.dimensions.to_dict()

        weight = self.weight.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dimensions": dimensions,
                "weight": weight,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dimensions import Dimensions
        from ..models.weight import Weight

        d = src_dict.copy()
        dimensions = Dimensions.from_dict(d.pop("dimensions"))

        weight = Weight.from_dict(d.pop("weight"))

        result = cls(
            dimensions=dimensions,
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
