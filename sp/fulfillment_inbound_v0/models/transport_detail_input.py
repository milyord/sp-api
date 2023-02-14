from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.non_partnered_ltl_data_input import NonPartneredLtlDataInput
    from ..models.non_partnered_small_parcel_data_input import NonPartneredSmallParcelDataInput
    from ..models.partnered_ltl_data_input import PartneredLtlDataInput
    from ..models.partnered_small_parcel_data_input import PartneredSmallParcelDataInput


T = TypeVar("T", bound="TransportDetailInput")


@attr.s(auto_attribs=True)
class TransportDetailInput:
    r"""Information required to create an Amazon-partnered carrier shipping estimate, or to alert the Amazon fulfillment
    center to the arrival of an inbound shipment by a non-Amazon-partnered carrier.

        Attributes:
            partnered_small_parcel_data (Union[Unset, PartneredSmallParcelDataInput]): Information that is required by an
                Amazon-partnered carrier to ship a Small Parcel inbound shipment.
            non_partnered_small_parcel_data (Union[Unset, NonPartneredSmallParcelDataInput]): Information that you provide
                to Amazon about a Small Parcel shipment shipped by a carrier that has not partnered with Amazon.
            partnered_ltl_data (Union[Unset, PartneredLtlDataInput]): Information that is required by an Amazon-partnered
                carrier to ship a Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.
            non_partnered_ltl_data (Union[Unset, NonPartneredLtlDataInput]): Information that you provide to Amazon about a
                Less Than Truckload/Full Truckload (LTL/FTL) shipment by a carrier that has not partnered with Amazon.
    """

    partnered_small_parcel_data: Union[Unset, "PartneredSmallParcelDataInput"] = UNSET
    non_partnered_small_parcel_data: Union[Unset, "NonPartneredSmallParcelDataInput"] = UNSET
    partnered_ltl_data: Union[Unset, "PartneredLtlDataInput"] = UNSET
    non_partnered_ltl_data: Union[Unset, "NonPartneredLtlDataInput"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        partnered_small_parcel_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partnered_small_parcel_data, Unset):
            partnered_small_parcel_data = self.partnered_small_parcel_data.to_dict()

        non_partnered_small_parcel_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.non_partnered_small_parcel_data, Unset):
            non_partnered_small_parcel_data = self.non_partnered_small_parcel_data.to_dict()

        partnered_ltl_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partnered_ltl_data, Unset):
            partnered_ltl_data = self.partnered_ltl_data.to_dict()

        non_partnered_ltl_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.non_partnered_ltl_data, Unset):
            non_partnered_ltl_data = self.non_partnered_ltl_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partnered_small_parcel_data is not UNSET:
            field_dict["PartneredSmallParcelData"] = partnered_small_parcel_data
        if non_partnered_small_parcel_data is not UNSET:
            field_dict["NonPartneredSmallParcelData"] = non_partnered_small_parcel_data
        if partnered_ltl_data is not UNSET:
            field_dict["PartneredLtlData"] = partnered_ltl_data
        if non_partnered_ltl_data is not UNSET:
            field_dict["NonPartneredLtlData"] = non_partnered_ltl_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.non_partnered_ltl_data_input import NonPartneredLtlDataInput
        from ..models.non_partnered_small_parcel_data_input import NonPartneredSmallParcelDataInput
        from ..models.partnered_ltl_data_input import PartneredLtlDataInput
        from ..models.partnered_small_parcel_data_input import PartneredSmallParcelDataInput

        d = src_dict.copy()
        _partnered_small_parcel_data = d.pop("PartneredSmallParcelData", UNSET)
        partnered_small_parcel_data: Union[Unset, PartneredSmallParcelDataInput]
        if isinstance(_partnered_small_parcel_data, Unset):
            partnered_small_parcel_data = UNSET
        else:
            partnered_small_parcel_data = PartneredSmallParcelDataInput.from_dict(_partnered_small_parcel_data)

        _non_partnered_small_parcel_data = d.pop("NonPartneredSmallParcelData", UNSET)
        non_partnered_small_parcel_data: Union[Unset, NonPartneredSmallParcelDataInput]
        if isinstance(_non_partnered_small_parcel_data, Unset):
            non_partnered_small_parcel_data = UNSET
        else:
            non_partnered_small_parcel_data = NonPartneredSmallParcelDataInput.from_dict(
                _non_partnered_small_parcel_data
            )

        _partnered_ltl_data = d.pop("PartneredLtlData", UNSET)
        partnered_ltl_data: Union[Unset, PartneredLtlDataInput]
        if isinstance(_partnered_ltl_data, Unset):
            partnered_ltl_data = UNSET
        else:
            partnered_ltl_data = PartneredLtlDataInput.from_dict(_partnered_ltl_data)

        _non_partnered_ltl_data = d.pop("NonPartneredLtlData", UNSET)
        non_partnered_ltl_data: Union[Unset, NonPartneredLtlDataInput]
        if isinstance(_non_partnered_ltl_data, Unset):
            non_partnered_ltl_data = UNSET
        else:
            non_partnered_ltl_data = NonPartneredLtlDataInput.from_dict(_non_partnered_ltl_data)

        result = cls(
            partnered_small_parcel_data=partnered_small_parcel_data,
            non_partnered_small_parcel_data=non_partnered_small_parcel_data,
            partnered_ltl_data=partnered_ltl_data,
            non_partnered_ltl_data=non_partnered_ltl_data,
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
