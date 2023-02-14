from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ItemBrowseClassification")


@attr.s(auto_attribs=True)
class ItemBrowseClassification:
    r"""Classification (browse node) associated with an Amazon catalog item.

    Attributes:
        display_name (str): Display name for the classification.
        classification_id (str): Identifier of the classification (browse node identifier).
    """

    display_name: str
    classification_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        classification_id = self.classification_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "classificationId": classification_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName")

        classification_id = d.pop("classificationId")

        result = cls(
            display_name=display_name,
            classification_id=classification_id,
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
