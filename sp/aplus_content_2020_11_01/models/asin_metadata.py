from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.asin_badge import AsinBadge
from ..types import UNSET, Unset

T = TypeVar("T", bound="AsinMetadata")


@attr.s(auto_attribs=True)
class AsinMetadata:
    r"""The A+ Content ASIN with additional metadata for content management. If you don't include the `includedDataSet`
    parameter in a call to the listContentDocumentAsinRelations operation, the related ASINs are returned without
    metadata.

        Attributes:
            asin (str): The Amazon Standard Identification Number (ASIN).
            badge_set (Union[Unset, List[AsinBadge]]): The set of ASIN badges.
            parent (Union[Unset, str]): The Amazon Standard Identification Number (ASIN).
            title (Union[Unset, str]): The title for the ASIN in the Amazon catalog.
            image_url (Union[Unset, str]): The default image for the ASIN in the Amazon catalog.
            content_reference_key_set (Union[Unset, List[str]]): A set of content reference keys.
    """

    asin: str
    badge_set: Union[Unset, List[AsinBadge]] = UNSET
    parent: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    content_reference_key_set: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        badge_set: Union[Unset, List[str]] = UNSET
        if not isinstance(self.badge_set, Unset):
            badge_set = []
            for componentsschemas_asin_badge_set_item_data in self.badge_set:
                componentsschemas_asin_badge_set_item = componentsschemas_asin_badge_set_item_data.value

                badge_set.append(componentsschemas_asin_badge_set_item)

        parent = self.parent
        title = self.title
        image_url = self.image_url
        content_reference_key_set: Union[Unset, List[str]] = UNSET
        if not isinstance(self.content_reference_key_set, Unset):
            content_reference_key_set = self.content_reference_key_set

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asin": asin,
            }
        )
        if badge_set is not UNSET:
            field_dict["badgeSet"] = badge_set
        if parent is not UNSET:
            field_dict["parent"] = parent
        if title is not UNSET:
            field_dict["title"] = title
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if content_reference_key_set is not UNSET:
            field_dict["contentReferenceKeySet"] = content_reference_key_set

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asin = d.pop("asin")

        badge_set = []
        _badge_set = d.pop("badgeSet", UNSET)
        for componentsschemas_asin_badge_set_item_data in _badge_set or []:
            componentsschemas_asin_badge_set_item = AsinBadge(componentsschemas_asin_badge_set_item_data)

            badge_set.append(componentsschemas_asin_badge_set_item)

        parent = d.pop("parent", UNSET)

        title = d.pop("title", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        content_reference_key_set = cast(List[str], d.pop("contentReferenceKeySet", UNSET))

        result = cls(
            asin=asin,
            badge_set=badge_set,
            parent=parent,
            title=title,
            image_url=image_url,
            content_reference_key_set=content_reference_key_set,
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
