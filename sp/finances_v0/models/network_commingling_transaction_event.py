import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="NetworkComminglingTransactionEvent")


@attr.s(auto_attribs=True)
class NetworkComminglingTransactionEvent:
    r"""A network commingling transaction event.

    Attributes:
        transaction_type (Union[Unset, str]): The type of network item swap.

            Possible values:

            * NetCo - A Fulfillment by Amazon inventory pooling transaction. Available only in the India marketplace.

            * ComminglingVAT - A commingling VAT transaction. Available only in the UK, Spain, France, Germany, and Italy
            marketplaces.
        posted_date (Union[Unset, datetime.datetime]):
        net_co_transaction_id (Union[Unset, str]): The identifier for the network item swap.
        swap_reason (Union[Unset, str]): The reason for the network item swap.
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the swapped item.
        marketplace_id (Union[Unset, str]): The marketplace in which the event took place.
        tax_exclusive_amount (Union[Unset, Currency]): A currency type and amount.
        tax_amount (Union[Unset, Currency]): A currency type and amount.
    """

    transaction_type: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    net_co_transaction_id: Union[Unset, str] = UNSET
    swap_reason: Union[Unset, str] = UNSET
    asin: Union[Unset, str] = UNSET
    marketplace_id: Union[Unset, str] = UNSET
    tax_exclusive_amount: Union[Unset, "Currency"] = UNSET
    tax_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_type = self.transaction_type
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        net_co_transaction_id = self.net_co_transaction_id
        swap_reason = self.swap_reason
        asin = self.asin
        marketplace_id = self.marketplace_id
        tax_exclusive_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_exclusive_amount, Unset):
            tax_exclusive_amount = self.tax_exclusive_amount.to_dict()

        tax_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_amount, Unset):
            tax_amount = self.tax_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_type is not UNSET:
            field_dict["TransactionType"] = transaction_type
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if net_co_transaction_id is not UNSET:
            field_dict["NetCoTransactionID"] = net_co_transaction_id
        if swap_reason is not UNSET:
            field_dict["SwapReason"] = swap_reason
        if asin is not UNSET:
            field_dict["ASIN"] = asin
        if marketplace_id is not UNSET:
            field_dict["MarketplaceId"] = marketplace_id
        if tax_exclusive_amount is not UNSET:
            field_dict["TaxExclusiveAmount"] = tax_exclusive_amount
        if tax_amount is not UNSET:
            field_dict["TaxAmount"] = tax_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        transaction_type = d.pop("TransactionType", UNSET)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        net_co_transaction_id = d.pop("NetCoTransactionID", UNSET)

        swap_reason = d.pop("SwapReason", UNSET)

        asin = d.pop("ASIN", UNSET)

        marketplace_id = d.pop("MarketplaceId", UNSET)

        _tax_exclusive_amount = d.pop("TaxExclusiveAmount", UNSET)
        tax_exclusive_amount: Union[Unset, Currency]
        if isinstance(_tax_exclusive_amount, Unset):
            tax_exclusive_amount = UNSET
        else:
            tax_exclusive_amount = Currency.from_dict(_tax_exclusive_amount)

        _tax_amount = d.pop("TaxAmount", UNSET)
        tax_amount: Union[Unset, Currency]
        if isinstance(_tax_amount, Unset):
            tax_amount = UNSET
        else:
            tax_amount = Currency.from_dict(_tax_amount)

        result = cls(
            transaction_type=transaction_type,
            posted_date=posted_date,
            net_co_transaction_id=net_co_transaction_id,
            swap_reason=swap_reason,
            asin=asin,
            marketplace_id=marketplace_id,
            tax_exclusive_amount=tax_exclusive_amount,
            tax_amount=tax_amount,
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
