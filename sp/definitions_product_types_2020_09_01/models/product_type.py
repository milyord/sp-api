from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ProductType")


@attr.s(auto_attribs=True)
class ProductType:
    r"""An Amazon product type with a definition available.

    Attributes:
        name (str): The name of the Amazon product type.
        marketplace_ids (List[str]): The Amazon marketplace identifiers for which the product type definition is
            available.
    """

    name: str
    marketplace_ids: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        marketplace_ids = self.marketplace_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "marketplaceIds": marketplace_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        marketplace_ids = cast(List[str], d.pop("marketplaceIds"))

        result = cls(
            name=name,
            marketplace_ids=marketplace_ids,
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
