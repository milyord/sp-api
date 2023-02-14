from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partnered_estimate import PartneredEstimate
    from ..models.partnered_small_parcel_package_output import PartneredSmallParcelPackageOutput


T = TypeVar("T", bound="PartneredSmallParcelDataOutput")


@attr.s(auto_attribs=True)
class PartneredSmallParcelDataOutput:
    r"""Information returned by Amazon about a Small Parcel shipment by an Amazon-partnered carrier.

    Attributes:
        package_list (List['PartneredSmallParcelPackageOutput']): A list of packages, including shipping information
            from the Amazon-partnered carrier.
        partnered_estimate (Union[Unset, PartneredEstimate]): The estimated shipping cost for a shipment using an
            Amazon-partnered carrier.
    """

    package_list: List["PartneredSmallParcelPackageOutput"]
    partnered_estimate: Union[Unset, "PartneredEstimate"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_list = []
        for componentsschemas_partnered_small_parcel_package_output_list_item_data in self.package_list:
            componentsschemas_partnered_small_parcel_package_output_list_item = (
                componentsschemas_partnered_small_parcel_package_output_list_item_data.to_dict()
            )

            package_list.append(componentsschemas_partnered_small_parcel_package_output_list_item)

        partnered_estimate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partnered_estimate, Unset):
            partnered_estimate = self.partnered_estimate.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PackageList": package_list,
            }
        )
        if partnered_estimate is not UNSET:
            field_dict["PartneredEstimate"] = partnered_estimate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.partnered_estimate import PartneredEstimate
        from ..models.partnered_small_parcel_package_output import PartneredSmallParcelPackageOutput

        d = src_dict.copy()
        package_list = []
        _package_list = d.pop("PackageList")
        for componentsschemas_partnered_small_parcel_package_output_list_item_data in _package_list:
            componentsschemas_partnered_small_parcel_package_output_list_item = (
                PartneredSmallParcelPackageOutput.from_dict(
                    componentsschemas_partnered_small_parcel_package_output_list_item_data
                )
            )

            package_list.append(componentsschemas_partnered_small_parcel_package_output_list_item)

        _partnered_estimate = d.pop("PartneredEstimate", UNSET)
        partnered_estimate: Union[Unset, PartneredEstimate]
        if isinstance(_partnered_estimate, Unset):
            partnered_estimate = UNSET
        else:
            partnered_estimate = PartneredEstimate.from_dict(_partnered_estimate)

        result = cls(
            package_list=package_list,
            partnered_estimate=partnered_estimate,
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
