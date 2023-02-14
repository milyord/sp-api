from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.container import Container
    from ..models.item import Item
    from ..models.party_identification import PartyIdentification
    from ..models.shipment_details import ShipmentDetails


T = TypeVar("T", bound="ShipmentConfirmation")


@attr.s(auto_attribs=True)
class ShipmentConfirmation:
    r"""
    Attributes:
        purchase_order_number (str): Purchase order number corresponding to the shipment.
        shipment_details (ShipmentDetails): Details about a shipment.
        selling_party (PartyIdentification):
        ship_from_party (PartyIdentification):
        items (List['Item']): Provide the details of the items in this shipment. If any of the item details field is
            common at a package or a pallet level, then provide them at the corresponding package.
        containers (Union[Unset, List['Container']]): Provide the details of the items in this shipment. If any of the
            item details field is common at a package or a pallet level, then provide them at the corresponding package.
    """

    purchase_order_number: str
    shipment_details: "ShipmentDetails"
    selling_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    items: List["Item"]
    containers: Union[Unset, List["Container"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        shipment_details = self.shipment_details.to_dict()

        selling_party = self.selling_party.to_dict()

        ship_from_party = self.ship_from_party.to_dict()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        containers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.containers, Unset):
            containers = []
            for containers_item_data in self.containers:
                containers_item = containers_item_data.to_dict()

                containers.append(containers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderNumber": purchase_order_number,
                "shipmentDetails": shipment_details,
                "sellingParty": selling_party,
                "shipFromParty": ship_from_party,
                "items": items,
            }
        )
        if containers is not UNSET:
            field_dict["containers"] = containers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.container import Container
        from ..models.item import Item
        from ..models.party_identification import PartyIdentification
        from ..models.shipment_details import ShipmentDetails

        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        shipment_details = ShipmentDetails.from_dict(d.pop("shipmentDetails"))

        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        ship_from_party = PartyIdentification.from_dict(d.pop("shipFromParty"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Item.from_dict(items_item_data)

            items.append(items_item)

        containers = []
        _containers = d.pop("containers", UNSET)
        for containers_item_data in _containers or []:
            containers_item = Container.from_dict(containers_item_data)

            containers.append(containers_item)

        result = cls(
            purchase_order_number=purchase_order_number,
            shipment_details=shipment_details,
            selling_party=selling_party,
            ship_from_party=ship_from_party,
            items=items,
            containers=containers,
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
