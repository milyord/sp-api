from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.link_object import LinkObject


T = TypeVar("T", bound="GetSolicitationActionsForOrderResponseLinks")


@attr.s(auto_attribs=True)
class GetSolicitationActionsForOrderResponseLinks:
    r"""
    Attributes:
        self_ (LinkObject): A Link object.
        actions (List['LinkObject']): Eligible actions for the specified amazonOrderId.
    """

    self_: "LinkObject"
    actions: List["LinkObject"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_object import LinkObject

        d = src_dict.copy()
        self_ = LinkObject.from_dict(d.pop("self"))

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = LinkObject.from_dict(actions_item_data)

            actions.append(actions_item)

        result = cls(
            self_=self_,
            actions=actions,
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
