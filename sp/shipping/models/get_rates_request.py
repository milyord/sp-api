import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.service_type import ServiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.container_specification import ContainerSpecification


T = TypeVar("T", bound="GetRatesRequest")


@attr.s(auto_attribs=True)
class GetRatesRequest:
    r"""The payload schema for the getRates operation.

    Attributes:
        ship_to (Address): The address.
        ship_from (Address): The address.
        service_types (List[ServiceType]): A list of service types that can be used to send the shipment.
        container_specifications (List['ContainerSpecification']): A list of container specifications.
        ship_date (Union[Unset, datetime.datetime]): The start date and time. This defaults to the current date and
            time.
    """

    ship_to: "Address"
    ship_from: "Address"
    service_types: List[ServiceType]
    container_specifications: List["ContainerSpecification"]
    ship_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ship_to = self.ship_to.to_dict()

        ship_from = self.ship_from.to_dict()

        service_types = []
        for componentsschemas_service_type_list_item_data in self.service_types:
            componentsschemas_service_type_list_item = componentsschemas_service_type_list_item_data.value

            service_types.append(componentsschemas_service_type_list_item)

        container_specifications = []
        for componentsschemas_container_specification_list_item_data in self.container_specifications:
            componentsschemas_container_specification_list_item = (
                componentsschemas_container_specification_list_item_data.to_dict()
            )

            container_specifications.append(componentsschemas_container_specification_list_item)

        ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.ship_date, Unset):
            ship_date = self.ship_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipTo": ship_to,
                "shipFrom": ship_from,
                "serviceTypes": service_types,
                "containerSpecifications": container_specifications,
            }
        )
        if ship_date is not UNSET:
            field_dict["shipDate"] = ship_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.container_specification import ContainerSpecification

        d = src_dict.copy()
        ship_to = Address.from_dict(d.pop("shipTo"))

        ship_from = Address.from_dict(d.pop("shipFrom"))

        service_types = []
        _service_types = d.pop("serviceTypes")
        for componentsschemas_service_type_list_item_data in _service_types:
            componentsschemas_service_type_list_item = ServiceType(componentsschemas_service_type_list_item_data)

            service_types.append(componentsschemas_service_type_list_item)

        container_specifications = []
        _container_specifications = d.pop("containerSpecifications")
        for componentsschemas_container_specification_list_item_data in _container_specifications:
            componentsschemas_container_specification_list_item = ContainerSpecification.from_dict(
                componentsschemas_container_specification_list_item_data
            )

            container_specifications.append(componentsschemas_container_specification_list_item)

        _ship_date = d.pop("shipDate", UNSET)
        ship_date: Union[Unset, datetime.datetime]
        if isinstance(_ship_date, Unset):
            ship_date = UNSET
        else:
            ship_date = isoparse(_ship_date)

        result = cls(
            ship_to=ship_to,
            ship_from=ship_from,
            service_types=service_types,
            container_specifications=container_specifications,
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
