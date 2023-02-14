import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="TDSReimbursementEvent")


@attr.s(auto_attribs=True)
class TDSReimbursementEvent:
    r"""An event related to a Tax-Deducted-at-Source (TDS) reimbursement.

    Attributes:
        posted_date (Union[Unset, datetime.datetime]):
        tds_order_id (Union[Unset, str]): The Tax-Deducted-at-Source (TDS) identifier.
        reimbursed_amount (Union[Unset, Currency]): A currency type and amount.
    """

    posted_date: Union[Unset, datetime.datetime] = UNSET
    tds_order_id: Union[Unset, str] = UNSET
    reimbursed_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        tds_order_id = self.tds_order_id
        reimbursed_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reimbursed_amount, Unset):
            reimbursed_amount = self.reimbursed_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if tds_order_id is not UNSET:
            field_dict["TDSOrderId"] = tds_order_id
        if reimbursed_amount is not UNSET:
            field_dict["ReimbursedAmount"] = reimbursed_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        tds_order_id = d.pop("TDSOrderId", UNSET)

        _reimbursed_amount = d.pop("ReimbursedAmount", UNSET)
        reimbursed_amount: Union[Unset, Currency]
        if isinstance(_reimbursed_amount, Unset):
            reimbursed_amount = UNSET
        else:
            reimbursed_amount = Currency.from_dict(_reimbursed_amount)

        result = cls(
            posted_date=posted_date,
            tds_order_id=tds_order_id,
            reimbursed_amount=reimbursed_amount,
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
