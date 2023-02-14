import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="SolutionProviderCreditEvent")


@attr.s(auto_attribs=True)
class SolutionProviderCreditEvent:
    r"""A credit given to a solution provider.

    Attributes:
        provider_transaction_type (Union[Unset, str]): The transaction type.
        seller_order_id (Union[Unset, str]): A seller-defined identifier for an order.
        marketplace_id (Union[Unset, str]): The identifier of the marketplace where the order was placed.
        marketplace_country_code (Union[Unset, str]): The two-letter country code of the country associated with the
            marketplace where the order was placed.
        seller_id (Union[Unset, str]): The Amazon-defined identifier of the seller.
        seller_store_name (Union[Unset, str]): The store name where the payment event occurred.
        provider_id (Union[Unset, str]): The Amazon-defined identifier of the solution provider.
        provider_store_name (Union[Unset, str]): The store name where the payment event occurred.
        transaction_amount (Union[Unset, Currency]): A currency type and amount.
        transaction_creation_date (Union[Unset, datetime.datetime]):
    """

    provider_transaction_type: Union[Unset, str] = UNSET
    seller_order_id: Union[Unset, str] = UNSET
    marketplace_id: Union[Unset, str] = UNSET
    marketplace_country_code: Union[Unset, str] = UNSET
    seller_id: Union[Unset, str] = UNSET
    seller_store_name: Union[Unset, str] = UNSET
    provider_id: Union[Unset, str] = UNSET
    provider_store_name: Union[Unset, str] = UNSET
    transaction_amount: Union[Unset, "Currency"] = UNSET
    transaction_creation_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider_transaction_type = self.provider_transaction_type
        seller_order_id = self.seller_order_id
        marketplace_id = self.marketplace_id
        marketplace_country_code = self.marketplace_country_code
        seller_id = self.seller_id
        seller_store_name = self.seller_store_name
        provider_id = self.provider_id
        provider_store_name = self.provider_store_name
        transaction_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transaction_amount, Unset):
            transaction_amount = self.transaction_amount.to_dict()

        transaction_creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_creation_date, Unset):
            transaction_creation_date = self.transaction_creation_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider_transaction_type is not UNSET:
            field_dict["ProviderTransactionType"] = provider_transaction_type
        if seller_order_id is not UNSET:
            field_dict["SellerOrderId"] = seller_order_id
        if marketplace_id is not UNSET:
            field_dict["MarketplaceId"] = marketplace_id
        if marketplace_country_code is not UNSET:
            field_dict["MarketplaceCountryCode"] = marketplace_country_code
        if seller_id is not UNSET:
            field_dict["SellerId"] = seller_id
        if seller_store_name is not UNSET:
            field_dict["SellerStoreName"] = seller_store_name
        if provider_id is not UNSET:
            field_dict["ProviderId"] = provider_id
        if provider_store_name is not UNSET:
            field_dict["ProviderStoreName"] = provider_store_name
        if transaction_amount is not UNSET:
            field_dict["TransactionAmount"] = transaction_amount
        if transaction_creation_date is not UNSET:
            field_dict["TransactionCreationDate"] = transaction_creation_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        provider_transaction_type = d.pop("ProviderTransactionType", UNSET)

        seller_order_id = d.pop("SellerOrderId", UNSET)

        marketplace_id = d.pop("MarketplaceId", UNSET)

        marketplace_country_code = d.pop("MarketplaceCountryCode", UNSET)

        seller_id = d.pop("SellerId", UNSET)

        seller_store_name = d.pop("SellerStoreName", UNSET)

        provider_id = d.pop("ProviderId", UNSET)

        provider_store_name = d.pop("ProviderStoreName", UNSET)

        _transaction_amount = d.pop("TransactionAmount", UNSET)
        transaction_amount: Union[Unset, Currency]
        if isinstance(_transaction_amount, Unset):
            transaction_amount = UNSET
        else:
            transaction_amount = Currency.from_dict(_transaction_amount)

        _transaction_creation_date = d.pop("TransactionCreationDate", UNSET)
        transaction_creation_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_creation_date, Unset):
            transaction_creation_date = UNSET
        else:
            transaction_creation_date = isoparse(_transaction_creation_date)

        result = cls(
            provider_transaction_type=provider_transaction_type,
            seller_order_id=seller_order_id,
            marketplace_id=marketplace_id,
            marketplace_country_code=marketplace_country_code,
            seller_id=seller_id,
            seller_store_name=seller_store_name,
            provider_id=provider_id,
            provider_store_name=provider_store_name,
            transaction_amount=transaction_amount,
            transaction_creation_date=transaction_creation_date,
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
