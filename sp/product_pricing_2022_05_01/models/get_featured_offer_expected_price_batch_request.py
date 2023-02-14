from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.featured_offer_expected_price_request import FeaturedOfferExpectedPriceRequest


T = TypeVar("T", bound="GetFeaturedOfferExpectedPriceBatchRequest")


@attr.s(auto_attribs=True)
class GetFeaturedOfferExpectedPriceBatchRequest:
    r"""The request body for the getFeaturedOfferExpectedPriceBatch operation.

    Attributes:
        requests (Union[Unset, List['FeaturedOfferExpectedPriceRequest']]): A batched list of featured offer expected
            price requests.
    """

    requests: Union[Unset, List["FeaturedOfferExpectedPriceRequest"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requests: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.requests, Unset):
            requests = []
            for componentsschemas_featured_offer_expected_price_request_list_item_data in self.requests:
                componentsschemas_featured_offer_expected_price_request_list_item = (
                    componentsschemas_featured_offer_expected_price_request_list_item_data.to_dict()
                )

                requests.append(componentsschemas_featured_offer_expected_price_request_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requests is not UNSET:
            field_dict["requests"] = requests

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.featured_offer_expected_price_request import FeaturedOfferExpectedPriceRequest

        d = src_dict.copy()
        requests = []
        _requests = d.pop("requests", UNSET)
        for componentsschemas_featured_offer_expected_price_request_list_item_data in _requests or []:
            componentsschemas_featured_offer_expected_price_request_list_item = (
                FeaturedOfferExpectedPriceRequest.from_dict(
                    componentsschemas_featured_offer_expected_price_request_list_item_data
                )
            )

            requests.append(componentsschemas_featured_offer_expected_price_request_list_item)

        result = cls(
            requests=requests,
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
