from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_request_details import ShipmentRequestDetails
    from ..models.shipping_offering_filter import ShippingOfferingFilter


T = TypeVar("T", bound="GetEligibleShipmentServicesRequest")


@attr.s(auto_attribs=True)
class GetEligibleShipmentServicesRequest:
    r"""Request schema.

    Attributes:
        shipment_request_details (ShipmentRequestDetails): Shipment information required for requesting shipping service
            offers or for creating a shipment.
        shipping_offering_filter (Union[Unset, ShippingOfferingFilter]): Filter for use when requesting eligible
            shipping services.
    """

    shipment_request_details: "ShipmentRequestDetails"
    shipping_offering_filter: Union[Unset, "ShippingOfferingFilter"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_request_details = self.shipment_request_details.to_dict()

        shipping_offering_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_offering_filter, Unset):
            shipping_offering_filter = self.shipping_offering_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShipmentRequestDetails": shipment_request_details,
            }
        )
        if shipping_offering_filter is not UNSET:
            field_dict["ShippingOfferingFilter"] = shipping_offering_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipment_request_details import ShipmentRequestDetails
        from ..models.shipping_offering_filter import ShippingOfferingFilter

        d = src_dict.copy()
        shipment_request_details = ShipmentRequestDetails.from_dict(d.pop("ShipmentRequestDetails"))

        _shipping_offering_filter = d.pop("ShippingOfferingFilter", UNSET)
        shipping_offering_filter: Union[Unset, ShippingOfferingFilter]
        if isinstance(_shipping_offering_filter, Unset):
            shipping_offering_filter = UNSET
        else:
            shipping_offering_filter = ShippingOfferingFilter.from_dict(_shipping_offering_filter)

        result = cls(
            shipment_request_details=shipment_request_details,
            shipping_offering_filter=shipping_offering_filter,
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
