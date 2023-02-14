from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.non_partnered_ltl_data_output import NonPartneredLtlDataOutput
    from ..models.non_partnered_small_parcel_data_output import NonPartneredSmallParcelDataOutput
    from ..models.partnered_ltl_data_output import PartneredLtlDataOutput
    from ..models.partnered_small_parcel_data_output import PartneredSmallParcelDataOutput


T = TypeVar("T", bound="TransportDetailOutput")


@attr.s(auto_attribs=True)
class TransportDetailOutput:
    r"""Inbound shipment information, including carrier details and shipment status.

    Attributes:
        partnered_small_parcel_data (Union[Unset, PartneredSmallParcelDataOutput]): Information returned by Amazon about
            a Small Parcel shipment by an Amazon-partnered carrier.
        non_partnered_small_parcel_data (Union[Unset, NonPartneredSmallParcelDataOutput]): Information returned by
            Amazon about a Small Parcel shipment by a carrier that has not partnered with Amazon.
        partnered_ltl_data (Union[Unset, PartneredLtlDataOutput]): Information returned by Amazon about a Less Than
            Truckload/Full Truckload (LTL/FTL) shipment by an Amazon-partnered carrier.
        non_partnered_ltl_data (Union[Unset, NonPartneredLtlDataOutput]): Information returned by Amazon about a Less
            Than Truckload/Full Truckload (LTL/FTL) shipment shipped by a carrier that has not partnered with Amazon.
    """

    partnered_small_parcel_data: Union[Unset, "PartneredSmallParcelDataOutput"] = UNSET
    non_partnered_small_parcel_data: Union[Unset, "NonPartneredSmallParcelDataOutput"] = UNSET
    partnered_ltl_data: Union[Unset, "PartneredLtlDataOutput"] = UNSET
    non_partnered_ltl_data: Union[Unset, "NonPartneredLtlDataOutput"] = UNSET
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
        from ..models.non_partnered_ltl_data_output import NonPartneredLtlDataOutput
        from ..models.non_partnered_small_parcel_data_output import NonPartneredSmallParcelDataOutput
        from ..models.partnered_ltl_data_output import PartneredLtlDataOutput
        from ..models.partnered_small_parcel_data_output import PartneredSmallParcelDataOutput

        d = src_dict.copy()
        _partnered_small_parcel_data = d.pop("PartneredSmallParcelData", UNSET)
        partnered_small_parcel_data: Union[Unset, PartneredSmallParcelDataOutput]
        if isinstance(_partnered_small_parcel_data, Unset):
            partnered_small_parcel_data = UNSET
        else:
            partnered_small_parcel_data = PartneredSmallParcelDataOutput.from_dict(_partnered_small_parcel_data)

        _non_partnered_small_parcel_data = d.pop("NonPartneredSmallParcelData", UNSET)
        non_partnered_small_parcel_data: Union[Unset, NonPartneredSmallParcelDataOutput]
        if isinstance(_non_partnered_small_parcel_data, Unset):
            non_partnered_small_parcel_data = UNSET
        else:
            non_partnered_small_parcel_data = NonPartneredSmallParcelDataOutput.from_dict(
                _non_partnered_small_parcel_data
            )

        _partnered_ltl_data = d.pop("PartneredLtlData", UNSET)
        partnered_ltl_data: Union[Unset, PartneredLtlDataOutput]
        if isinstance(_partnered_ltl_data, Unset):
            partnered_ltl_data = UNSET
        else:
            partnered_ltl_data = PartneredLtlDataOutput.from_dict(_partnered_ltl_data)

        _non_partnered_ltl_data = d.pop("NonPartneredLtlData", UNSET)
        non_partnered_ltl_data: Union[Unset, NonPartneredLtlDataOutput]
        if isinstance(_non_partnered_ltl_data, Unset):
            non_partnered_ltl_data = UNSET
        else:
            non_partnered_ltl_data = NonPartneredLtlDataOutput.from_dict(_non_partnered_ltl_data)

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
