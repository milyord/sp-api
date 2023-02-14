from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partnered_small_parcel_package_input import PartneredSmallParcelPackageInput


T = TypeVar("T", bound="PartneredSmallParcelDataInput")


@attr.s(auto_attribs=True)
class PartneredSmallParcelDataInput:
    r"""Information that is required by an Amazon-partnered carrier to ship a Small Parcel inbound shipment.

    Attributes:
        package_list (Union[Unset, List['PartneredSmallParcelPackageInput']]): A list of dimensions and weight
            information for packages.
        carrier_name (Union[Unset, str]): The Amazon-partnered carrier to use for the inbound shipment.
            **`CarrierName`** values in France (FR), Italy (IT), Spain (ES), the United Kingdom (UK), and the United States
            (US): `UNITED_PARCEL_SERVICE_INC`. <br> **`CarrierName`** values in Germany (DE):
            `DHL_STANDARD`,`UNITED_PARCEL_SERVICE_INC`. <br>Default: `UNITED_PARCEL_SERVICE_INC`.
    """

    package_list: Union[Unset, List["PartneredSmallParcelPackageInput"]] = UNSET
    carrier_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.package_list, Unset):
            package_list = []
            for componentsschemas_partnered_small_parcel_package_input_list_item_data in self.package_list:
                componentsschemas_partnered_small_parcel_package_input_list_item = (
                    componentsschemas_partnered_small_parcel_package_input_list_item_data.to_dict()
                )

                package_list.append(componentsschemas_partnered_small_parcel_package_input_list_item)

        carrier_name = self.carrier_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_list is not UNSET:
            field_dict["PackageList"] = package_list
        if carrier_name is not UNSET:
            field_dict["CarrierName"] = carrier_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.partnered_small_parcel_package_input import PartneredSmallParcelPackageInput

        d = src_dict.copy()
        package_list = []
        _package_list = d.pop("PackageList", UNSET)
        for componentsschemas_partnered_small_parcel_package_input_list_item_data in _package_list or []:
            componentsschemas_partnered_small_parcel_package_input_list_item = (
                PartneredSmallParcelPackageInput.from_dict(
                    componentsschemas_partnered_small_parcel_package_input_list_item_data
                )
            )

            package_list.append(componentsschemas_partnered_small_parcel_package_input_list_item)

        carrier_name = d.pop("CarrierName", UNSET)

        result = cls(
            package_list=package_list,
            carrier_name=carrier_name,
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
