from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplaceFilter")


@attr.s(auto_attribs=True)
class MarketplaceFilter:
    r"""Use this event filter to customize your subscription to send notifications for only the specified marketplaceId's.

    Attributes:
        marketplace_ids (Union[Unset, List[str]]): A list of marketplace identifiers to subscribe to (e.g.
            ATVPDKIKX0DER). To receive notifications in every marketplace, do not provide this list.
    """

    marketplace_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.marketplace_ids, Unset):
            marketplace_ids = self.marketplace_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if marketplace_ids is not UNSET:
            field_dict["marketplaceIds"] = marketplace_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_ids = cast(List[str], d.pop("marketplaceIds", UNSET))

        result = cls(
            marketplace_ids=marketplace_ids,
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
