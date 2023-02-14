from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.container import Container
    from ..models.party_identification import PartyIdentification


T = TypeVar("T", bound="ShippingLabelRequest")


@attr.s(auto_attribs=True)
class ShippingLabelRequest:
    r"""
    Attributes:
        purchase_order_number (str): Purchase order number of the order for which to create a shipping label.
        selling_party (PartyIdentification):
        ship_from_party (PartyIdentification):
        containers (Union[Unset, List['Container']]): A list of the packages in this shipment.
    """

    purchase_order_number: str
    selling_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    containers: Union[Unset, List["Container"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        selling_party = self.selling_party.to_dict()

        ship_from_party = self.ship_from_party.to_dict()

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
                "sellingParty": selling_party,
                "shipFromParty": ship_from_party,
            }
        )
        if containers is not UNSET:
            field_dict["containers"] = containers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.container import Container
        from ..models.party_identification import PartyIdentification

        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        ship_from_party = PartyIdentification.from_dict(d.pop("shipFromParty"))

        containers = []
        _containers = d.pop("containers", UNSET)
        for containers_item_data in _containers or []:
            containers_item = Container.from_dict(containers_item_data)

            containers.append(containers_item)

        result = cls(
            purchase_order_number=purchase_order_number,
            selling_party=selling_party,
            ship_from_party=ship_from_party,
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
