import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.service_type import ServiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.container import Container
    from ..models.label_specification import LabelSpecification


T = TypeVar("T", bound="PurchaseShipmentRequest")


@attr.s(auto_attribs=True)
class PurchaseShipmentRequest:
    r"""The payload schema for the purchaseShipment operation.

    Attributes:
        client_reference_id (str): Client reference id.
        ship_to (Address): The address.
        ship_from (Address): The address.
        service_type (ServiceType): The type of shipping service that will be used for the service offering.
        containers (List['Container']): A list of container.
        label_specification (LabelSpecification): The label specification info.
        ship_date (Union[Unset, datetime.datetime]): The start date and time. This defaults to the current date and
            time.
    """

    client_reference_id: str
    ship_to: "Address"
    ship_from: "Address"
    service_type: ServiceType
    containers: List["Container"]
    label_specification: "LabelSpecification"
    ship_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_reference_id = self.client_reference_id
        ship_to = self.ship_to.to_dict()

        ship_from = self.ship_from.to_dict()

        service_type = self.service_type.value

        containers = []
        for componentsschemas_container_list_item_data in self.containers:
            componentsschemas_container_list_item = componentsschemas_container_list_item_data.to_dict()

            containers.append(componentsschemas_container_list_item)

        label_specification = self.label_specification.to_dict()

        ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.ship_date, Unset):
            ship_date = self.ship_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientReferenceId": client_reference_id,
                "shipTo": ship_to,
                "shipFrom": ship_from,
                "serviceType": service_type,
                "containers": containers,
                "labelSpecification": label_specification,
            }
        )
        if ship_date is not UNSET:
            field_dict["shipDate"] = ship_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.container import Container
        from ..models.label_specification import LabelSpecification

        d = src_dict.copy()
        client_reference_id = d.pop("clientReferenceId")

        ship_to = Address.from_dict(d.pop("shipTo"))

        ship_from = Address.from_dict(d.pop("shipFrom"))

        service_type = ServiceType(d.pop("serviceType"))

        containers = []
        _containers = d.pop("containers")
        for componentsschemas_container_list_item_data in _containers:
            componentsschemas_container_list_item = Container.from_dict(componentsschemas_container_list_item_data)

            containers.append(componentsschemas_container_list_item)

        label_specification = LabelSpecification.from_dict(d.pop("labelSpecification"))

        _ship_date = d.pop("shipDate", UNSET)
        ship_date: Union[Unset, datetime.datetime]
        if isinstance(_ship_date, Unset):
            ship_date = UNSET
        else:
            ship_date = isoparse(_ship_date)

        result = cls(
            client_reference_id=client_reference_id,
            ship_to=ship_to,
            ship_from=ship_from,
            service_type=service_type,
            containers=containers,
            label_specification=label_specification,
            ship_date=ship_date,
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
