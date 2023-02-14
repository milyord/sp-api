from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competitive_price_type import CompetitivePriceType
    from ..models.money_type import MoneyType
    from ..models.offer_listing_count_type import OfferListingCountType


T = TypeVar("T", bound="CompetitivePricingType")


@attr.s(auto_attribs=True)
class CompetitivePricingType:
    r"""Competitive pricing information for the item.

    Attributes:
        competitive_prices (List['CompetitivePriceType']): A list of competitive pricing information.
        number_of_offer_listings (List['OfferListingCountType']): The number of active offer listings for the item that
            was submitted. The listing count is returned by condition, one for each listing condition value that is
            returned.
        trade_in_value (Union[Unset, MoneyType]):
    """

    competitive_prices: List["CompetitivePriceType"]
    number_of_offer_listings: List["OfferListingCountType"]
    trade_in_value: Union[Unset, "MoneyType"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        competitive_prices = []
        for componentsschemas_competitive_price_list_item_data in self.competitive_prices:
            componentsschemas_competitive_price_list_item = componentsschemas_competitive_price_list_item_data.to_dict()

            competitive_prices.append(componentsschemas_competitive_price_list_item)

        number_of_offer_listings = []
        for componentsschemas_number_of_offer_listings_list_item_data in self.number_of_offer_listings:
            componentsschemas_number_of_offer_listings_list_item = (
                componentsschemas_number_of_offer_listings_list_item_data.to_dict()
            )

            number_of_offer_listings.append(componentsschemas_number_of_offer_listings_list_item)

        trade_in_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trade_in_value, Unset):
            trade_in_value = self.trade_in_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CompetitivePrices": competitive_prices,
                "NumberOfOfferListings": number_of_offer_listings,
            }
        )
        if trade_in_value is not UNSET:
            field_dict["TradeInValue"] = trade_in_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competitive_price_type import CompetitivePriceType
        from ..models.money_type import MoneyType
        from ..models.offer_listing_count_type import OfferListingCountType

        d = src_dict.copy()
        competitive_prices = []
        _competitive_prices = d.pop("CompetitivePrices")
        for componentsschemas_competitive_price_list_item_data in _competitive_prices:
            componentsschemas_competitive_price_list_item = CompetitivePriceType.from_dict(
                componentsschemas_competitive_price_list_item_data
            )

            competitive_prices.append(componentsschemas_competitive_price_list_item)

        number_of_offer_listings = []
        _number_of_offer_listings = d.pop("NumberOfOfferListings")
        for componentsschemas_number_of_offer_listings_list_item_data in _number_of_offer_listings:
            componentsschemas_number_of_offer_listings_list_item = OfferListingCountType.from_dict(
                componentsschemas_number_of_offer_listings_list_item_data
            )

            number_of_offer_listings.append(componentsschemas_number_of_offer_listings_list_item)

        _trade_in_value = d.pop("TradeInValue", UNSET)
        trade_in_value: Union[Unset, MoneyType]
        if isinstance(_trade_in_value, Unset):
            trade_in_value = UNSET
        else:
            trade_in_value = MoneyType.from_dict(_trade_in_value)

        result = cls(
            competitive_prices=competitive_prices,
            number_of_offer_listings=number_of_offer_listings,
            trade_in_value=trade_in_value,
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
