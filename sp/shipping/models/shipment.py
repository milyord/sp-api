from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accepted_rate import AcceptedRate
    from ..models.address import Address
    from ..models.container import Container
    from ..models.party import Party


T = TypeVar("T", bound="Shipment")


@attr.s(auto_attribs=True)
class Shipment:
    r"""The shipment related data.

    Attributes:
        shipment_id (str): The unique shipment identifier.
        client_reference_id (str): Client reference id.
        ship_from (Address): The address.
        ship_to (Address): The address.
        containers (List['Container']): A list of container.
        accepted_rate (Union[Unset, AcceptedRate]): The specific rate purchased for the shipment, or null if
            unpurchased.
        shipper (Union[Unset, Party]): The account related with the shipment.
    """

    shipment_id: str
    client_reference_id: str
    ship_from: "Address"
    ship_to: "Address"
    containers: List["Container"]
    accepted_rate: Union[Unset, "AcceptedRate"] = UNSET
    shipper: Union[Unset, "Party"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_id = self.shipment_id
        client_reference_id = self.client_reference_id
        ship_from = self.ship_from.to_dict()

        ship_to = self.ship_to.to_dict()

        containers = []
        for componentsschemas_container_list_item_data in self.containers:
            componentsschemas_container_list_item = componentsschemas_container_list_item_data.to_dict()

            containers.append(componentsschemas_container_list_item)

        accepted_rate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accepted_rate, Unset):
            accepted_rate = self.accepted_rate.to_dict()

        shipper: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipper, Unset):
            shipper = self.shipper.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipmentId": shipment_id,
                "clientReferenceId": client_reference_id,
                "shipFrom": ship_from,
                "shipTo": ship_to,
                "containers": containers,
            }
        )
        if accepted_rate is not UNSET:
            field_dict["acceptedRate"] = accepted_rate
        if shipper is not UNSET:
            field_dict["shipper"] = shipper

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.accepted_rate import AcceptedRate
        from ..models.address import Address
        from ..models.container import Container
        from ..models.party import Party

        d = src_dict.copy()
        shipment_id = d.pop("shipmentId")

        client_reference_id = d.pop("clientReferenceId")

        ship_from = Address.from_dict(d.pop("shipFrom"))

        ship_to = Address.from_dict(d.pop("shipTo"))

        containers = []
        _containers = d.pop("containers")
        for componentsschemas_container_list_item_data in _containers:
            componentsschemas_container_list_item = Container.from_dict(componentsschemas_container_list_item_data)

            containers.append(componentsschemas_container_list_item)

        _accepted_rate = d.pop("acceptedRate", UNSET)
        accepted_rate: Union[Unset, AcceptedRate]
        if isinstance(_accepted_rate, Unset):
            accepted_rate = UNSET
        else:
            accepted_rate = AcceptedRate.from_dict(_accepted_rate)

        _shipper = d.pop("shipper", UNSET)
        shipper: Union[Unset, Party]
        if isinstance(_shipper, Unset):
            shipper = UNSET
        else:
            shipper = Party.from_dict(_shipper)

        result = cls(
            shipment_id=shipment_id,
            client_reference_id=client_reference_id,
            ship_from=ship_from,
            ship_to=ship_to,
            containers=containers,
            accepted_rate=accepted_rate,
            shipper=shipper,
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
