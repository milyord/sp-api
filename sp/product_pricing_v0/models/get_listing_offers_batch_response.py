from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_offers_response import ListingOffersResponse


T = TypeVar("T", bound="GetListingOffersBatchResponse")


@attr.s(auto_attribs=True)
class GetListingOffersBatchResponse:
    r"""The response associated with the `getListingOffersBatch` API call.

    Attributes:
        responses (Union[Unset, List['ListingOffersResponse']]): A list of `getListingOffers` batched responses.
    """

    responses: Union[Unset, List["ListingOffersResponse"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        responses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for componentsschemas_listing_offers_response_list_item_data in self.responses:
                componentsschemas_listing_offers_response_list_item = (
                    componentsschemas_listing_offers_response_list_item_data.to_dict()
                )

                responses.append(componentsschemas_listing_offers_response_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_offers_response import ListingOffersResponse

        d = src_dict.copy()
        responses = []
        _responses = d.pop("responses", UNSET)
        for componentsschemas_listing_offers_response_list_item_data in _responses or []:
            componentsschemas_listing_offers_response_list_item = ListingOffersResponse.from_dict(
                componentsschemas_listing_offers_response_list_item_data
            )

            responses.append(componentsschemas_listing_offers_response_list_item)

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
