from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.categories_parent import CategoriesParent


T = TypeVar("T", bound="Categories")


@attr.s(auto_attribs=True)
class Categories:
    r"""
    Attributes:
        product_category_id (Union[Unset, str]): The identifier for the product category (or browse node).
        product_category_name (Union[Unset, str]): The name of the product category (or browse node).
        parent (Union[Unset, CategoriesParent]): The parent product category.
    """

    product_category_id: Union[Unset, str] = UNSET
    product_category_name: Union[Unset, str] = UNSET
    parent: Union[Unset, "CategoriesParent"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_category_id = self.product_category_id
        product_category_name = self.product_category_name
        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_category_id is not UNSET:
            field_dict["ProductCategoryId"] = product_category_id
        if product_category_name is not UNSET:
            field_dict["ProductCategoryName"] = product_category_name
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.categories_parent import CategoriesParent

        d = src_dict.copy()
        product_category_id = d.pop("ProductCategoryId", UNSET)

        product_category_name = d.pop("ProductCategoryName", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, CategoriesParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = CategoriesParent.from_dict(_parent)

        result = cls(
            product_category_id=product_category_id,
            product_category_name=product_category_name,
            parent=parent,
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
