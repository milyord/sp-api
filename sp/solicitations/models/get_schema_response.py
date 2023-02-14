from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.get_schema_response_links import GetSchemaResponseLinks
    from ..models.schema import Schema


T = TypeVar("T", bound="GetSchemaResponse")


@attr.s(auto_attribs=True)
class GetSchemaResponse:
    r"""
    Attributes:
        field_links (Union[Unset, GetSchemaResponseLinks]):
        payload (Union[Unset, Schema]): A JSON schema document describing the expected payload of the action. This
            object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-
            schema.org/draft-04/schema</a>.
        errors (Union[Unset, List['Error']]): A list of error responses returned when a request is unsuccessful.
    """

    field_links: Union[Unset, "GetSchemaResponseLinks"] = UNSET
    payload: Union[Unset, "Schema"] = UNSET
    errors: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemas_error_list_item_data in self.errors:
                componentsschemas_error_list_item = componentsschemas_error_list_item_data.to_dict()

                errors.append(componentsschemas_error_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if payload is not UNSET:
            field_dict["payload"] = payload
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.get_schema_response_links import GetSchemaResponseLinks
        from ..models.schema import Schema

        d = src_dict.copy()
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, GetSchemaResponseLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = GetSchemaResponseLinks.from_dict(_field_links)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, Schema]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = Schema.from_dict(_payload)

        errors = []
        _errors = d.pop("errors", UNSET)
        for componentsschemas_error_list_item_data in _errors or []:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            errors.append(componentsschemas_error_list_item)

        result = cls(
            field_links=field_links,
            payload=payload,
            errors=errors,
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
