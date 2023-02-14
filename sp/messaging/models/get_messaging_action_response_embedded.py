from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_schema_response import GetSchemaResponse


T = TypeVar("T", bound="GetMessagingActionResponseEmbedded")


@attr.s(auto_attribs=True)
class GetMessagingActionResponseEmbedded:
    r"""
    Attributes:
        schema (Union[Unset, GetSchemaResponse]):
    """

    schema: Union[Unset, "GetSchemaResponse"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_schema_response import GetSchemaResponse

        d = src_dict.copy()
        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, GetSchemaResponse]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = GetSchemaResponse.from_dict(_schema)

        result = cls(
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
