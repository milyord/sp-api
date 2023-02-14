from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemClassificationSalesRank")


@attr.s(auto_attribs=True)
class ItemClassificationSalesRank:
    r"""Sales rank of an Amazon catalog item by classification.

    Attributes:
        classification_id (str): Identifier of the classification associated with the sales rank.
        title (str): Title, or name, of the sales rank.
        rank (int): Sales rank value.
        link (Union[Unset, str]): Corresponding Amazon retail website link, or URL, for the sales rank.
    """

    classification_id: str
    title: str
    rank: int
    link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        classification_id = self.classification_id
        title = self.title
        rank = self.rank
        link = self.link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "classificationId": classification_id,
                "title": title,
                "rank": rank,
            }
        )
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        classification_id = d.pop("classificationId")

        title = d.pop("title")

        rank = d.pop("rank")

        link = d.pop("link", UNSET)

        result = cls(
            classification_id=classification_id,
            title=title,
            rank=rank,
            link=link,
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
