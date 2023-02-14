from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_text_pair_block import StandardTextPairBlock
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardTechSpecsModule")


@attr.s(auto_attribs=True)
class StandardTechSpecsModule:
    r"""The standard table of technical feature names and definitions.

    Attributes:
        specification_list (List['StandardTextPairBlock']): The specification list.
        headline (Union[Unset, TextComponent]): Rich text content.
        table_count (Union[Unset, int]): The number of tables to present. Features are evenly divided between the
            tables.
    """

    specification_list: List["StandardTextPairBlock"]
    headline: Union[Unset, "TextComponent"] = UNSET
    table_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        specification_list = []
        for specification_list_item_data in self.specification_list:
            specification_list_item = specification_list_item_data.to_dict()

            specification_list.append(specification_list_item)

        headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headline, Unset):
            headline = self.headline.to_dict()

        table_count = self.table_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "specificationList": specification_list,
            }
        )
        if headline is not UNSET:
            field_dict["headline"] = headline
        if table_count is not UNSET:
            field_dict["tableCount"] = table_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standard_text_pair_block import StandardTextPairBlock
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        specification_list = []
        _specification_list = d.pop("specificationList")
        for specification_list_item_data in _specification_list:
            specification_list_item = StandardTextPairBlock.from_dict(specification_list_item_data)

            specification_list.append(specification_list_item)

        _headline = d.pop("headline", UNSET)
        headline: Union[Unset, TextComponent]
        if isinstance(_headline, Unset):
            headline = UNSET
        else:
            headline = TextComponent.from_dict(_headline)

        table_count = d.pop("tableCount", UNSET)

        result = cls(
            specification_list=specification_list,
            headline=headline,
            table_count=table_count,
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
