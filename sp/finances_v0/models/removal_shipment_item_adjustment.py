from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="RemovalShipmentItemAdjustment")


@attr.s(auto_attribs=True)
class RemovalShipmentItemAdjustment:
    r"""Item-level information for a removal shipment item adjustment.

    Attributes:
        removal_shipment_item_id (Union[Unset, str]): An identifier for an item in a removal shipment.
        tax_collection_model (Union[Unset, str]): The tax collection model applied to the item.

            Possible values:

            * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the
            seller.

            * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.
        fulfillment_network_sku (Union[Unset, str]): The Amazon fulfillment network SKU for the item.
        adjusted_quantity (Union[Unset, int]): Adjusted quantity of removal shipmentItemAdjustment items.
        revenue_adjustment (Union[Unset, Currency]): A currency type and amount.
        tax_amount_adjustment (Union[Unset, Currency]): A currency type and amount.
        tax_withheld_adjustment (Union[Unset, Currency]): A currency type and amount.
    """

    removal_shipment_item_id: Union[Unset, str] = UNSET
    tax_collection_model: Union[Unset, str] = UNSET
    fulfillment_network_sku: Union[Unset, str] = UNSET
    adjusted_quantity: Union[Unset, int] = UNSET
    revenue_adjustment: Union[Unset, "Currency"] = UNSET
    tax_amount_adjustment: Union[Unset, "Currency"] = UNSET
    tax_withheld_adjustment: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        removal_shipment_item_id = self.removal_shipment_item_id
        tax_collection_model = self.tax_collection_model
        fulfillment_network_sku = self.fulfillment_network_sku
        adjusted_quantity = self.adjusted_quantity
        revenue_adjustment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revenue_adjustment, Unset):
            revenue_adjustment = self.revenue_adjustment.to_dict()

        tax_amount_adjustment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_amount_adjustment, Unset):
            tax_amount_adjustment = self.tax_amount_adjustment.to_dict()

        tax_withheld_adjustment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_withheld_adjustment, Unset):
            tax_withheld_adjustment = self.tax_withheld_adjustment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if removal_shipment_item_id is not UNSET:
            field_dict["RemovalShipmentItemId"] = removal_shipment_item_id
        if tax_collection_model is not UNSET:
            field_dict["TaxCollectionModel"] = tax_collection_model
        if fulfillment_network_sku is not UNSET:
            field_dict["FulfillmentNetworkSKU"] = fulfillment_network_sku
        if adjusted_quantity is not UNSET:
            field_dict["AdjustedQuantity"] = adjusted_quantity
        if revenue_adjustment is not UNSET:
            field_dict["RevenueAdjustment"] = revenue_adjustment
        if tax_amount_adjustment is not UNSET:
            field_dict["TaxAmountAdjustment"] = tax_amount_adjustment
        if tax_withheld_adjustment is not UNSET:
            field_dict["TaxWithheldAdjustment"] = tax_withheld_adjustment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        removal_shipment_item_id = d.pop("RemovalShipmentItemId", UNSET)

        tax_collection_model = d.pop("TaxCollectionModel", UNSET)

        fulfillment_network_sku = d.pop("FulfillmentNetworkSKU", UNSET)

        adjusted_quantity = d.pop("AdjustedQuantity", UNSET)

        _revenue_adjustment = d.pop("RevenueAdjustment", UNSET)
        revenue_adjustment: Union[Unset, Currency]
        if isinstance(_revenue_adjustment, Unset):
            revenue_adjustment = UNSET
        else:
            revenue_adjustment = Currency.from_dict(_revenue_adjustment)

        _tax_amount_adjustment = d.pop("TaxAmountAdjustment", UNSET)
        tax_amount_adjustment: Union[Unset, Currency]
        if isinstance(_tax_amount_adjustment, Unset):
            tax_amount_adjustment = UNSET
        else:
            tax_amount_adjustment = Currency.from_dict(_tax_amount_adjustment)

        _tax_withheld_adjustment = d.pop("TaxWithheldAdjustment", UNSET)
        tax_withheld_adjustment: Union[Unset, Currency]
        if isinstance(_tax_withheld_adjustment, Unset):
            tax_withheld_adjustment = UNSET
        else:
            tax_withheld_adjustment = Currency.from_dict(_tax_withheld_adjustment)

        result = cls(
            removal_shipment_item_id=removal_shipment_item_id,
            tax_collection_model=tax_collection_model,
            fulfillment_network_sku=fulfillment_network_sku,
            adjusted_quantity=adjusted_quantity,
            revenue_adjustment=revenue_adjustment,
            tax_amount_adjustment=tax_amount_adjustment,
            tax_withheld_adjustment=tax_withheld_adjustment,
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
