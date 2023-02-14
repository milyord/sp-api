from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.feed import Feed


T = TypeVar("T", bound="GetFeedsResponse")


@attr.s(auto_attribs=True)
class GetFeedsResponse:
    r"""Response schema.

    Attributes:
        payload (Union[Unset, List['Feed']]):
        next_token (Union[Unset, str]): Returned when the number of results exceeds pageSize. To get the next page of
            results, call the getFeeds operation with this token as the only parameter.
        errors (Union[Unset, List['Error']]): A list of error responses returned when a request is unsuccessful.
    """

    payload: Union[Unset, List["Feed"]] = UNSET
    next_token: Union[Unset, str] = UNSET
    errors: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payload: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = []
            for componentsschemas_feed_list_item_data in self.payload:
                componentsschemas_feed_list_item = componentsschemas_feed_list_item_data.to_dict()

                payload.append(componentsschemas_feed_list_item)

        next_token = self.next_token
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
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.feed import Feed

        d = src_dict.copy()
        payload = []
        _payload = d.pop("payload", UNSET)
        for componentsschemas_feed_list_item_data in _payload or []:
            componentsschemas_feed_list_item = Feed.from_dict(componentsschemas_feed_list_item_data)

            payload.append(componentsschemas_feed_list_item)

        next_token = d.pop("nextToken", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for componentsschemas_error_list_item_data in _errors or []:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            errors.append(componentsschemas_error_list_item)

        result = cls(
            payload=payload,
            next_token=next_token,
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