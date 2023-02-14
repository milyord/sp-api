from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.non_partnered_small_parcel_package_input import NonPartneredSmallParcelPackageInput


T = TypeVar("T", bound="NonPartneredSmallParcelDataInput")


@attr.s(auto_attribs=True)
class NonPartneredSmallParcelDataInput:
    r"""Information that you provide to Amazon about a Small Parcel shipment shipped by a carrier that has not partnered
    with Amazon.

        Attributes:
            carrier_name (str): The carrier that you are using for the inbound shipment.
            package_list (List['NonPartneredSmallParcelPackageInput']): A list of package tracking information.
    """

    carrier_name: str
    package_list: List["NonPartneredSmallParcelPackageInput"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carrier_name = self.carrier_name
        package_list = []
        for componentsschemas_non_partnered_small_parcel_package_input_list_item_data in self.package_list:
            componentsschemas_non_partnered_small_parcel_package_input_list_item = (
                componentsschemas_non_partnered_small_parcel_package_input_list_item_data.to_dict()
            )

            package_list.append(componentsschemas_non_partnered_small_parcel_package_input_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CarrierName": carrier_name,
                "PackageList": package_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.non_partnered_small_parcel_package_input import NonPartneredSmallParcelPackageInput

        d = src_dict.copy()
        carrier_name = d.pop("CarrierName")

        package_list = []
        _package_list = d.pop("PackageList")
        for componentsschemas_non_partnered_small_parcel_package_input_list_item_data in _package_list:
            componentsschemas_non_partnered_small_parcel_package_input_list_item = (
                NonPartneredSmallParcelPackageInput.from_dict(
                    componentsschemas_non_partnered_small_parcel_package_input_list_item_data
                )
            )

            package_list.append(componentsschemas_non_partnered_small_parcel_package_input_list_item)

        result = cls(
            carrier_name=carrier_name,
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
