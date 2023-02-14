from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.content_type import ContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_module import ContentModule


T = TypeVar("T", bound="ContentDocument")


@attr.s(auto_attribs=True)
class ContentDocument:
    r"""The A+ Content document. This is the enhanced content that is published to product detail pages.

    Attributes:
        name (str): The A+ Content document name.
        content_type (ContentType): The A+ Content document type.
        locale (str): The IETF language tag. This only supports the primary language subtag with one secondary language
            subtag. The secondary language subtag is almost always a regional designation. This does not support additional
            subtags beyond the primary and secondary subtags.
            **Pattern:** ^[a-z]{2,}-[A-Z0-9]{2,}$
        content_module_list (List['ContentModule']): A list of A+ Content modules.
        content_sub_type (Union[Unset, str]): The A+ Content document subtype. This represents a special-purpose type of
            an A+ Content document. Not every A+ Content document type will have a subtype, and subtypes may change at any
            time.
    """

    name: str
    content_type: ContentType
    locale: str
    content_module_list: List["ContentModule"]
    content_sub_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        content_type = self.content_type.value

        locale = self.locale
        content_module_list = []
        for componentsschemas_content_module_list_item_data in self.content_module_list:
            componentsschemas_content_module_list_item = componentsschemas_content_module_list_item_data.to_dict()

            content_module_list.append(componentsschemas_content_module_list_item)

        content_sub_type = self.content_sub_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "contentType": content_type,
                "locale": locale,
                "contentModuleList": content_module_list,
            }
        )
        if content_sub_type is not UNSET:
            field_dict["contentSubType"] = content_sub_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_module import ContentModule

        d = src_dict.copy()
        name = d.pop("name")

        content_type = ContentType(d.pop("contentType"))

        locale = d.pop("locale")

        content_module_list = []
        _content_module_list = d.pop("contentModuleList")
        for componentsschemas_content_module_list_item_data in _content_module_list:
            componentsschemas_content_module_list_item = ContentModule.from_dict(
                componentsschemas_content_module_list_item_data
            )

            content_module_list.append(componentsschemas_content_module_list_item)

        content_sub_type = d.pop("contentSubType", UNSET)

        result = cls(
            name=name,
            content_type=content_type,
            locale=locale,
            content_module_list=content_module_list,
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
