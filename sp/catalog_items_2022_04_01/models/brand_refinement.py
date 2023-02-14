from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="BrandRefinement")


@attr.s(auto_attribs=True)
class BrandRefinement:
    r"""Description of a brand that can be used to get more fine-grained search results.

    Attributes:
        number_of_results (int): The estimated number of results that would still be returned if refinement key applied.
        brand_name (str): Brand name. For display and can be used as a search refinement.
    """

    number_of_results: int
    brand_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number_of_results = self.number_of_results
        brand_name = self.brand_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numberOfResults": number_of_results,
                "brandName": brand_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number_of_results = d.pop("numberOfResults")

        brand_name = d.pop("brandName")

        result = cls(
            number_of_results=number_of_results,
            brand_name=brand_name,
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
