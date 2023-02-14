import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.buyer_tax_info import BuyerTaxInfo
    from ..models.marketplace_tax_info import MarketplaceTaxInfo
    from ..models.shipment_item import ShipmentItem


T = TypeVar("T", bound="ShipmentDetail")


@attr.s(auto_attribs=True)
class ShipmentDetail:
    r"""The information required by a selling partner to issue a shipment invoice.

    Attributes:
        warehouse_id (Union[Unset, str]): The Amazon-defined identifier for the warehouse.
        amazon_order_id (Union[Unset, str]): The Amazon-defined identifier for the order.
        amazon_shipment_id (Union[Unset, str]): The Amazon-defined identifier for the shipment.
        purchase_date (Union[Unset, datetime.datetime]): The date and time when the order was created.
        shipping_address (Union[Unset, Address]): The shipping address details of the shipment.
        payment_method_details (Union[Unset, List[str]]): The list of payment method details.
        marketplace_id (Union[Unset, str]): The identifier for the marketplace where the order was placed.
        seller_id (Union[Unset, str]): The seller identifier.
        buyer_name (Union[Unset, str]): The name of the buyer.
        buyer_county (Union[Unset, str]): The county of the buyer.
        buyer_tax_info (Union[Unset, BuyerTaxInfo]): Tax information about the buyer.
        marketplace_tax_info (Union[Unset, MarketplaceTaxInfo]): Tax information about the marketplace.
        seller_display_name (Union[Unset, str]): The seller’s friendly name registered in the marketplace.
        shipment_items (Union[Unset, List['ShipmentItem']]): A list of shipment items.
    """

    warehouse_id: Union[Unset, str] = UNSET
    amazon_order_id: Union[Unset, str] = UNSET
    amazon_shipment_id: Union[Unset, str] = UNSET
    purchase_date: Union[Unset, datetime.datetime] = UNSET
    shipping_address: Union[Unset, "Address"] = UNSET
    payment_method_details: Union[Unset, List[str]] = UNSET
    marketplace_id: Union[Unset, str] = UNSET
    seller_id: Union[Unset, str] = UNSET
    buyer_name: Union[Unset, str] = UNSET
    buyer_county: Union[Unset, str] = UNSET
    buyer_tax_info: Union[Unset, "BuyerTaxInfo"] = UNSET
    marketplace_tax_info: Union[Unset, "MarketplaceTaxInfo"] = UNSET
    seller_display_name: Union[Unset, str] = UNSET
    shipment_items: Union[Unset, List["ShipmentItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        warehouse_id = self.warehouse_id
        amazon_order_id = self.amazon_order_id
        amazon_shipment_id = self.amazon_shipment_id
        purchase_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchase_date, Unset):
            purchase_date = self.purchase_date.isoformat()

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        payment_method_details: Union[Unset, List[str]] = UNSET
        if not isinstance(self.payment_method_details, Unset):
            payment_method_details = self.payment_method_details

        marketplace_id = self.marketplace_id
        seller_id = self.seller_id
        buyer_name = self.buyer_name
        buyer_county = self.buyer_county
        buyer_tax_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyer_tax_info, Unset):
            buyer_tax_info = self.buyer_tax_info.to_dict()

        marketplace_tax_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.marketplace_tax_info, Unset):
            marketplace_tax_info = self.marketplace_tax_info.to_dict()

        seller_display_name = self.seller_display_name
        shipment_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_items, Unset):
            shipment_items = []
            for componentsschemas_shipment_items_item_data in self.shipment_items:
                componentsschemas_shipment_items_item = componentsschemas_shipment_items_item_data.to_dict()

                shipment_items.append(componentsschemas_shipment_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warehouse_id is not UNSET:
            field_dict["WarehouseId"] = warehouse_id
        if amazon_order_id is not UNSET:
            field_dict["AmazonOrderId"] = amazon_order_id
        if amazon_shipment_id is not UNSET:
            field_dict["AmazonShipmentId"] = amazon_shipment_id
        if purchase_date is not UNSET:
            field_dict["PurchaseDate"] = purchase_date
        if shipping_address is not UNSET:
            field_dict["ShippingAddress"] = shipping_address
        if payment_method_details is not UNSET:
            field_dict["PaymentMethodDetails"] = payment_method_details
        if marketplace_id is not UNSET:
            field_dict["MarketplaceId"] = marketplace_id
        if seller_id is not UNSET:
            field_dict["SellerId"] = seller_id
        if buyer_name is not UNSET:
            field_dict["BuyerName"] = buyer_name
        if buyer_county is not UNSET:
            field_dict["BuyerCounty"] = buyer_county
        if buyer_tax_info is not UNSET:
            field_dict["BuyerTaxInfo"] = buyer_tax_info
        if marketplace_tax_info is not UNSET:
            field_dict["MarketplaceTaxInfo"] = marketplace_tax_info
        if seller_display_name is not UNSET:
            field_dict["SellerDisplayName"] = seller_display_name
        if shipment_items is not UNSET:
            field_dict["ShipmentItems"] = shipment_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.buyer_tax_info import BuyerTaxInfo
        from ..models.marketplace_tax_info import MarketplaceTaxInfo
        from ..models.shipment_item import ShipmentItem

        d = src_dict.copy()
        warehouse_id = d.pop("WarehouseId", UNSET)

        amazon_order_id = d.pop("AmazonOrderId", UNSET)

        amazon_shipment_id = d.pop("AmazonShipmentId", UNSET)

        _purchase_date = d.pop("PurchaseDate", UNSET)
        purchase_date: Union[Unset, datetime.datetime]
        if isinstance(_purchase_date, Unset):
            purchase_date = UNSET
        else:
            purchase_date = isoparse(_purchase_date)

        _shipping_address = d.pop("ShippingAddress", UNSET)
        shipping_address: Union[Unset, Address]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = Address.from_dict(_shipping_address)

        payment_method_details = cast(List[str], d.pop("PaymentMethodDetails", UNSET))

        marketplace_id = d.pop("MarketplaceId", UNSET)

        seller_id = d.pop("SellerId", UNSET)

        buyer_name = d.pop("BuyerName", UNSET)

        buyer_county = d.pop("BuyerCounty", UNSET)

        _buyer_tax_info = d.pop("BuyerTaxInfo", UNSET)
        buyer_tax_info: Union[Unset, BuyerTaxInfo]
        if isinstance(_buyer_tax_info, Unset):
            buyer_tax_info = UNSET
        else:
            buyer_tax_info = BuyerTaxInfo.from_dict(_buyer_tax_info)

        _marketplace_tax_info = d.pop("MarketplaceTaxInfo", UNSET)
        marketplace_tax_info: Union[Unset, MarketplaceTaxInfo]
        if isinstance(_marketplace_tax_info, Unset):
            marketplace_tax_info = UNSET
        else:
            marketplace_tax_info = MarketplaceTaxInfo.from_dict(_marketplace_tax_info)

        seller_display_name = d.pop("SellerDisplayName", UNSET)

        shipment_items = []
        _shipment_items = d.pop("ShipmentItems", UNSET)
        for componentsschemas_shipment_items_item_data in _shipment_items or []:
            componentsschemas_shipment_items_item = ShipmentItem.from_dict(componentsschemas_shipment_items_item_data)

            shipment_items.append(componentsschemas_shipment_items_item)

        result = cls(
            warehouse_id=warehouse_id,
            amazon_order_id=amazon_order_id,
            amazon_shipment_id=amazon_shipment_id,
            purchase_date=purchase_date,
            shipping_address=shipping_address,
            payment_method_details=payment_method_details,
            marketplace_id=marketplace_id,
            seller_id=seller_id,
            buyer_name=buyer_name,
            buyer_county=buyer_county,
            buyer_tax_info=buyer_tax_info,
            marketplace_tax_info=marketplace_tax_info,
            seller_display_name=seller_display_name,
            shipment_items=shipment_items,
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
