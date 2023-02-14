from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.item_contributor_role import ItemContributorRole


T = TypeVar("T", bound="ItemContributor")


@attr.s(auto_attribs=True)
class ItemContributor:
    r"""Individual contributor to the creation of an item, such as an author or actor.

    Attributes:
        role (ItemContributorRole): Role of an individual contributor in the creation of an item, such as author or
            actor.
        value (str): Name of the contributor, such as Jane Austen.
    """

    role: "ItemContributorRole"
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.to_dict()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_contributor_role import ItemContributorRole

        d = src_dict.copy()
        role = ItemContributorRole.from_dict(d.pop("role"))

        value = d.pop("value")

        result = cls(
            role=role,
            value=value,
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
