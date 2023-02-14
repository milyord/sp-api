from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.featured_offer import FeaturedOffer
    from ..models.featured_offer_expected_price import FeaturedOfferExpectedPrice


T = TypeVar("T", bound="FeaturedOfferExpectedPriceResult")


@attr.s(auto_attribs=True)
class FeaturedOfferExpectedPriceResult:
    r"""The featured offer expected price result data for the requested offer.

    Attributes:
        result_status (str): The status of the featured offer expected price computation. Possible values include
            VALID_FOEP, NO_COMPETING_OFFER, OFFER_NOT_ELIGIBLE, OFFER_NOT_FOUND.
        featured_offer_expected_price (Union[Unset, FeaturedOfferExpectedPrice]): The item price at or below which the
            target offer may be featured.
        competing_featured_offer (Union[Unset, FeaturedOffer]):
        current_featured_offer (Union[Unset, FeaturedOffer]):
    """

    result_status: str
    featured_offer_expected_price: Union[Unset, "FeaturedOfferExpectedPrice"] = UNSET
    competing_featured_offer: Union[Unset, "FeaturedOffer"] = UNSET
    current_featured_offer: Union[Unset, "FeaturedOffer"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_status = self.result_status
        featured_offer_expected_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.featured_offer_expected_price, Unset):
            featured_offer_expected_price = self.featured_offer_expected_price.to_dict()

        competing_featured_offer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competing_featured_offer, Unset):
            competing_featured_offer = self.competing_featured_offer.to_dict()

        current_featured_offer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_featured_offer, Unset):
            current_featured_offer = self.current_featured_offer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resultStatus": result_status,
            }
        )
        if featured_offer_expected_price is not UNSET:
            field_dict["featuredOfferExpectedPrice"] = featured_offer_expected_price
        if competing_featured_offer is not UNSET:
            field_dict["competingFeaturedOffer"] = competing_featured_offer
        if current_featured_offer is not UNSET:
            field_dict["currentFeaturedOffer"] = current_featured_offer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.featured_offer import FeaturedOffer
        from ..models.featured_offer_expected_price import FeaturedOfferExpectedPrice

        d = src_dict.copy()
        result_status = d.pop("resultStatus")

        _featured_offer_expected_price = d.pop("featuredOfferExpectedPrice", UNSET)
        featured_offer_expected_price: Union[Unset, FeaturedOfferExpectedPrice]
        if isinstance(_featured_offer_expected_price, Unset):
            featured_offer_expected_price = UNSET
        else:
            featured_offer_expected_price = FeaturedOfferExpectedPrice.from_dict(_featured_offer_expected_price)

        _competing_featured_offer = d.pop("competingFeaturedOffer", UNSET)
        competing_featured_offer: Union[Unset, FeaturedOffer]
        if isinstance(_competing_featured_offer, Unset):
            competing_featured_offer = UNSET
        else:
            competing_featured_offer = FeaturedOffer.from_dict(_competing_featured_offer)

        _current_featured_offer = d.pop("currentFeaturedOffer", UNSET)
        current_featured_offer: Union[Unset, FeaturedOffer]
        if isinstance(_current_featured_offer, Unset):
            current_featured_offer = UNSET
        else:
            current_featured_offer = FeaturedOffer.from_dict(_current_featured_offer)

        result = cls(
            result_status=result_status,
            featured_offer_expected_price=featured_offer_expected_price,
            competing_featured_offer=competing_featured_offer,
            current_featured_offer=current_featured_offer,
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
