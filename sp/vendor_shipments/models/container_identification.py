from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.container_identification_container_identification_type import (
    ContainerIdentificationContainerIdentificationType,
)

T = TypeVar("T", bound="ContainerIdentification")


@attr.s(auto_attribs=True)
class ContainerIdentification:
    r"""
    Attributes:
        container_identification_type (ContainerIdentificationContainerIdentificationType): The container identification
            type.
        container_identification_number (str): Container identification number that adheres to the definition of the
            container identification type.
    """

    container_identification_type: ContainerIdentificationContainerIdentificationType
    container_identification_number: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container_identification_type = self.container_identification_type.value

        container_identification_number = self.container_identification_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerIdentificationType": container_identification_type,
                "containerIdentificationNumber": container_identification_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        container_identification_type = ContainerIdentificationContainerIdentificationType(
            d.pop("containerIdentificationType")
        )

        container_identification_number = d.pop("containerIdentificationNumber")

        result = cls(
            container_identification_type=container_identification_type,
            container_identification_number=container_identification_number,
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
