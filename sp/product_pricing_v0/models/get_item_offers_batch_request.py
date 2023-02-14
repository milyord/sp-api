from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_offers_request import ItemOffersRequest


T = TypeVar("T", bound="GetItemOffersBatchRequest")


@attr.s(auto_attribs=True)
class GetItemOffersBatchRequest:
    r"""The request associated with the `getItemOffersBatch` API call.

    Attributes:
        requests (Union[Unset, List['ItemOffersRequest']]): A list of `getListingOffers` batched requests to run.
    """

    requests: Union[Unset, List["ItemOffersRequest"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requests: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.requests, Unset):
            requests = []
            for componentsschemas_item_offers_request_list_item_data in self.requests:
                componentsschemas_item_offers_request_list_item = (
                    componentsschemas_item_offers_request_list_item_data.to_dict()
                )

                requests.append(componentsschemas_item_offers_request_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requests is not UNSET:
            field_dict["requests"] = requests

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_offers_request import ItemOffersRequest

        d = src_dict.copy()
        requests = []
        _requests = d.pop("requests", UNSET)
        for componentsschemas_item_offers_request_list_item_data in _requests or []:
            componentsschemas_item_offers_request_list_item = ItemOffersRequest.from_dict(
                componentsschemas_item_offers_request_list_item_data
            )

            requests.append(componentsschemas_item_offers_request_list_item)

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
