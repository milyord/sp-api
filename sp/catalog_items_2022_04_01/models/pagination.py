from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pagination")


@attr.s(auto_attribs=True)
class Pagination:
    r"""When a request produces a response that exceeds the `pageSize`, pagination occurs. This means the response is
    divided into individual pages. To retrieve the next page or the previous page, you must pass the `nextToken` value
    or the `previousToken` value as the `pageToken` parameter in the next request. When you receive the last page, there
    will be no `nextToken` key in the pagination object.

        Attributes:
            next_token (Union[Unset, str]): A token that can be used to fetch the next page.
            previous_token (Union[Unset, str]): A token that can be used to fetch the previous page.
    """

    next_token: Union[Unset, str] = UNSET
    previous_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_token = self.next_token
        previous_token = self.previous_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token
        if previous_token is not UNSET:
            field_dict["previousToken"] = previous_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        next_token = d.pop("nextToken", UNSET)

        previous_token = d.pop("previousToken", UNSET)

        result = cls(
            next_token=next_token,
            previous_token=previous_token,
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
