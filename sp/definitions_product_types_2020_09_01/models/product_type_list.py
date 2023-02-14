from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.product_type import ProductType


T = TypeVar("T", bound="ProductTypeList")


@attr.s(auto_attribs=True)
class ProductTypeList:
    r"""A list of Amazon product types with definitions available.

    Attributes:
        product_types (List['ProductType']):
    """

    product_types: List["ProductType"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_types = []
        for product_types_item_data in self.product_types:
            product_types_item = product_types_item_data.to_dict()

            product_types.append(product_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productTypes": product_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_type import ProductType

        d = src_dict.copy()
        product_types = []
        _product_types = d.pop("productTypes")
        for product_types_item_data in _product_types:
            product_types_item = ProductType.from_dict(product_types_item_data)

            product_types.append(product_types_item)

        result = cls(
            product_types=product_types,
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
