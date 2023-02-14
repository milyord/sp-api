import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="DebtRecoveryItem")


@attr.s(auto_attribs=True)
class DebtRecoveryItem:
    r"""An item of a debt payment or debt adjustment.

    Attributes:
        recovery_amount (Union[Unset, Currency]): A currency type and amount.
        original_amount (Union[Unset, Currency]): A currency type and amount.
        group_begin_date (Union[Unset, datetime.datetime]):
        group_end_date (Union[Unset, datetime.datetime]):
    """

    recovery_amount: Union[Unset, "Currency"] = UNSET
    original_amount: Union[Unset, "Currency"] = UNSET
    group_begin_date: Union[Unset, datetime.datetime] = UNSET
    group_end_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        recovery_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recovery_amount, Unset):
            recovery_amount = self.recovery_amount.to_dict()

        original_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.original_amount, Unset):
            original_amount = self.original_amount.to_dict()

        group_begin_date: Union[Unset, str] = UNSET
        if not isinstance(self.group_begin_date, Unset):
            group_begin_date = self.group_begin_date.isoformat()

        group_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.group_end_date, Unset):
            group_end_date = self.group_end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recovery_amount is not UNSET:
            field_dict["RecoveryAmount"] = recovery_amount
        if original_amount is not UNSET:
            field_dict["OriginalAmount"] = original_amount
        if group_begin_date is not UNSET:
            field_dict["GroupBeginDate"] = group_begin_date
        if group_end_date is not UNSET:
            field_dict["GroupEndDate"] = group_end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        _recovery_amount = d.pop("RecoveryAmount", UNSET)
        recovery_amount: Union[Unset, Currency]
        if isinstance(_recovery_amount, Unset):
            recovery_amount = UNSET
        else:
            recovery_amount = Currency.from_dict(_recovery_amount)

        _original_amount = d.pop("OriginalAmount", UNSET)
        original_amount: Union[Unset, Currency]
        if isinstance(_original_amount, Unset):
            original_amount = UNSET
        else:
            original_amount = Currency.from_dict(_original_amount)

        _group_begin_date = d.pop("GroupBeginDate", UNSET)
        group_begin_date: Union[Unset, datetime.datetime]
        if isinstance(_group_begin_date, Unset):
            group_begin_date = UNSET
        else:
            group_begin_date = isoparse(_group_begin_date)

        _group_end_date = d.pop("GroupEndDate", UNSET)
        group_end_date: Union[Unset, datetime.datetime]
        if isinstance(_group_end_date, Unset):
            group_end_date = UNSET
        else:
            group_end_date = isoparse(_group_end_date)

        result = cls(
            recovery_amount=recovery_amount,
            original_amount=original_amount,
            group_begin_date=group_begin_date,
            group_end_date=group_end_date,
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
