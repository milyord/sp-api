from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_offer_by_marketplace_offer_type import ItemOfferByMarketplaceOfferType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money
    from ..models.points import Points


T = TypeVar("T", bound="ItemOfferByMarketplace")


@attr.s(auto_attribs=True)
class ItemOfferByMarketplace:
    r"""Offer details of a listings item for an Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        offer_type (ItemOfferByMarketplaceOfferType): Type of offer for the listings item.
        price (Money): The currency type and the amount.
        points (Union[Unset, Points]): The number of Amazon Points offered with the purchase of an item, and their
            monetary value. Note that the Points element is only returned in Japan (JP).
    """

    marketplace_id: str
    offer_type: ItemOfferByMarketplaceOfferType
    price: "Money"
    points: Union[Unset, "Points"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        offer_type = self.offer_type.value

        price = self.price.to_dict()

        points: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.points, Unset):
            points = self.points.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "offerType": offer_type,
                "price": price,
            }
        )
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money
        from ..models.points import Points

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        offer_type = ItemOfferByMarketplaceOfferType(d.pop("offerType"))

        price = Money.from_dict(d.pop("price"))

        _points = d.pop("points", UNSET)
        points: Union[Unset, Points]
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = Points.from_dict(_points)

        result = cls(
            marketplace_id=marketplace_id,
            offer_type=offer_type,
            price=price,
            points=points,
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
