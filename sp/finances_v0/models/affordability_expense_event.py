import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="AffordabilityExpenseEvent")


@attr.s(auto_attribs=True)
class AffordabilityExpenseEvent:
    r"""An expense related to an affordability promotion.

    Attributes:
        tax_type_cgst (Currency): A currency type and amount.
        tax_type_sgst (Currency): A currency type and amount.
        tax_type_igst (Currency): A currency type and amount.
        amazon_order_id (Union[Unset, str]): An Amazon-defined identifier for an order.
        posted_date (Union[Unset, datetime.datetime]):
        marketplace_id (Union[Unset, str]): An encrypted, Amazon-defined marketplace identifier.
        transaction_type (Union[Unset, str]): Indicates the type of transaction.

            Possible values:

            * Charge - For an affordability promotion expense.

            * Refund - For an affordability promotion expense reversal.
        base_expense (Union[Unset, Currency]): A currency type and amount.
        total_expense (Union[Unset, Currency]): A currency type and amount.
    """

    tax_type_cgst: "Currency"
    tax_type_sgst: "Currency"
    tax_type_igst: "Currency"
    amazon_order_id: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    marketplace_id: Union[Unset, str] = UNSET
    transaction_type: Union[Unset, str] = UNSET
    base_expense: Union[Unset, "Currency"] = UNSET
    total_expense: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_type_cgst = self.tax_type_cgst.to_dict()

        tax_type_sgst = self.tax_type_sgst.to_dict()

        tax_type_igst = self.tax_type_igst.to_dict()

        amazon_order_id = self.amazon_order_id
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        marketplace_id = self.marketplace_id
        transaction_type = self.transaction_type
        base_expense: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base_expense, Unset):
            base_expense = self.base_expense.to_dict()

        total_expense: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_expense, Unset):
            total_expense = self.total_expense.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TaxTypeCGST": tax_type_cgst,
                "TaxTypeSGST": tax_type_sgst,
                "TaxTypeIGST": tax_type_igst,
            }
        )
        if amazon_order_id is not UNSET:
            field_dict["AmazonOrderId"] = amazon_order_id
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if marketplace_id is not UNSET:
            field_dict["MarketplaceId"] = marketplace_id
        if transaction_type is not UNSET:
            field_dict["TransactionType"] = transaction_type
        if base_expense is not UNSET:
            field_dict["BaseExpense"] = base_expense
        if total_expense is not UNSET:
            field_dict["TotalExpense"] = total_expense

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        tax_type_cgst = Currency.from_dict(d.pop("TaxTypeCGST"))

        tax_type_sgst = Currency.from_dict(d.pop("TaxTypeSGST"))

        tax_type_igst = Currency.from_dict(d.pop("TaxTypeIGST"))

        amazon_order_id = d.pop("AmazonOrderId", UNSET)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        marketplace_id = d.pop("MarketplaceId", UNSET)

        transaction_type = d.pop("TransactionType", UNSET)

        _base_expense = d.pop("BaseExpense", UNSET)
        base_expense: Union[Unset, Currency]
        if isinstance(_base_expense, Unset):
            base_expense = UNSET
        else:
            base_expense = Currency.from_dict(_base_expense)

        _total_expense = d.pop("TotalExpense", UNSET)
        total_expense: Union[Unset, Currency]
        if isinstance(_total_expense, Unset):
            total_expense = UNSET
        else:
            total_expense = Currency.from_dict(_total_expense)

        result = cls(
            tax_type_cgst=tax_type_cgst,
            tax_type_sgst=tax_type_sgst,
            tax_type_igst=tax_type_igst,
            amazon_order_id=amazon_order_id,
            posted_date=posted_date,
            marketplace_id=marketplace_id,
            transaction_type=transaction_type,
            base_expense=base_expense,
            total_expense=total_expense,
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
