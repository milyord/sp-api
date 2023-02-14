from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ASINIdentifier")


@attr.s(auto_attribs=True)
class ASINIdentifier:
    r"""
    Attributes:
        marketplace_id (str): A marketplace identifier.
        asin (str): The Amazon Standard Identification Number (ASIN) of the item.
    """

    marketplace_id: str
    asin: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        asin = self.asin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "MarketplaceId": marketplace_id,
                "ASIN": asin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("MarketplaceId")

        asin = d.pop("ASIN")

        result = cls(
            marketplace_id=marketplace_id,
            asin=asin,
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
