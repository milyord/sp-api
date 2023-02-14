import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.safet_reimbursement_item import SAFETReimbursementItem


T = TypeVar("T", bound="SAFETReimbursementEvent")


@attr.s(auto_attribs=True)
class SAFETReimbursementEvent:
    r"""A SAFE-T claim reimbursement on the seller's account.

    Attributes:
        posted_date (Union[Unset, datetime.datetime]):
        safet_claim_id (Union[Unset, str]): A SAFE-T claim identifier.
        reimbursed_amount (Union[Unset, Currency]): A currency type and amount.
        reason_code (Union[Unset, str]): Indicates why the seller was reimbursed.
        safet_reimbursement_item_list (Union[Unset, List['SAFETReimbursementItem']]): A list of SAFETReimbursementItems.
    """

    posted_date: Union[Unset, datetime.datetime] = UNSET
    safet_claim_id: Union[Unset, str] = UNSET
    reimbursed_amount: Union[Unset, "Currency"] = UNSET
    reason_code: Union[Unset, str] = UNSET
    safet_reimbursement_item_list: Union[Unset, List["SAFETReimbursementItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        safet_claim_id = self.safet_claim_id
        reimbursed_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reimbursed_amount, Unset):
            reimbursed_amount = self.reimbursed_amount.to_dict()

        reason_code = self.reason_code
        safet_reimbursement_item_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.safet_reimbursement_item_list, Unset):
            safet_reimbursement_item_list = []
            for componentsschemas_safet_reimbursement_item_list_item_data in self.safet_reimbursement_item_list:
                componentsschemas_safet_reimbursement_item_list_item = (
                    componentsschemas_safet_reimbursement_item_list_item_data.to_dict()
                )

                safet_reimbursement_item_list.append(componentsschemas_safet_reimbursement_item_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if safet_claim_id is not UNSET:
            field_dict["SAFETClaimId"] = safet_claim_id
        if reimbursed_amount is not UNSET:
            field_dict["ReimbursedAmount"] = reimbursed_amount
        if reason_code is not UNSET:
            field_dict["ReasonCode"] = reason_code
        if safet_reimbursement_item_list is not UNSET:
            field_dict["SAFETReimbursementItemList"] = safet_reimbursement_item_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.safet_reimbursement_item import SAFETReimbursementItem

        d = src_dict.copy()
        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        safet_claim_id = d.pop("SAFETClaimId", UNSET)

        _reimbursed_amount = d.pop("ReimbursedAmount", UNSET)
        reimbursed_amount: Union[Unset, Currency]
        if isinstance(_reimbursed_amount, Unset):
            reimbursed_amount = UNSET
        else:
            reimbursed_amount = Currency.from_dict(_reimbursed_amount)

        reason_code = d.pop("ReasonCode", UNSET)

        safet_reimbursement_item_list = []
        _safet_reimbursement_item_list = d.pop("SAFETReimbursementItemList", UNSET)
        for componentsschemas_safet_reimbursement_item_list_item_data in _safet_reimbursement_item_list or []:
            componentsschemas_safet_reimbursement_item_list_item = SAFETReimbursementItem.from_dict(
                componentsschemas_safet_reimbursement_item_list_item_data
            )

            safet_reimbursement_item_list.append(componentsschemas_safet_reimbursement_item_list_item)

        result = cls(
            posted_date=posted_date,
            safet_claim_id=safet_claim_id,
            reimbursed_amount=reimbursed_amount,
            reason_code=reason_code,
            safet_reimbursement_item_list=safet_reimbursement_item_list,
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
