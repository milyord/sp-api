from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.inbound_shipment_header import InboundShipmentHeader
    from ..models.inbound_shipment_item import InboundShipmentItem


T = TypeVar("T", bound="InboundShipmentRequest")


@attr.s(auto_attribs=True)
class InboundShipmentRequest:
    r"""The request schema for an inbound shipment.

    Attributes:
        inbound_shipment_header (InboundShipmentHeader): Inbound shipment information used to create and update inbound
            shipments.
        inbound_shipment_items (List['InboundShipmentItem']): A list of inbound shipment item information.
        marketplace_id (str): A marketplace identifier. Specifies the marketplace where the product would be stored.
    """

    inbound_shipment_header: "InboundShipmentHeader"
    inbound_shipment_items: List["InboundShipmentItem"]
    marketplace_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inbound_shipment_header = self.inbound_shipment_header.to_dict()

        inbound_shipment_items = []
        for componentsschemas_inbound_shipment_item_list_item_data in self.inbound_shipment_items:
            componentsschemas_inbound_shipment_item_list_item = (
                componentsschemas_inbound_shipment_item_list_item_data.to_dict()
            )

            inbound_shipment_items.append(componentsschemas_inbound_shipment_item_list_item)

        marketplace_id = self.marketplace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "InboundShipmentHeader": inbound_shipment_header,
                "InboundShipmentItems": inbound_shipment_items,
                "MarketplaceId": marketplace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inbound_shipment_header import InboundShipmentHeader
        from ..models.inbound_shipment_item import InboundShipmentItem

        d = src_dict.copy()
        inbound_shipment_header = InboundShipmentHeader.from_dict(d.pop("InboundShipmentHeader"))

        inbound_shipment_items = []
        _inbound_shipment_items = d.pop("InboundShipmentItems")
        for componentsschemas_inbound_shipment_item_list_item_data in _inbound_shipment_items:
            componentsschemas_inbound_shipment_item_list_item = InboundShipmentItem.from_dict(
                componentsschemas_inbound_shipment_item_list_item_data
            )

            inbound_shipment_items.append(componentsschemas_inbound_shipment_item_list_item)

        marketplace_id = d.pop("MarketplaceId")

        result = cls(
            inbound_shipment_header=inbound_shipment_header,
            inbound_shipment_items=inbound_shipment_items,
            marketplace_id=marketplace_id,
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
