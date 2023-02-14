from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.link_object import LinkObject


T = TypeVar("T", bound="GetSolicitationActionResponseLinks")


@attr.s(auto_attribs=True)
class GetSolicitationActionResponseLinks:
    r"""
    Attributes:
        self_ (LinkObject): A Link object.
        schema (LinkObject): A Link object.
    """

    self_: "LinkObject"
    schema: "LinkObject"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "schema": schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_object import LinkObject

        d = src_dict.copy()
        self_ = LinkObject.from_dict(d.pop("self"))

        schema = LinkObject.from_dict(d.pop("schema"))

        result = cls(
            self_=self_,
            schema=schema,
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
