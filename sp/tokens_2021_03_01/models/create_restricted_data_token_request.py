from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.restricted_resource import RestrictedResource


T = TypeVar("T", bound="CreateRestrictedDataTokenRequest")


@attr.s(auto_attribs=True)
class CreateRestrictedDataTokenRequest:
    r"""The request schema for the createRestrictedDataToken operation.

    Attributes:
        restricted_resources (List['RestrictedResource']): A list of restricted resources.
            Maximum: 50
        target_application (Union[Unset, str]): The application ID for the target application to which access is being
            delegated.
    """

    restricted_resources: List["RestrictedResource"]
    target_application: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        restricted_resources = []
        for restricted_resources_item_data in self.restricted_resources:
            restricted_resources_item = restricted_resources_item_data.to_dict()

            restricted_resources.append(restricted_resources_item)

        target_application = self.target_application

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restrictedResources": restricted_resources,
            }
        )
        if target_application is not UNSET:
            field_dict["targetApplication"] = target_application

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.restricted_resource import RestrictedResource

        d = src_dict.copy()
        restricted_resources = []
        _restricted_resources = d.pop("restrictedResources")
        for restricted_resources_item_data in _restricted_resources:
            restricted_resources_item = RestrictedResource.from_dict(restricted_resources_item_data)

            restricted_resources.append(restricted_resources_item)

        target_application = d.pop("targetApplication", UNSET)

        result = cls(
            restricted_resources=restricted_resources,
            target_application=target_application,
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
