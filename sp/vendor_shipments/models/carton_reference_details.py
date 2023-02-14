from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CartonReferenceDetails")


@attr.s(auto_attribs=True)
class CartonReferenceDetails:
    r"""
    Attributes:
        carton_reference_numbers (List[str]): Array of reference numbers for the carton that are part of this
            pallet/shipment. Please provide the cartonSequenceNumber from the 'cartons' segment to refer to that carton's
            details here.
        carton_count (Union[Unset, int]): Pallet level carton count is mandatory for single item pallet and optional for
            mixed item pallet.
    """

    carton_reference_numbers: List[str]
    carton_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carton_reference_numbers = self.carton_reference_numbers

        carton_count = self.carton_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cartonReferenceNumbers": carton_reference_numbers,
            }
        )
        if carton_count is not UNSET:
            field_dict["cartonCount"] = carton_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        carton_reference_numbers = cast(List[str], d.pop("cartonReferenceNumbers"))

        carton_count = d.pop("cartonCount", UNSET)

        result = cls(
            carton_reference_numbers=carton_reference_numbers,
            carton_count=carton_count,
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
