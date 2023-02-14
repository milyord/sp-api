from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.fulfillment_type import FulfillmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferIdentifier")


@attr.s(auto_attribs=True)
class OfferIdentifier:
    r"""Identifies an offer from a particular seller on an ASIN.

    Attributes:
        marketplace_id (str): A marketplace identifier. Specifies the marketplace for which data is returned.
        asin (str): The Amazon Standard Identification Number (ASIN) of the item.
        seller_id (Union[Unset, str]): The seller identifier for the offer.
        sku (Union[Unset, str]): The seller stock keeping unit (SKU) of the item. This will only be present for the
            target offer, which belongs to the requesting seller.
        fulfillment_type (Union[Unset, FulfillmentType]): Indicates whether the item is fulfilled by Amazon or by the
            seller (merchant).
    """

    marketplace_id: str
    asin: str
    seller_id: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    fulfillment_type: Union[Unset, FulfillmentType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        asin = self.asin
        seller_id = self.seller_id
        sku = self.sku
        fulfillment_type: Union[Unset, str] = UNSET
        if not isinstance(self.fulfillment_type, Unset):
            fulfillment_type = self.fulfillment_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "asin": asin,
            }
        )
        if seller_id is not UNSET:
            field_dict["sellerId"] = seller_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if fulfillment_type is not UNSET:
            field_dict["fulfillmentType"] = fulfillment_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        asin = d.pop("asin")

        seller_id = d.pop("sellerId", UNSET)

        sku = d.pop("sku", UNSET)

        _fulfillment_type = d.pop("fulfillmentType", UNSET)
        fulfillment_type: Union[Unset, FulfillmentType]
        if isinstance(_fulfillment_type, Unset):
            fulfillment_type = UNSET
        else:
            fulfillment_type = FulfillmentType(_fulfillment_type)

        result = cls(
            marketplace_id=marketplace_id,
            asin=asin,
            seller_id=seller_id,
            sku=sku,
            fulfillment_type=fulfillment_type,
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
