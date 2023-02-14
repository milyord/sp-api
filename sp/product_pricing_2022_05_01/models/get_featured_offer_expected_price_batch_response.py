from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.featured_offer_expected_price_response import FeaturedOfferExpectedPriceResponse


T = TypeVar("T", bound="GetFeaturedOfferExpectedPriceBatchResponse")


@attr.s(auto_attribs=True)
class GetFeaturedOfferExpectedPriceBatchResponse:
    r"""The response schema for the getFeaturedOfferExpectedPriceBatch operation.

    Attributes:
        responses (Union[Unset, List['FeaturedOfferExpectedPriceResponse']]): A batched list of featured offer expected
            price responses.
    """

    responses: Union[Unset, List["FeaturedOfferExpectedPriceResponse"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        responses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for componentsschemas_featured_offer_expected_price_response_list_item_data in self.responses:
                componentsschemas_featured_offer_expected_price_response_list_item = (
                    componentsschemas_featured_offer_expected_price_response_list_item_data.to_dict()
                )

                responses.append(componentsschemas_featured_offer_expected_price_response_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.featured_offer_expected_price_response import FeaturedOfferExpectedPriceResponse

        d = src_dict.copy()
        responses = []
        _responses = d.pop("responses", UNSET)
        for componentsschemas_featured_offer_expected_price_response_list_item_data in _responses or []:
            componentsschemas_featured_offer_expected_price_response_list_item = (
                FeaturedOfferExpectedPriceResponse.from_dict(
                    componentsschemas_featured_offer_expected_price_response_list_item_data
                )
            )

            responses.append(componentsschemas_featured_offer_expected_price_response_list_item)

        result = cls(
            responses=responses,
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
