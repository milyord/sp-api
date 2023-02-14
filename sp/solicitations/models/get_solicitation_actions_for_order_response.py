from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.get_solicitation_actions_for_order_response_embedded import (
        GetSolicitationActionsForOrderResponseEmbedded,
    )
    from ..models.get_solicitation_actions_for_order_response_links import GetSolicitationActionsForOrderResponseLinks


T = TypeVar("T", bound="GetSolicitationActionsForOrderResponse")


@attr.s(auto_attribs=True)
class GetSolicitationActionsForOrderResponse:
    r"""The response schema for the getSolicitationActionsForOrder operation.

    Attributes:
        field_links (Union[Unset, GetSolicitationActionsForOrderResponseLinks]):
        field_embedded (Union[Unset, GetSolicitationActionsForOrderResponseEmbedded]):
        errors (Union[Unset, List['Error']]): A list of error responses returned when a request is unsuccessful.
    """

    field_links: Union[Unset, "GetSolicitationActionsForOrderResponseLinks"] = UNSET
    field_embedded: Union[Unset, "GetSolicitationActionsForOrderResponseEmbedded"] = UNSET
    errors: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_embedded: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

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
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.get_solicitation_actions_for_order_response_embedded import (
            GetSolicitationActionsForOrderResponseEmbedded,
        )
        from ..models.get_solicitation_actions_for_order_response_links import (
            GetSolicitationActionsForOrderResponseLinks,
        )

        d = src_dict.copy()
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, GetSolicitationActionsForOrderResponseLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = GetSolicitationActionsForOrderResponseLinks.from_dict(_field_links)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, GetSolicitationActionsForOrderResponseEmbedded]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = GetSolicitationActionsForOrderResponseEmbedded.from_dict(_field_embedded)

        errors = []
        _errors = d.pop("errors", UNSET)
        for componentsschemas_error_list_item_data in _errors or []:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            errors.append(componentsschemas_error_list_item)

        result = cls(
            field_links=field_links,
            field_embedded=field_embedded,
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
