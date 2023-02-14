from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money_type import MoneyType
    from ..models.points import Points


T = TypeVar("T", bound="Price")


@attr.s(auto_attribs=True)
class Price:
    r"""
    Attributes:
        listing_price (MoneyType):
        shipping_price (Union[Unset, MoneyType]):
        points (Union[Unset, Points]):
    """

    listing_price: "MoneyType"
    shipping_price: Union[Unset, "MoneyType"] = UNSET
    points: Union[Unset, "Points"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        listing_price = self.listing_price.to_dict()

        shipping_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_price, Unset):
            shipping_price = self.shipping_price.to_dict()

        points: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.points, Unset):
            points = self.points.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listingPrice": listing_price,
            }
        )
        if shipping_price is not UNSET:
            field_dict["shippingPrice"] = shipping_price
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_type import MoneyType
        from ..models.points import Points

        d = src_dict.copy()
        listing_price = MoneyType.from_dict(d.pop("listingPrice"))

        _shipping_price = d.pop("shippingPrice", UNSET)
        shipping_price: Union[Unset, MoneyType]
        if isinstance(_shipping_price, Unset):
            shipping_price = UNSET
        else:
            shipping_price = MoneyType.from_dict(_shipping_price)

        _points = d.pop("points", UNSET)
        points: Union[Unset, Points]
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = Points.from_dict(_points)

        result = cls(
            listing_price=listing_price,
            shipping_price=shipping_price,
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
