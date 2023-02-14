from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.brand_refinement import BrandRefinement
    from ..models.classification_refinement import ClassificationRefinement


T = TypeVar("T", bound="Refinements")


@attr.s(auto_attribs=True)
class Refinements:
    r"""Search refinements.

    Attributes:
        brands (List['BrandRefinement']): Brand search refinements.
        classifications (List['ClassificationRefinement']): Classification search refinements.
    """

    brands: List["BrandRefinement"]
    classifications: List["ClassificationRefinement"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        brands = []
        for brands_item_data in self.brands:
            brands_item = brands_item_data.to_dict()

            brands.append(brands_item)

        classifications = []
        for classifications_item_data in self.classifications:
            classifications_item = classifications_item_data.to_dict()

            classifications.append(classifications_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brands": brands,
                "classifications": classifications,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.brand_refinement import BrandRefinement
        from ..models.classification_refinement import ClassificationRefinement

        d = src_dict.copy()
        brands = []
        _brands = d.pop("brands")
        for brands_item_data in _brands:
            brands_item = BrandRefinement.from_dict(brands_item_data)

            brands.append(brands_item)

        classifications = []
        _classifications = d.pop("classifications")
        for classifications_item_data in _classifications:
            classifications_item = ClassificationRefinement.from_dict(classifications_item_data)

            classifications.append(classifications_item)

        result = cls(
            brands=brands,
            classifications=classifications,
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
