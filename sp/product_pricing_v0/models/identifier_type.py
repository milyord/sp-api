from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asin_identifier import ASINIdentifier
    from ..models.seller_sku_identifier import SellerSKUIdentifier


T = TypeVar("T", bound="IdentifierType")


@attr.s(auto_attribs=True)
class IdentifierType:
    r"""Specifies the identifiers used to uniquely identify an item.

    Attributes:
        marketplace_asin (ASINIdentifier):
        sku_identifier (Union[Unset, SellerSKUIdentifier]):
    """

    marketplace_asin: "ASINIdentifier"
    sku_identifier: Union[Unset, "SellerSKUIdentifier"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_asin = self.marketplace_asin.to_dict()

        sku_identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_identifier, Unset):
            sku_identifier = self.sku_identifier.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "MarketplaceASIN": marketplace_asin,
            }
        )
        if sku_identifier is not UNSET:
            field_dict["SKUIdentifier"] = sku_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asin_identifier import ASINIdentifier
        from ..models.seller_sku_identifier import SellerSKUIdentifier

        d = src_dict.copy()
        marketplace_asin = ASINIdentifier.from_dict(d.pop("MarketplaceASIN"))

        _sku_identifier = d.pop("SKUIdentifier", UNSET)
        sku_identifier: Union[Unset, SellerSKUIdentifier]
        if isinstance(_sku_identifier, Unset):
            sku_identifier = UNSET
        else:
            sku_identifier = SellerSKUIdentifier.from_dict(_sku_identifier)

        result = cls(
            marketplace_asin=marketplace_asin,
            sku_identifier=sku_identifier,
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
