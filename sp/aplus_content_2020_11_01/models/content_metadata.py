import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.content_badge import ContentBadge
from ..models.content_status import ContentStatus

T = TypeVar("T", bound="ContentMetadata")


@attr.s(auto_attribs=True)
class ContentMetadata:
    r"""The metadata of an A+ Content document.

    Attributes:
        name (str): The A+ Content document name.
        marketplace_id (str): The identifier for the marketplace where the A+ Content is published.
        status (ContentStatus): The submission status of the content document.
        badge_set (List[ContentBadge]): The set of content badges.
        update_time (datetime.datetime): The approximate age of the A+ Content document and metadata.
    """

    name: str
    marketplace_id: str
    status: ContentStatus
    badge_set: List[ContentBadge]
    update_time: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        marketplace_id = self.marketplace_id
        status = self.status.value

        badge_set = []
        for componentsschemas_content_badge_set_item_data in self.badge_set:
            componentsschemas_content_badge_set_item = componentsschemas_content_badge_set_item_data.value

            badge_set.append(componentsschemas_content_badge_set_item)

        update_time = self.update_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "marketplaceId": marketplace_id,
                "status": status,
                "badgeSet": badge_set,
                "updateTime": update_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        marketplace_id = d.pop("marketplaceId")

        status = ContentStatus(d.pop("status"))

        badge_set = []
        _badge_set = d.pop("badgeSet")
        for componentsschemas_content_badge_set_item_data in _badge_set:
            componentsschemas_content_badge_set_item = ContentBadge(componentsschemas_content_badge_set_item_data)

            badge_set.append(componentsschemas_content_badge_set_item)

        update_time = isoparse(d.pop("updateTime"))

        result = cls(
            name=name,
            marketplace_id=marketplace_id,
            status=status,
            badge_set=badge_set,
            update_time=update_time,
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
