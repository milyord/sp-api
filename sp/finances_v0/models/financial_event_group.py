import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="FinancialEventGroup")


@attr.s(auto_attribs=True)
class FinancialEventGroup:
    r"""Information related to a financial event group.

    Attributes:
        financial_event_group_id (Union[Unset, str]): A unique identifier for the financial event group.
        processing_status (Union[Unset, str]): The processing status of the financial event group indicates whether the
            balance of the financial event group is settled.

            Possible values:

            * Open

            * Closed
        fund_transfer_status (Union[Unset, str]): The status of the fund transfer.
        original_total (Union[Unset, Currency]): A currency type and amount.
        converted_total (Union[Unset, Currency]): A currency type and amount.
        fund_transfer_date (Union[Unset, datetime.datetime]):
        trace_id (Union[Unset, str]): The trace identifier used by sellers to look up transactions externally.
        account_tail (Union[Unset, str]): The account tail of the payment instrument.
        beginning_balance (Union[Unset, Currency]): A currency type and amount.
        financial_event_group_start (Union[Unset, datetime.datetime]):
        financial_event_group_end (Union[Unset, datetime.datetime]):
    """

    financial_event_group_id: Union[Unset, str] = UNSET
    processing_status: Union[Unset, str] = UNSET
    fund_transfer_status: Union[Unset, str] = UNSET
    original_total: Union[Unset, "Currency"] = UNSET
    converted_total: Union[Unset, "Currency"] = UNSET
    fund_transfer_date: Union[Unset, datetime.datetime] = UNSET
    trace_id: Union[Unset, str] = UNSET
    account_tail: Union[Unset, str] = UNSET
    beginning_balance: Union[Unset, "Currency"] = UNSET
    financial_event_group_start: Union[Unset, datetime.datetime] = UNSET
    financial_event_group_end: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        financial_event_group_id = self.financial_event_group_id
        processing_status = self.processing_status
        fund_transfer_status = self.fund_transfer_status
        original_total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.original_total, Unset):
            original_total = self.original_total.to_dict()

        converted_total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.converted_total, Unset):
            converted_total = self.converted_total.to_dict()

        fund_transfer_date: Union[Unset, str] = UNSET
        if not isinstance(self.fund_transfer_date, Unset):
            fund_transfer_date = self.fund_transfer_date.isoformat()

        trace_id = self.trace_id
        account_tail = self.account_tail
        beginning_balance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.beginning_balance, Unset):
            beginning_balance = self.beginning_balance.to_dict()

        financial_event_group_start: Union[Unset, str] = UNSET
        if not isinstance(self.financial_event_group_start, Unset):
            financial_event_group_start = self.financial_event_group_start.isoformat()

        financial_event_group_end: Union[Unset, str] = UNSET
        if not isinstance(self.financial_event_group_end, Unset):
            financial_event_group_end = self.financial_event_group_end.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if financial_event_group_id is not UNSET:
            field_dict["FinancialEventGroupId"] = financial_event_group_id
        if processing_status is not UNSET:
            field_dict["ProcessingStatus"] = processing_status
        if fund_transfer_status is not UNSET:
            field_dict["FundTransferStatus"] = fund_transfer_status
        if original_total is not UNSET:
            field_dict["OriginalTotal"] = original_total
        if converted_total is not UNSET:
            field_dict["ConvertedTotal"] = converted_total
        if fund_transfer_date is not UNSET:
            field_dict["FundTransferDate"] = fund_transfer_date
        if trace_id is not UNSET:
            field_dict["TraceId"] = trace_id
        if account_tail is not UNSET:
            field_dict["AccountTail"] = account_tail
        if beginning_balance is not UNSET:
            field_dict["BeginningBalance"] = beginning_balance
        if financial_event_group_start is not UNSET:
            field_dict["FinancialEventGroupStart"] = financial_event_group_start
        if financial_event_group_end is not UNSET:
            field_dict["FinancialEventGroupEnd"] = financial_event_group_end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        financial_event_group_id = d.pop("FinancialEventGroupId", UNSET)

        processing_status = d.pop("ProcessingStatus", UNSET)

        fund_transfer_status = d.pop("FundTransferStatus", UNSET)

        _original_total = d.pop("OriginalTotal", UNSET)
        original_total: Union[Unset, Currency]
        if isinstance(_original_total, Unset):
            original_total = UNSET
        else:
            original_total = Currency.from_dict(_original_total)

        _converted_total = d.pop("ConvertedTotal", UNSET)
        converted_total: Union[Unset, Currency]
        if isinstance(_converted_total, Unset):
            converted_total = UNSET
        else:
            converted_total = Currency.from_dict(_converted_total)

        _fund_transfer_date = d.pop("FundTransferDate", UNSET)
        fund_transfer_date: Union[Unset, datetime.datetime]
        if isinstance(_fund_transfer_date, Unset):
            fund_transfer_date = UNSET
        else:
            fund_transfer_date = isoparse(_fund_transfer_date)

        trace_id = d.pop("TraceId", UNSET)

        account_tail = d.pop("AccountTail", UNSET)

        _beginning_balance = d.pop("BeginningBalance", UNSET)
        beginning_balance: Union[Unset, Currency]
        if isinstance(_beginning_balance, Unset):
            beginning_balance = UNSET
        else:
            beginning_balance = Currency.from_dict(_beginning_balance)

        _financial_event_group_start = d.pop("FinancialEventGroupStart", UNSET)
        financial_event_group_start: Union[Unset, datetime.datetime]
        if isinstance(_financial_event_group_start, Unset):
            financial_event_group_start = UNSET
        else:
            financial_event_group_start = isoparse(_financial_event_group_start)

        _financial_event_group_end = d.pop("FinancialEventGroupEnd", UNSET)
        financial_event_group_end: Union[Unset, datetime.datetime]
        if isinstance(_financial_event_group_end, Unset):
            financial_event_group_end = UNSET
        else:
            financial_event_group_end = isoparse(_financial_event_group_end)

        result = cls(
            financial_event_group_id=financial_event_group_id,
            processing_status=processing_status,
            fund_transfer_status=fund_transfer_status,
            original_total=original_total,
            converted_total=converted_total,
            fund_transfer_date=fund_transfer_date,
            trace_id=trace_id,
            account_tail=account_tail,
            beginning_balance=beginning_balance,
            financial_event_group_start=financial_event_group_start,
            financial_event_group_end=financial_event_group_end,
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
