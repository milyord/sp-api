import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buy_box_price_type import BuyBoxPriceType
    from ..models.lowest_price_type import LowestPriceType
    from ..models.money_type import MoneyType
    from ..models.offer_count_type import OfferCountType
    from ..models.sales_rank_type import SalesRankType


T = TypeVar("T", bound="Summary")


@attr.s(auto_attribs=True)
class Summary:
    r"""Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the
    SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.

        Attributes:
            total_offer_count (int): The number of unique offers contained in NumberOfOffers.
            number_of_offers (Union[Unset, List['OfferCountType']]):
            lowest_prices (Union[Unset, List['LowestPriceType']]):
            buy_box_prices (Union[Unset, List['BuyBoxPriceType']]):
            list_price (Union[Unset, MoneyType]):
            competitive_price_threshold (Union[Unset, MoneyType]):
            suggested_lower_price_plus_shipping (Union[Unset, MoneyType]):
            sales_rankings (Union[Unset, List['SalesRankType']]): A list of sales rank information for the item, by
                category.
            buy_box_eligible_offers (Union[Unset, List['OfferCountType']]):
            offers_available_time (Union[Unset, datetime.datetime]): When the status is ActiveButTooSoonForProcessing, this
                is the time when the offers will be available for processing.
    """

    total_offer_count: int
    number_of_offers: Union[Unset, List["OfferCountType"]] = UNSET
    lowest_prices: Union[Unset, List["LowestPriceType"]] = UNSET
    buy_box_prices: Union[Unset, List["BuyBoxPriceType"]] = UNSET
    list_price: Union[Unset, "MoneyType"] = UNSET
    competitive_price_threshold: Union[Unset, "MoneyType"] = UNSET
    suggested_lower_price_plus_shipping: Union[Unset, "MoneyType"] = UNSET
    sales_rankings: Union[Unset, List["SalesRankType"]] = UNSET
    buy_box_eligible_offers: Union[Unset, List["OfferCountType"]] = UNSET
    offers_available_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_offer_count = self.total_offer_count
        number_of_offers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.number_of_offers, Unset):
            number_of_offers = []
            for componentsschemas_number_of_offers_item_data in self.number_of_offers:
                componentsschemas_number_of_offers_item = componentsschemas_number_of_offers_item_data.to_dict()

                number_of_offers.append(componentsschemas_number_of_offers_item)

        lowest_prices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lowest_prices, Unset):
            lowest_prices = []
            for componentsschemas_lowest_prices_item_data in self.lowest_prices:
                componentsschemas_lowest_prices_item = componentsschemas_lowest_prices_item_data.to_dict()

                lowest_prices.append(componentsschemas_lowest_prices_item)

        buy_box_prices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buy_box_prices, Unset):
            buy_box_prices = []
            for componentsschemas_buy_box_prices_item_data in self.buy_box_prices:
                componentsschemas_buy_box_prices_item = componentsschemas_buy_box_prices_item_data.to_dict()

                buy_box_prices.append(componentsschemas_buy_box_prices_item)

        list_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.list_price, Unset):
            list_price = self.list_price.to_dict()

        competitive_price_threshold: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competitive_price_threshold, Unset):
            competitive_price_threshold = self.competitive_price_threshold.to_dict()

        suggested_lower_price_plus_shipping: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suggested_lower_price_plus_shipping, Unset):
            suggested_lower_price_plus_shipping = self.suggested_lower_price_plus_shipping.to_dict()

        sales_rankings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_rankings, Unset):
            sales_rankings = []
            for componentsschemas_sales_rank_list_item_data in self.sales_rankings:
                componentsschemas_sales_rank_list_item = componentsschemas_sales_rank_list_item_data.to_dict()

                sales_rankings.append(componentsschemas_sales_rank_list_item)

        buy_box_eligible_offers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buy_box_eligible_offers, Unset):
            buy_box_eligible_offers = []
            for componentsschemas_buy_box_eligible_offers_item_data in self.buy_box_eligible_offers:
                componentsschemas_buy_box_eligible_offers_item = (
                    componentsschemas_buy_box_eligible_offers_item_data.to_dict()
                )

                buy_box_eligible_offers.append(componentsschemas_buy_box_eligible_offers_item)

        offers_available_time: Union[Unset, str] = UNSET
        if not isinstance(self.offers_available_time, Unset):
            offers_available_time = self.offers_available_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TotalOfferCount": total_offer_count,
            }
        )
        if number_of_offers is not UNSET:
            field_dict["NumberOfOffers"] = number_of_offers
        if lowest_prices is not UNSET:
            field_dict["LowestPrices"] = lowest_prices
        if buy_box_prices is not UNSET:
            field_dict["BuyBoxPrices"] = buy_box_prices
        if list_price is not UNSET:
            field_dict["ListPrice"] = list_price
        if competitive_price_threshold is not UNSET:
            field_dict["CompetitivePriceThreshold"] = competitive_price_threshold
        if suggested_lower_price_plus_shipping is not UNSET:
            field_dict["SuggestedLowerPricePlusShipping"] = suggested_lower_price_plus_shipping
        if sales_rankings is not UNSET:
            field_dict["SalesRankings"] = sales_rankings
        if buy_box_eligible_offers is not UNSET:
            field_dict["BuyBoxEligibleOffers"] = buy_box_eligible_offers
        if offers_available_time is not UNSET:
            field_dict["OffersAvailableTime"] = offers_available_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.buy_box_price_type import BuyBoxPriceType
        from ..models.lowest_price_type import LowestPriceType
        from ..models.money_type import MoneyType
        from ..models.offer_count_type import OfferCountType
        from ..models.sales_rank_type import SalesRankType

        d = src_dict.copy()
        total_offer_count = d.pop("TotalOfferCount")

        number_of_offers = []
        _number_of_offers = d.pop("NumberOfOffers", UNSET)
        for componentsschemas_number_of_offers_item_data in _number_of_offers or []:
            componentsschemas_number_of_offers_item = OfferCountType.from_dict(
                componentsschemas_number_of_offers_item_data
            )

            number_of_offers.append(componentsschemas_number_of_offers_item)

        lowest_prices = []
        _lowest_prices = d.pop("LowestPrices", UNSET)
        for componentsschemas_lowest_prices_item_data in _lowest_prices or []:
            componentsschemas_lowest_prices_item = LowestPriceType.from_dict(componentsschemas_lowest_prices_item_data)

            lowest_prices.append(componentsschemas_lowest_prices_item)

        buy_box_prices = []
        _buy_box_prices = d.pop("BuyBoxPrices", UNSET)
        for componentsschemas_buy_box_prices_item_data in _buy_box_prices or []:
            componentsschemas_buy_box_prices_item = BuyBoxPriceType.from_dict(
                componentsschemas_buy_box_prices_item_data
            )

            buy_box_prices.append(componentsschemas_buy_box_prices_item)

        _list_price = d.pop("ListPrice", UNSET)
        list_price: Union[Unset, MoneyType]
        if isinstance(_list_price, Unset):
            list_price = UNSET
        else:
            list_price = MoneyType.from_dict(_list_price)

        _competitive_price_threshold = d.pop("CompetitivePriceThreshold", UNSET)
        competitive_price_threshold: Union[Unset, MoneyType]
        if isinstance(_competitive_price_threshold, Unset):
            competitive_price_threshold = UNSET
        else:
            competitive_price_threshold = MoneyType.from_dict(_competitive_price_threshold)

        _suggested_lower_price_plus_shipping = d.pop("SuggestedLowerPricePlusShipping", UNSET)
        suggested_lower_price_plus_shipping: Union[Unset, MoneyType]
        if isinstance(_suggested_lower_price_plus_shipping, Unset):
            suggested_lower_price_plus_shipping = UNSET
        else:
            suggested_lower_price_plus_shipping = MoneyType.from_dict(_suggested_lower_price_plus_shipping)

        sales_rankings = []
        _sales_rankings = d.pop("SalesRankings", UNSET)
        for componentsschemas_sales_rank_list_item_data in _sales_rankings or []:
            componentsschemas_sales_rank_list_item = SalesRankType.from_dict(
                componentsschemas_sales_rank_list_item_data
            )

            sales_rankings.append(componentsschemas_sales_rank_list_item)

        buy_box_eligible_offers = []
        _buy_box_eligible_offers = d.pop("BuyBoxEligibleOffers", UNSET)
        for componentsschemas_buy_box_eligible_offers_item_data in _buy_box_eligible_offers or []:
            componentsschemas_buy_box_eligible_offers_item = OfferCountType.from_dict(
                componentsschemas_buy_box_eligible_offers_item_data
            )

            buy_box_eligible_offers.append(componentsschemas_buy_box_eligible_offers_item)

        _offers_available_time = d.pop("OffersAvailableTime", UNSET)
        offers_available_time: Union[Unset, datetime.datetime]
        if isinstance(_offers_available_time, Unset):
            offers_available_time = UNSET
        else:
            offers_available_time = isoparse(_offers_available_time)

        result = cls(
            total_offer_count=total_offer_count,
            number_of_offers=number_of_offers,
            lowest_prices=lowest_prices,
            buy_box_prices=buy_box_prices,
            list_price=list_price,
            competitive_price_threshold=competitive_price_threshold,
            suggested_lower_price_plus_shipping=suggested_lower_price_plus_shipping,
            sales_rankings=sales_rankings,
            buy_box_eligible_offers=buy_box_eligible_offers,
            offers_available_time=offers_available_time,
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
