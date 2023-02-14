from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.predefined_package_dimensions import PredefinedPackageDimensions
from ..models.unit_of_length import UnitOfLength
from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageDimensions")


@attr.s(auto_attribs=True)
class PackageDimensions:
    r"""The dimensions of a package contained in a shipment.

    Attributes:
        length (Union[Unset, float]):
        width (Union[Unset, float]):
        height (Union[Unset, float]):
        unit (Union[Unset, UnitOfLength]): The unit of length.
        predefined_package_dimensions (Union[Unset, PredefinedPackageDimensions]): An enumeration of predefined parcel
            tokens. If you specify a PredefinedPackageDimensions token, you are not obligated to use a branded package from
            a carrier. For example, if you specify the FedEx_Box_10kg token, you do not have to use that particular package
            from FedEx. You are only obligated to use a box that matches the dimensions specified by the token.

            Note: Please note that carriers can have restrictions on the type of package allowed for certain ship methods.
            Check the carrier website for all details. Example: Flat rate pricing is available when materials are sent by
            USPS in a USPS-produced Flat Rate Envelope or Box.
    """

    length: Union[Unset, float] = UNSET
    width: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    unit: Union[Unset, UnitOfLength] = UNSET
    predefined_package_dimensions: Union[Unset, PredefinedPackageDimensions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        length = self.length
        width = self.width
        height = self.height
        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        predefined_package_dimensions: Union[Unset, str] = UNSET
        if not isinstance(self.predefined_package_dimensions, Unset):
            predefined_package_dimensions = self.predefined_package_dimensions.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if length is not UNSET:
            field_dict["Length"] = length
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if unit is not UNSET:
            field_dict["Unit"] = unit
        if predefined_package_dimensions is not UNSET:
            field_dict["PredefinedPackageDimensions"] = predefined_package_dimensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        length = d.pop("Length", UNSET)

        width = d.pop("Width", UNSET)

        height = d.pop("Height", UNSET)

        _unit = d.pop("Unit", UNSET)
        unit: Union[Unset, UnitOfLength]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = UnitOfLength(_unit)

        _predefined_package_dimensions = d.pop("PredefinedPackageDimensions", UNSET)
        predefined_package_dimensions: Union[Unset, PredefinedPackageDimensions]
        if isinstance(_predefined_package_dimensions, Unset):
            predefined_package_dimensions = UNSET
        else:
            predefined_package_dimensions = PredefinedPackageDimensions(_predefined_package_dimensions)

        result = cls(
            length=length,
            width=width,
            height=height,
            unit=unit,
            predefined_package_dimensions=predefined_package_dimensions,
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
