import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adjustment_item import AdjustmentItem
    from ..models.currency import Currency


T = TypeVar("T", bound="AdjustmentEvent")


@attr.s(auto_attribs=True)
class AdjustmentEvent:
    r"""An adjustment to the seller's account.

    Attributes:
        adjustment_type (Union[Unset, str]): The type of adjustment.

            Possible values:

            * FBAInventoryReimbursement - An FBA inventory reimbursement to a seller's account. This occurs if a seller's
            inventory is damaged.

            * ReserveEvent - A reserve event that is generated at the time of a settlement period closing. This occurs when
            some money from a seller's account is held back.

            * PostageBilling - The amount paid by a seller for shipping labels.

            * PostageRefund - The reimbursement of shipping labels purchased for orders that were canceled or refunded.

            * LostOrDamagedReimbursement - An Amazon Easy Ship reimbursement to a seller's account for a package that we
            lost or damaged.

            * CanceledButPickedUpReimbursement - An Amazon Easy Ship reimbursement to a seller's account. This occurs when a
            package is picked up and the order is subsequently canceled. This value is used only in the India marketplace.

            * ReimbursementClawback - An Amazon Easy Ship reimbursement clawback from a seller's account. This occurs when a
            prior reimbursement is reversed. This value is used only in the India marketplace.

            * SellerRewards - An award credited to a seller's account for their participation in an offer in the Seller
            Rewards program. Applies only to the India marketplace.
        posted_date (Union[Unset, datetime.datetime]):
        adjustment_amount (Union[Unset, Currency]): A currency type and amount.
        adjustment_item_list (Union[Unset, List['AdjustmentItem']]): A list of information about items in an adjustment
            to the seller's account.
    """

    adjustment_type: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    adjustment_amount: Union[Unset, "Currency"] = UNSET
    adjustment_item_list: Union[Unset, List["AdjustmentItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        adjustment_type = self.adjustment_type
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        adjustment_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.adjustment_amount, Unset):
            adjustment_amount = self.adjustment_amount.to_dict()

        adjustment_item_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.adjustment_item_list, Unset):
            adjustment_item_list = []
            for componentsschemas_adjustment_item_list_item_data in self.adjustment_item_list:
                componentsschemas_adjustment_item_list_item = componentsschemas_adjustment_item_list_item_data.to_dict()

                adjustment_item_list.append(componentsschemas_adjustment_item_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adjustment_type is not UNSET:
            field_dict["AdjustmentType"] = adjustment_type
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if adjustment_amount is not UNSET:
            field_dict["AdjustmentAmount"] = adjustment_amount
        if adjustment_item_list is not UNSET:
            field_dict["AdjustmentItemList"] = adjustment_item_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adjustment_item import AdjustmentItem
        from ..models.currency import Currency

        d = src_dict.copy()
        adjustment_type = d.pop("AdjustmentType", UNSET)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        _adjustment_amount = d.pop("AdjustmentAmount", UNSET)
        adjustment_amount: Union[Unset, Currency]
        if isinstance(_adjustment_amount, Unset):
            adjustment_amount = UNSET
        else:
            adjustment_amount = Currency.from_dict(_adjustment_amount)

        adjustment_item_list = []
        _adjustment_item_list = d.pop("AdjustmentItemList", UNSET)
        for componentsschemas_adjustment_item_list_item_data in _adjustment_item_list or []:
            componentsschemas_adjustment_item_list_item = AdjustmentItem.from_dict(
                componentsschemas_adjustment_item_list_item_data
            )

            adjustment_item_list.append(componentsschemas_adjustment_item_list_item)

        result = cls(
            adjustment_type=adjustment_type,
            posted_date=posted_date,
            adjustment_amount=adjustment_amount,
            adjustment_item_list=adjustment_item_list,
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
