from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="ChargeRefundTransaction")


@attr.s(auto_attribs=True)
class ChargeRefundTransaction:
    r"""The charge refund transaction.

    Attributes:
        charge_amount (Union[Unset, Currency]): A currency type and amount.
        charge_type (Union[Unset, str]): The type of charge.
    """

    charge_amount: Union[Unset, "Currency"] = UNSET
    charge_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charge_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.charge_amount, Unset):
            charge_amount = self.charge_amount.to_dict()

        charge_type = self.charge_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_amount is not UNSET:
            field_dict["ChargeAmount"] = charge_amount
        if charge_type is not UNSET:
            field_dict["ChargeType"] = charge_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        _charge_amount = d.pop("ChargeAmount", UNSET)
        charge_amount: Union[Unset, Currency]
        if isinstance(_charge_amount, Unset):
            charge_amount = UNSET
        else:
            charge_amount = Currency.from_dict(_charge_amount)

        charge_type = d.pop("ChargeType", UNSET)

        result = cls(
            charge_amount=charge_amount,
            charge_type=charge_type,
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
