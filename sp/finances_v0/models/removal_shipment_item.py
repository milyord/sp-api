from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="RemovalShipmentItem")


@attr.s(auto_attribs=True)
class RemovalShipmentItem:
    r"""Item-level information for a removal shipment.

    Attributes:
        removal_shipment_item_id (Union[Unset, str]): An identifier for an item in a removal shipment.
        tax_collection_model (Union[Unset, str]): The tax collection model applied to the item.

            Possible values:

            * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the
            seller.

            * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.
        fulfillment_network_sku (Union[Unset, str]): The Amazon fulfillment network SKU for the item.
        quantity (Union[Unset, int]): The quantity of the item.
        revenue (Union[Unset, Currency]): A currency type and amount.
        fee_amount (Union[Unset, Currency]): A currency type and amount.
        tax_amount (Union[Unset, Currency]): A currency type and amount.
        tax_withheld (Union[Unset, Currency]): A currency type and amount.
    """

    removal_shipment_item_id: Union[Unset, str] = UNSET
    tax_collection_model: Union[Unset, str] = UNSET
    fulfillment_network_sku: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    revenue: Union[Unset, "Currency"] = UNSET
    fee_amount: Union[Unset, "Currency"] = UNSET
    tax_amount: Union[Unset, "Currency"] = UNSET
    tax_withheld: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        removal_shipment_item_id = self.removal_shipment_item_id
        tax_collection_model = self.tax_collection_model
        fulfillment_network_sku = self.fulfillment_network_sku
        quantity = self.quantity
        revenue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revenue, Unset):
            revenue = self.revenue.to_dict()

        fee_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fee_amount, Unset):
            fee_amount = self.fee_amount.to_dict()

        tax_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_amount, Unset):
            tax_amount = self.tax_amount.to_dict()

        tax_withheld: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_withheld, Unset):
            tax_withheld = self.tax_withheld.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if removal_shipment_item_id is not UNSET:
            field_dict["RemovalShipmentItemId"] = removal_shipment_item_id
        if tax_collection_model is not UNSET:
            field_dict["TaxCollectionModel"] = tax_collection_model
        if fulfillment_network_sku is not UNSET:
            field_dict["FulfillmentNetworkSKU"] = fulfillment_network_sku
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if revenue is not UNSET:
            field_dict["Revenue"] = revenue
        if fee_amount is not UNSET:
            field_dict["FeeAmount"] = fee_amount
        if tax_amount is not UNSET:
            field_dict["TaxAmount"] = tax_amount
        if tax_withheld is not UNSET:
            field_dict["TaxWithheld"] = tax_withheld

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        removal_shipment_item_id = d.pop("RemovalShipmentItemId", UNSET)

        tax_collection_model = d.pop("TaxCollectionModel", UNSET)

        fulfillment_network_sku = d.pop("FulfillmentNetworkSKU", UNSET)

        quantity = d.pop("Quantity", UNSET)

        _revenue = d.pop("Revenue", UNSET)
        revenue: Union[Unset, Currency]
        if isinstance(_revenue, Unset):
            revenue = UNSET
        else:
            revenue = Currency.from_dict(_revenue)

        _fee_amount = d.pop("FeeAmount", UNSET)
        fee_amount: Union[Unset, Currency]
        if isinstance(_fee_amount, Unset):
            fee_amount = UNSET
        else:
            fee_amount = Currency.from_dict(_fee_amount)

        _tax_amount = d.pop("TaxAmount", UNSET)
        tax_amount: Union[Unset, Currency]
        if isinstance(_tax_amount, Unset):
            tax_amount = UNSET
        else:
            tax_amount = Currency.from_dict(_tax_amount)

        _tax_withheld = d.pop("TaxWithheld", UNSET)
        tax_withheld: Union[Unset, Currency]
        if isinstance(_tax_withheld, Unset):
            tax_withheld = UNSET
        else:
            tax_withheld = Currency.from_dict(_tax_withheld)

        result = cls(
            removal_shipment_item_id=removal_shipment_item_id,
            tax_collection_model=tax_collection_model,
            fulfillment_network_sku=fulfillment_network_sku,
            quantity=quantity,
            revenue=revenue,
            fee_amount=fee_amount,
            tax_amount=tax_amount,
            tax_withheld=tax_withheld,
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
