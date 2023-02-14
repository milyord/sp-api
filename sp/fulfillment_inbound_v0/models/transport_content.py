from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.transport_detail_output import TransportDetailOutput
    from ..models.transport_header import TransportHeader
    from ..models.transport_result import TransportResult


T = TypeVar("T", bound="TransportContent")


@attr.s(auto_attribs=True)
class TransportContent:
    r"""Inbound shipment information, including carrier details, shipment status, and the workflow status for a request for
    shipment with an Amazon-partnered carrier.

        Attributes:
            transport_header (TransportHeader): The shipping identifier, information about whether the shipment is by an
                Amazon-partnered carrier, and information about whether the shipment is Small Parcel or Less Than Truckload/Full
                Truckload (LTL/FTL).
            transport_details (TransportDetailOutput): Inbound shipment information, including carrier details and shipment
                status.
            transport_result (TransportResult): The workflow status for a shipment with an Amazon-partnered carrier.
    """

    transport_header: "TransportHeader"
    transport_details: "TransportDetailOutput"
    transport_result: "TransportResult"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transport_header = self.transport_header.to_dict()

        transport_details = self.transport_details.to_dict()

        transport_result = self.transport_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TransportHeader": transport_header,
                "TransportDetails": transport_details,
                "TransportResult": transport_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transport_detail_output import TransportDetailOutput
        from ..models.transport_header import TransportHeader
        from ..models.transport_result import TransportResult

        d = src_dict.copy()
        transport_header = TransportHeader.from_dict(d.pop("TransportHeader"))

        transport_details = TransportDetailOutput.from_dict(d.pop("TransportDetails"))

        transport_result = TransportResult.from_dict(d.pop("TransportResult"))

        result = cls(
            transport_header=transport_header,
            transport_details=transport_details,
            transport_result=transport_result,
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
