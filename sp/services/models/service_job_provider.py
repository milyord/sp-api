from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceJobProvider")


@attr.s(auto_attribs=True)
class ServiceJobProvider:
    r"""Information about the service job provider.

    Attributes:
        service_job_provider_id (Union[Unset, str]): The identifier of the service job provider.
    """

    service_job_provider_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_job_provider_id = self.service_job_provider_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_job_provider_id is not UNSET:
            field_dict["serviceJobProviderId"] = service_job_provider_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_job_provider_id = d.pop("serviceJobProviderId", UNSET)

        result = cls(
            service_job_provider_id=service_job_provider_id,
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
