from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Points")


@attr.s(auto_attribs=True)
class Points:
    r"""The number of Amazon Points offered with the purchase of an item, and their monetary value. Note that the Points
    element is only returned in Japan (JP).

        Attributes:
            points_number (int):
    """

    points_number: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        points_number = self.points_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pointsNumber": points_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        points_number = d.pop("pointsNumber")

        result = cls(
            points_number=points_number,
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
