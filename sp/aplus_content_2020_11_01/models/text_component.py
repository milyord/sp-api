from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decorator import Decorator


T = TypeVar("T", bound="TextComponent")


@attr.s(auto_attribs=True)
class TextComponent:
    r"""Rich text content.

    Attributes:
        value (str): The actual plain text.
        decorator_set (Union[Unset, List['Decorator']]): A set of content decorators.
    """

    value: str
    decorator_set: Union[Unset, List["Decorator"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        decorator_set: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.decorator_set, Unset):
            decorator_set = []
            for componentsschemas_decorator_set_item_data in self.decorator_set:
                componentsschemas_decorator_set_item = componentsschemas_decorator_set_item_data.to_dict()

                decorator_set.append(componentsschemas_decorator_set_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if decorator_set is not UNSET:
            field_dict["decoratorSet"] = decorator_set

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.decorator import Decorator

        d = src_dict.copy()
        value = d.pop("value")

        decorator_set = []
        _decorator_set = d.pop("decoratorSet", UNSET)
        for componentsschemas_decorator_set_item_data in _decorator_set or []:
            componentsschemas_decorator_set_item = Decorator.from_dict(componentsschemas_decorator_set_item_data)

            decorator_set.append(componentsschemas_decorator_set_item)

        result = cls(
            value=value,
            decorator_set=decorator_set,
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
