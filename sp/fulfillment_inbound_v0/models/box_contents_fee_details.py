from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount import Amount


T = TypeVar("T", bound="BoxContentsFeeDetails")


@attr.s(auto_attribs=True)
class BoxContentsFeeDetails:
    r"""The manual processing fee per unit and total fee for a shipment.

    Attributes:
        total_units (Union[Unset, int]): The item quantity.
        fee_per_unit (Union[Unset, Amount]): The monetary value.
        total_fee (Union[Unset, Amount]): The monetary value.
    """

    total_units: Union[Unset, int] = UNSET
    fee_per_unit: Union[Unset, "Amount"] = UNSET
    total_fee: Union[Unset, "Amount"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_units = self.total_units
        fee_per_unit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fee_per_unit, Unset):
            fee_per_unit = self.fee_per_unit.to_dict()

        total_fee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_fee, Unset):
            total_fee = self.total_fee.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_units is not UNSET:
            field_dict["TotalUnits"] = total_units
        if fee_per_unit is not UNSET:
            field_dict["FeePerUnit"] = fee_per_unit
        if total_fee is not UNSET:
            field_dict["TotalFee"] = total_fee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amount import Amount

        d = src_dict.copy()
        total_units = d.pop("TotalUnits", UNSET)

        _fee_per_unit = d.pop("FeePerUnit", UNSET)
        fee_per_unit: Union[Unset, Amount]
        if isinstance(_fee_per_unit, Unset):
            fee_per_unit = UNSET
        else:
            fee_per_unit = Amount.from_dict(_fee_per_unit)

        _total_fee = d.pop("TotalFee", UNSET)
        total_fee: Union[Unset, Amount]
        if isinstance(_total_fee, Unset):
            total_fee = UNSET
        else:
            total_fee = Amount.from_dict(_total_fee)

        result = cls(
            total_units=total_units,
            fee_per_unit=fee_per_unit,
            total_fee=total_fee,
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
