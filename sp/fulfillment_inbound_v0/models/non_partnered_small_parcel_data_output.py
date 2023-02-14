from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.non_partnered_small_parcel_package_output import NonPartneredSmallParcelPackageOutput


T = TypeVar("T", bound="NonPartneredSmallParcelDataOutput")


@attr.s(auto_attribs=True)
class NonPartneredSmallParcelDataOutput:
    r"""Information returned by Amazon about a Small Parcel shipment by a carrier that has not partnered with Amazon.

    Attributes:
        package_list (List['NonPartneredSmallParcelPackageOutput']): A list of packages, including carrier, tracking
            number, and status information for each package.
    """

    package_list: List["NonPartneredSmallParcelPackageOutput"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_list = []
        for componentsschemas_non_partnered_small_parcel_package_output_list_item_data in self.package_list:
            componentsschemas_non_partnered_small_parcel_package_output_list_item = (
                componentsschemas_non_partnered_small_parcel_package_output_list_item_data.to_dict()
            )

            package_list.append(componentsschemas_non_partnered_small_parcel_package_output_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PackageList": package_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.non_partnered_small_parcel_package_output import NonPartneredSmallParcelPackageOutput

        d = src_dict.copy()
        package_list = []
        _package_list = d.pop("PackageList")
        for componentsschemas_non_partnered_small_parcel_package_output_list_item_data in _package_list:
            componentsschemas_non_partnered_small_parcel_package_output_list_item = (
                NonPartneredSmallParcelPackageOutput.from_dict(
                    componentsschemas_non_partnered_small_parcel_package_output_list_item_data
                )
            )

            package_list.append(componentsschemas_non_partnered_small_parcel_package_output_list_item)

        result = cls(
            package_list=package_list,
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
