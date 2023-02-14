from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.get_inventory_summaries_result import GetInventorySummariesResult
    from ..models.pagination import Pagination


T = TypeVar("T", bound="GetInventorySummariesResponse")


@attr.s(auto_attribs=True)
class GetInventorySummariesResponse:
    r"""The Response schema.

    Attributes:
        payload (Union[Unset, GetInventorySummariesResult]): The payload schema for the getInventorySummaries operation.
        pagination (Union[Unset, Pagination]): The process of returning the results to a request in batches of a defined
            size called pages. This is done to exercise some control over result size and overall throughput. It's a form of
            traffic management.
        errors (Union[Unset, List['Error']]): A list of error responses returned when a request is unsuccessful.
    """

    payload: Union[Unset, "GetInventorySummariesResult"] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    errors: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemas_error_list_item_data in self.errors:
                componentsschemas_error_list_item = componentsschemas_error_list_item_data.to_dict()

                errors.append(componentsschemas_error_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.get_inventory_summaries_result import GetInventorySummariesResult
        from ..models.pagination import Pagination

        d = src_dict.copy()
        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, GetInventorySummariesResult]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = GetInventorySummariesResult.from_dict(_payload)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        errors = []
        _errors = d.pop("errors", UNSET)
        for componentsschemas_error_list_item_data in _errors or []:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            errors.append(componentsschemas_error_list_item)

        result = cls(
            payload=payload,
            pagination=pagination,
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
