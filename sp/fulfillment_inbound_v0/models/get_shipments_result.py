from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_shipment_info import InboundShipmentInfo


T = TypeVar("T", bound="GetShipmentsResult")


@attr.s(auto_attribs=True)
class GetShipmentsResult:
    r"""
    Attributes:
        shipment_data (Union[Unset, List['InboundShipmentInfo']]): A list of inbound shipment information.
        next_token (Union[Unset, str]): When present and not empty, pass this string token in the next request to return
            the next response page.
    """

    shipment_data: Union[Unset, List["InboundShipmentInfo"]] = UNSET
    next_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_data, Unset):
            shipment_data = []
            for componentsschemas_inbound_shipment_list_item_data in self.shipment_data:
                componentsschemas_inbound_shipment_list_item = (
                    componentsschemas_inbound_shipment_list_item_data.to_dict()
                )

                shipment_data.append(componentsschemas_inbound_shipment_list_item)

        next_token = self.next_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment_data is not UNSET:
            field_dict["ShipmentData"] = shipment_data
        if next_token is not UNSET:
            field_dict["NextToken"] = next_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inbound_shipment_info import InboundShipmentInfo

        d = src_dict.copy()
        shipment_data = []
        _shipment_data = d.pop("ShipmentData", UNSET)
        for componentsschemas_inbound_shipment_list_item_data in _shipment_data or []:
            componentsschemas_inbound_shipment_list_item = InboundShipmentInfo.from_dict(
                componentsschemas_inbound_shipment_list_item_data
            )

            shipment_data.append(componentsschemas_inbound_shipment_list_item)

        next_token = d.pop("NextToken", UNSET)

        result = cls(
            shipment_data=shipment_data,
            next_token=next_token,
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
