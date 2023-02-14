from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.restriction import Restriction


T = TypeVar("T", bound="RestrictionList")


@attr.s(auto_attribs=True)
class RestrictionList:
    r"""A list of restrictions for the specified Amazon catalog item.

    Attributes:
        restrictions (List['Restriction']):
    """

    restrictions: List["Restriction"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        restrictions = []
        for restrictions_item_data in self.restrictions:
            restrictions_item = restrictions_item_data.to_dict()

            restrictions.append(restrictions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restrictions": restrictions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.restriction import Restriction

        d = src_dict.copy()
        restrictions = []
        _restrictions = d.pop("restrictions")
        for restrictions_item_data in _restrictions:
            restrictions_item = Restriction.from_dict(restrictions_item_data)

            restrictions.append(restrictions_item)

        result = cls(
            restrictions=restrictions,
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
