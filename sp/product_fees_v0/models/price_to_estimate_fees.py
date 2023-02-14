from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money_type import MoneyType
    from ..models.points import Points


T = TypeVar("T", bound="PriceToEstimateFees")


@attr.s(auto_attribs=True)
class PriceToEstimateFees:
    r"""Price information for an item, used to estimate fees.

    Attributes:
        listing_price (MoneyType):
        shipping (Union[Unset, MoneyType]):
        points (Union[Unset, Points]):
    """

    listing_price: "MoneyType"
    shipping: Union[Unset, "MoneyType"] = UNSET
    points: Union[Unset, "Points"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        listing_price = self.listing_price.to_dict()

        shipping: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict()

        points: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.points, Unset):
            points = self.points.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ListingPrice": listing_price,
            }
        )
        if shipping is not UNSET:
            field_dict["Shipping"] = shipping
        if points is not UNSET:
            field_dict["Points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_type import MoneyType
        from ..models.points import Points

        d = src_dict.copy()
        listing_price = MoneyType.from_dict(d.pop("ListingPrice"))

        _shipping = d.pop("Shipping", UNSET)
        shipping: Union[Unset, MoneyType]
        if isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = MoneyType.from_dict(_shipping)

        _points = d.pop("Points", UNSET)
        points: Union[Unset, Points]
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = Points.from_dict(_points)

        result = cls(
            listing_price=listing_price,
            shipping=shipping,
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
