from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.featured_offer_expected_price_result import FeaturedOfferExpectedPriceResult
    from ..models.offer_identifier import OfferIdentifier


T = TypeVar("T", bound="FeaturedOfferExpectedPriceResponseBody")


@attr.s(auto_attribs=True)
class FeaturedOfferExpectedPriceResponseBody:
    r"""The featured offer expected price response data for a requested SKU.

    Attributes:
        offer_identifier (OfferIdentifier): Identifies an offer from a particular seller on an ASIN.
        featured_offer_expected_price_results (Union[Unset, List['FeaturedOfferExpectedPriceResult']]): A list of
            featured offer expected price results for the requested offer.
        errors (Union[Unset, List['Error']]): A list of error responses returned when a request is unsuccessful.
    """

    offer_identifier: "OfferIdentifier"
    featured_offer_expected_price_results: Union[Unset, List["FeaturedOfferExpectedPriceResult"]] = UNSET
    errors: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offer_identifier = self.offer_identifier.to_dict()

        featured_offer_expected_price_results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.featured_offer_expected_price_results, Unset):
            featured_offer_expected_price_results = []
            for (
                componentsschemas_featured_offer_expected_price_result_list_item_data
            ) in self.featured_offer_expected_price_results:
                componentsschemas_featured_offer_expected_price_result_list_item = (
                    componentsschemas_featured_offer_expected_price_result_list_item_data.to_dict()
                )

                featured_offer_expected_price_results.append(
                    componentsschemas_featured_offer_expected_price_result_list_item
                )

        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemas_error_list_item_data in self.errors:
                componentsschemas_error_list_item = componentsschemas_error_list_item_data.to_dict()

                errors.append(componentsschemas_error_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offerIdentifier": offer_identifier,
            }
        )
        if featured_offer_expected_price_results is not UNSET:
            field_dict["featuredOfferExpectedPriceResults"] = featured_offer_expected_price_results
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.featured_offer_expected_price_result import FeaturedOfferExpectedPriceResult
        from ..models.offer_identifier import OfferIdentifier

        d = src_dict.copy()
        offer_identifier = OfferIdentifier.from_dict(d.pop("offerIdentifier"))

        featured_offer_expected_price_results = []
        _featured_offer_expected_price_results = d.pop("featuredOfferExpectedPriceResults", UNSET)
        for componentsschemas_featured_offer_expected_price_result_list_item_data in (
            _featured_offer_expected_price_results or []
        ):
            componentsschemas_featured_offer_expected_price_result_list_item = (
                FeaturedOfferExpectedPriceResult.from_dict(
                    componentsschemas_featured_offer_expected_price_result_list_item_data
                )
            )

            featured_offer_expected_price_results.append(
                componentsschemas_featured_offer_expected_price_result_list_item
            )

        errors = []
        _errors = d.pop("errors", UNSET)
        for componentsschemas_error_list_item_data in _errors or []:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            errors.append(componentsschemas_error_list_item)

        result = cls(
            offer_identifier=offer_identifier,
            featured_offer_expected_price_results=featured_offer_expected_price_results,
            errors=errors,
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
