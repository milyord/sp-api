from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.container import Container


T = TypeVar("T", bound="CreateShipmentRequest")


@attr.s(auto_attribs=True)
class CreateShipmentRequest:
    r"""The request schema for the createShipment operation.

    Attributes:
        client_reference_id (str): Client reference id.
        ship_to (Address): The address.
        ship_from (Address): The address.
        containers (List['Container']): A list of container.
    """

    client_reference_id: str
    ship_to: "Address"
    ship_from: "Address"
    containers: List["Container"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_reference_id = self.client_reference_id
        ship_to = self.ship_to.to_dict()

        ship_from = self.ship_from.to_dict()

        containers = []
        for componentsschemas_container_list_item_data in self.containers:
            componentsschemas_container_list_item = componentsschemas_container_list_item_data.to_dict()

            containers.append(componentsschemas_container_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientReferenceId": client_reference_id,
                "shipTo": ship_to,
                "shipFrom": ship_from,
                "containers": containers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.container import Container

        d = src_dict.copy()
        client_reference_id = d.pop("clientReferenceId")

        ship_to = Address.from_dict(d.pop("shipTo"))

        ship_from = Address.from_dict(d.pop("shipFrom"))

        containers = []
        _containers = d.pop("containers")
        for componentsschemas_container_list_item_data in _containers:
            componentsschemas_container_list_item = Container.from_dict(componentsschemas_container_list_item_data)

            containers.append(componentsschemas_container_list_item)

        result = cls(
            client_reference_id=client_reference_id,
            ship_to=ship_to,
            ship_from=ship_from,
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
