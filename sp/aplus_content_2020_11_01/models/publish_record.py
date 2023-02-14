from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.content_type import ContentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishRecord")


@attr.s(auto_attribs=True)
class PublishRecord:
    r"""The full context for an A+ Content publishing event.

    Attributes:
        marketplace_id (str): The identifier for the marketplace where the A+ Content is published.
        locale (str): The IETF language tag. This only supports the primary language subtag with one secondary language
            subtag. The secondary language subtag is almost always a regional designation. This does not support additional
            subtags beyond the primary and secondary subtags.
            **Pattern:** ^[a-z]{2,}-[A-Z0-9]{2,}$
        asin (str): The Amazon Standard Identification Number (ASIN).
        content_type (ContentType): The A+ Content document type.
        content_reference_key (str): A unique reference key for the A+ Content document. A content reference key cannot
            form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content
            identifier.
        content_sub_type (Union[Unset, str]): The A+ Content document subtype. This represents a special-purpose type of
            an A+ Content document. Not every A+ Content document type will have a subtype, and subtypes may change at any
            time.
    """

    marketplace_id: str
    locale: str
    asin: str
    content_type: ContentType
    content_reference_key: str
    content_sub_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        locale = self.locale
        asin = self.asin
        content_type = self.content_type.value

        content_reference_key = self.content_reference_key
        content_sub_type = self.content_sub_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "locale": locale,
                "asin": asin,
                "contentType": content_type,
                "contentReferenceKey": content_reference_key,
            }
        )
        if content_sub_type is not UNSET:
            field_dict["contentSubType"] = content_sub_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        locale = d.pop("locale")

        asin = d.pop("asin")

        content_type = ContentType(d.pop("contentType"))

        content_reference_key = d.pop("contentReferenceKey")

        content_sub_type = d.pop("contentSubType", UNSET)

        result = cls(
            marketplace_id=marketplace_id,
            locale=locale,
            asin=asin,
            content_type=content_type,
            content_reference_key=content_reference_key,
            content_sub_type=content_sub_type,
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
