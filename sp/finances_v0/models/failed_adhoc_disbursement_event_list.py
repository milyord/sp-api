import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="FailedAdhocDisbursementEventList")


@attr.s(auto_attribs=True)
class FailedAdhocDisbursementEventList:
    r"""Failed ad hoc disbursement event list.

    Attributes:
        funds_transfers_type (Union[Unset, str]): The type of fund transfer.

            Example "Refund"
        transfer_id (Union[Unset, str]): The transfer identifier.
        disbursement_id (Union[Unset, str]): The disbursement identifier.
        payment_disbursement_type (Union[Unset, str]): The type of payment for disbursement.

            Example `CREDIT_CARD`
        status (Union[Unset, str]): The status of the failed `AdhocDisbursement`.

            Example `HARD_DECLINED`
        transfer_amount (Union[Unset, Currency]): A currency type and amount.
        posted_date (Union[Unset, datetime.datetime]):
    """

    funds_transfers_type: Union[Unset, str] = UNSET
    transfer_id: Union[Unset, str] = UNSET
    disbursement_id: Union[Unset, str] = UNSET
    payment_disbursement_type: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    transfer_amount: Union[Unset, "Currency"] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        funds_transfers_type = self.funds_transfers_type
        transfer_id = self.transfer_id
        disbursement_id = self.disbursement_id
        payment_disbursement_type = self.payment_disbursement_type
        status = self.status
        transfer_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transfer_amount, Unset):
            transfer_amount = self.transfer_amount.to_dict()

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if funds_transfers_type is not UNSET:
            field_dict["FundsTransfersType"] = funds_transfers_type
        if transfer_id is not UNSET:
            field_dict["TransferId"] = transfer_id
        if disbursement_id is not UNSET:
            field_dict["DisbursementId"] = disbursement_id
        if payment_disbursement_type is not UNSET:
            field_dict["PaymentDisbursementType"] = payment_disbursement_type
        if status is not UNSET:
            field_dict["Status"] = status
        if transfer_amount is not UNSET:
            field_dict["TransferAmount"] = transfer_amount
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        funds_transfers_type = d.pop("FundsTransfersType", UNSET)

        transfer_id = d.pop("TransferId", UNSET)

        disbursement_id = d.pop("DisbursementId", UNSET)

        payment_disbursement_type = d.pop("PaymentDisbursementType", UNSET)

        status = d.pop("Status", UNSET)

        _transfer_amount = d.pop("TransferAmount", UNSET)
        transfer_amount: Union[Unset, Currency]
        if isinstance(_transfer_amount, Unset):
            transfer_amount = UNSET
        else:
            transfer_amount = Currency.from_dict(_transfer_amount)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        result = cls(
            funds_transfers_type=funds_transfers_type,
            transfer_id=transfer_id,
            disbursement_id=disbursement_id,
            payment_disbursement_type=payment_disbursement_type,
            status=status,
            transfer_amount=transfer_amount,
            posted_date=posted_date,
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
