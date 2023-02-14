from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.get_solicitation_action_response import GetSolicitationActionResponse


T = TypeVar("T", bound="GetSolicitationActionsForOrderResponseEmbedded")


@attr.s(auto_attribs=True)
class GetSolicitationActionsForOrderResponseEmbedded:
    r"""
    Attributes:
        actions (List['GetSolicitationActionResponse']):
    """

    actions: List["GetSolicitationActionResponse"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_solicitation_action_response import GetSolicitationActionResponse

        d = src_dict.copy()
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = GetSolicitationActionResponse.from_dict(actions_item_data)

            actions.append(actions_item)

        result = cls(
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
