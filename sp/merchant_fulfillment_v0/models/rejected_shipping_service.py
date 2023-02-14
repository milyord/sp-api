from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RejectedShippingService")


@attr.s(auto_attribs=True)
class RejectedShippingService:
    r"""Information about a rejected shipping service

    Attributes:
        carrier_name (str): The rejected shipping carrier name. e.g. USPS
        shipping_service_name (str): The rejected shipping service localized name. e.g. FedEx Standard Overnight
        shipping_service_id (str): An Amazon-defined shipping service identifier.
        rejection_reason_code (str): A reason code meant to be consumed programatically. e.g.
            CARRIER_CANNOT_SHIP_TO_POBOX
        rejection_reason_message (Union[Unset, str]): A localized human readable description of the rejected reason.
    """

    carrier_name: str
    shipping_service_name: str
    shipping_service_id: str
    rejection_reason_code: str
    rejection_reason_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carrier_name = self.carrier_name
        shipping_service_name = self.shipping_service_name
        shipping_service_id = self.shipping_service_id
        rejection_reason_code = self.rejection_reason_code
        rejection_reason_message = self.rejection_reason_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CarrierName": carrier_name,
                "ShippingServiceName": shipping_service_name,
                "ShippingServiceId": shipping_service_id,
                "RejectionReasonCode": rejection_reason_code,
            }
        )
        if rejection_reason_message is not UNSET:
            field_dict["RejectionReasonMessage"] = rejection_reason_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        carrier_name = d.pop("CarrierName")

        shipping_service_name = d.pop("ShippingServiceName")

        shipping_service_id = d.pop("ShippingServiceId")

        rejection_reason_code = d.pop("RejectionReasonCode")

        rejection_reason_message = d.pop("RejectionReasonMessage", UNSET)

        result = cls(
            carrier_name=carrier_name,
            shipping_service_name=shipping_service_name,
            shipping_service_id=shipping_service_id,
            rejection_reason_code=rejection_reason_code,
            rejection_reason_message=rejection_reason_message,
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
