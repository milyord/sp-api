from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="FeaturedOfferExpectedPriceRequestParams")


@attr.s(auto_attribs=True)
class FeaturedOfferExpectedPriceRequestParams:
    r"""The parameters for an individual request.

    Attributes:
        marketplace_id (str): A marketplace identifier. Specifies the marketplace for which data is returned.
        sku (str): The seller SKU of the item.
    """

    marketplace_id: str
    sku: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        sku = self.sku

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "sku": sku,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        sku = d.pop("sku")

        result = cls(
            marketplace_id=marketplace_id,
            sku=sku,
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
