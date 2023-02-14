from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feed import Feed


T = TypeVar("T", bound="GetFeedsResponse")


@attr.s(auto_attribs=True)
class GetFeedsResponse:
    r"""Response schema.

    Attributes:
        feeds (List['Feed']): A list of feeds.
        next_token (Union[Unset, str]): Returned when the number of results exceeds pageSize. To get the next page of
            results, call the getFeeds operation with this token as the only parameter.
    """

    feeds: List["Feed"]
    next_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feeds = []
        for componentsschemas_feed_list_item_data in self.feeds:
            componentsschemas_feed_list_item = componentsschemas_feed_list_item_data.to_dict()

            feeds.append(componentsschemas_feed_list_item)

        next_token = self.next_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feeds": feeds,
            }
        )
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feed import Feed

        d = src_dict.copy()
        feeds = []
        _feeds = d.pop("feeds")
        for componentsschemas_feed_list_item_data in _feeds:
            componentsschemas_feed_list_item = Feed.from_dict(componentsschemas_feed_list_item_data)

            feeds.append(componentsschemas_feed_list_item)

        next_token = d.pop("nextToken", UNSET)

        result = cls(
            feeds=feeds,
            next_token=next_token,
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
