from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ClassificationRefinement")


@attr.s(auto_attribs=True)
class ClassificationRefinement:
    r"""Description of a classification that can be used to get more fine-grained search results.

    Attributes:
        number_of_results (int): The estimated number of results that would still be returned if refinement key applied.
        display_name (str): Display name for the classification.
        classification_id (str): Identifier for the classification that can be used for search refinement purposes.
    """

    number_of_results: int
    display_name: str
    classification_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number_of_results = self.number_of_results
        display_name = self.display_name
        classification_id = self.classification_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numberOfResults": number_of_results,
                "displayName": display_name,
                "classificationId": classification_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number_of_results = d.pop("numberOfResults")

        display_name = d.pop("displayName")

        classification_id = d.pop("classificationId")

        result = cls(
            number_of_results=number_of_results,
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
