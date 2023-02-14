from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipping_label_request import ShippingLabelRequest


T = TypeVar("T", bound="SubmitShippingLabelsRequest")


@attr.s(auto_attribs=True)
class SubmitShippingLabelsRequest:
    r"""
    Attributes:
        shipping_label_requests (Union[Unset, List['ShippingLabelRequest']]):
    """

    shipping_label_requests: Union[Unset, List["ShippingLabelRequest"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_label_requests: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_label_requests, Unset):
            shipping_label_requests = []
            for shipping_label_requests_item_data in self.shipping_label_requests:
                shipping_label_requests_item = shipping_label_requests_item_data.to_dict()

                shipping_label_requests.append(shipping_label_requests_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipping_label_requests is not UNSET:
            field_dict["shippingLabelRequests"] = shipping_label_requests

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipping_label_request import ShippingLabelRequest

        d = src_dict.copy()
        shipping_label_requests = []
        _shipping_label_requests = d.pop("shippingLabelRequests", UNSET)
        for shipping_label_requests_item_data in _shipping_label_requests or []:
            shipping_label_requests_item = ShippingLabelRequest.from_dict(shipping_label_requests_item_data)

            shipping_label_requests.append(shipping_label_requests_item)

        result = cls(
            shipping_label_requests=shipping_label_requests,
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
