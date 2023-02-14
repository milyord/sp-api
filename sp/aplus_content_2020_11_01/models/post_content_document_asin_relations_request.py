from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="PostContentDocumentAsinRelationsRequest")


@attr.s(auto_attribs=True)
class PostContentDocumentAsinRelationsRequest:
    r"""
    Attributes:
        asin_set (List[str]): The set of ASINs.
    """

    asin_set: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin_set = self.asin_set

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asinSet": asin_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asin_set = cast(List[str], d.pop("asinSet"))

        result = cls(
            asin_set=asin_set,
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
