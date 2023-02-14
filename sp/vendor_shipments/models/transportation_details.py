from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.transportation_details_transportation_mode import TransportationDetailsTransportationMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransportationDetails")


@attr.s(auto_attribs=True)
class TransportationDetails:
    r"""
    Attributes:
        carrier_scac (Union[Unset, str]): Code that identifies the carrier for the shipment. The Standard Carrier Alpha
            Code (SCAC) is a unique two to four letter code used to identify a carrier. Carrier SCAC codes are assigned and
            maintained by the NMFTA (National Motor Freight Association). This field is mandatory for US, CA, MX shipment
            confirmations.
        carrier_shipment_reference_number (Union[Unset, str]): The field also known as PRO number is a unique number
            assigned by the carrier. It is used to identify and track the shipment that goes out for delivery. This field is
            mandatory for UA, CA, MX shipment confirmations.
        transportation_mode (Union[Unset, TransportationDetailsTransportationMode]): The mode of transportation for this
            shipment.
        bill_of_lading_number (Union[Unset, str]): Bill Of Lading (BOL) number is the unique number assigned by the
            vendor. The BOL present in the Shipment Confirmation message ideally matches the paper BOL provided with the
            shipment, but that is no must. Instead of BOL, an alternative reference number (like Delivery Note Number) for
            the shipment can also be sent in this field.
    """

    carrier_scac: Union[Unset, str] = UNSET
    carrier_shipment_reference_number: Union[Unset, str] = UNSET
    transportation_mode: Union[Unset, TransportationDetailsTransportationMode] = UNSET
    bill_of_lading_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carrier_scac = self.carrier_scac
        carrier_shipment_reference_number = self.carrier_shipment_reference_number
        transportation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.transportation_mode, Unset):
            transportation_mode = self.transportation_mode.value

        bill_of_lading_number = self.bill_of_lading_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier_scac is not UNSET:
            field_dict["carrierScac"] = carrier_scac
        if carrier_shipment_reference_number is not UNSET:
            field_dict["carrierShipmentReferenceNumber"] = carrier_shipment_reference_number
        if transportation_mode is not UNSET:
            field_dict["transportationMode"] = transportation_mode
        if bill_of_lading_number is not UNSET:
            field_dict["billOfLadingNumber"] = bill_of_lading_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        carrier_scac = d.pop("carrierScac", UNSET)

        carrier_shipment_reference_number = d.pop("carrierShipmentReferenceNumber", UNSET)

        _transportation_mode = d.pop("transportationMode", UNSET)
        transportation_mode: Union[Unset, TransportationDetailsTransportationMode]
        if isinstance(_transportation_mode, Unset):
            transportation_mode = UNSET
        else:
            transportation_mode = TransportationDetailsTransportationMode(_transportation_mode)

        bill_of_lading_number = d.pop("billOfLadingNumber", UNSET)

        result = cls(
            carrier_scac=carrier_scac,
            carrier_shipment_reference_number=carrier_shipment_reference_number,
            transportation_mode=transportation_mode,
            bill_of_lading_number=bill_of_lading_number,
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
