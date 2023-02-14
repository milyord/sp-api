from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.service_location_service_location_type import ServiceLocationServiceLocationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="ServiceLocation")


@attr.s(auto_attribs=True)
class ServiceLocation:
    r"""Information about the location of the service job.

    Attributes:
        service_location_type (Union[Unset, ServiceLocationServiceLocationType]): The location of the service job.
        address (Union[Unset, Address]): The shipping address for the service job.
    """

    service_location_type: Union[Unset, ServiceLocationServiceLocationType] = UNSET
    address: Union[Unset, "Address"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_location_type: Union[Unset, str] = UNSET
        if not isinstance(self.service_location_type, Unset):
            service_location_type = self.service_location_type.value

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_location_type is not UNSET:
            field_dict["serviceLocationType"] = service_location_type
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        _service_location_type = d.pop("serviceLocationType", UNSET)
        service_location_type: Union[Unset, ServiceLocationServiceLocationType]
        if isinstance(_service_location_type, Unset):
            service_location_type = UNSET
        else:
            service_location_type = ServiceLocationServiceLocationType(_service_location_type)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        result = cls(
            service_location_type=service_location_type,
            address=address,
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
