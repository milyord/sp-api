from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.update_package_details import UpdatePackageDetails


T = TypeVar("T", bound="UpdateScheduledPackagesRequest")


@attr.s(auto_attribs=True)
class UpdateScheduledPackagesRequest:
    r"""The request schema for the `updateScheduledPackages` operation.

    Attributes:
        marketplace_id (str): A string of up to 255 characters.
        update_package_details_list (List['UpdatePackageDetails']): A list of package update details.
    """

    marketplace_id: str
    update_package_details_list: List["UpdatePackageDetails"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        update_package_details_list = []
        for componentsschemas_update_package_details_list_item_data in self.update_package_details_list:
            componentsschemas_update_package_details_list_item = (
                componentsschemas_update_package_details_list_item_data.to_dict()
            )

            update_package_details_list.append(componentsschemas_update_package_details_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "updatePackageDetailsList": update_package_details_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_package_details import UpdatePackageDetails

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        update_package_details_list = []
        _update_package_details_list = d.pop("updatePackageDetailsList")
        for componentsschemas_update_package_details_list_item_data in _update_package_details_list:
            componentsschemas_update_package_details_list_item = UpdatePackageDetails.from_dict(
                componentsschemas_update_package_details_list_item_data
            )

            update_package_details_list.append(componentsschemas_update_package_details_list_item)

        result = cls(
            marketplace_id=marketplace_id,
            update_package_details_list=update_package_details_list,
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
