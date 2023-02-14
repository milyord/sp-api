from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.order_item_deemed_reseller_category import OrderItemDeemedResellerCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buyer_requested_cancel import BuyerRequestedCancel
    from ..models.item_approval_context import ItemApprovalContext
    from ..models.item_buyer_info import ItemBuyerInfo
    from ..models.money import Money
    from ..models.points_granted_detail import PointsGrantedDetail
    from ..models.product_info_detail import ProductInfoDetail
    from ..models.tax_collection import TaxCollection


T = TypeVar("T", bound="OrderItem")


@attr.s(auto_attribs=True)
class OrderItem:
    r"""A single order item.

    Attributes:
        asin (str): The Amazon Standard Identification Number (ASIN) of the item.
        order_item_id (str): An Amazon-defined order item identifier.
        quantity_ordered (int): The number of items in the order.
        seller_sku (Union[Unset, str]): The seller stock keeping unit (SKU) of the item.
        title (Union[Unset, str]): The name of the item.
        quantity_shipped (Union[Unset, int]): The number of items shipped.
        product_info (Union[Unset, ProductInfoDetail]): Product information on the number of items.
        points_granted (Union[Unset, PointsGrantedDetail]): The number of Amazon Points offered with the purchase of an
            item, and their monetary value.
        item_price (Union[Unset, Money]): The monetary value of the order.
        shipping_price (Union[Unset, Money]): The monetary value of the order.
        item_tax (Union[Unset, Money]): The monetary value of the order.
        shipping_tax (Union[Unset, Money]): The monetary value of the order.
        shipping_discount (Union[Unset, Money]): The monetary value of the order.
        shipping_discount_tax (Union[Unset, Money]): The monetary value of the order.
        promotion_discount (Union[Unset, Money]): The monetary value of the order.
        promotion_discount_tax (Union[Unset, Money]): The monetary value of the order.
        promotion_ids (Union[Unset, List[str]]): A list of promotion identifiers provided by the seller when the
            promotions were created.
        cod_fee (Union[Unset, Money]): The monetary value of the order.
        cod_fee_discount (Union[Unset, Money]): The monetary value of the order.
        is_gift (Union[Unset, bool]): When true, the item is a gift.
        condition_note (Union[Unset, str]): The condition of the item as described by the seller.
        condition_id (Union[Unset, str]): The condition of the item.

            Possible values: New, Used, Collectible, Refurbished, Preorder, Club.
        condition_subtype_id (Union[Unset, str]): The subcondition of the item.

            Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty,
            Refurbished, Open Box, Any, Other.
        scheduled_delivery_start_date (Union[Unset, str]): The start date of the scheduled delivery window in the time
            zone of the order destination. In ISO 8601 date time format.
        scheduled_delivery_end_date (Union[Unset, str]): The end date of the scheduled delivery window in the time zone
            of the order destination. In ISO 8601 date time format.
        price_designation (Union[Unset, str]): Indicates that the selling price is a special price that is available
            only for Amazon Business orders. For more information about the Amazon Business Seller Program, see the [Amazon
            Business website](https://www.amazon.com/b2b/info/amazon-business).

            Possible values: BusinessPrice - A special price that is available only for Amazon Business orders.
        tax_collection (Union[Unset, TaxCollection]): Information about withheld taxes.
        serial_number_required (Union[Unset, bool]): When true, the product type for this item has a serial number.

            Returned only for Amazon Easy Ship orders.
        is_transparency (Union[Unset, bool]): When true, transparency codes are required.
        ioss_number (Union[Unset, str]): The IOSS number for the marketplace. Sellers shipping to the European Union
            (EU) from outside of the EU must provide this IOSS number to their carrier when Amazon has collected the VAT on
            the sale.
        store_chain_store_id (Union[Unset, str]): The store chain store identifier. Linked to a specific store in a
            store chain.
        deemed_reseller_category (Union[Unset, OrderItemDeemedResellerCategory]): The category of deemed reseller. This
            applies to selling partners that are not based in the EU and is used to help them meet the VAT Deemed Reseller
            tax laws in the EU and UK.
        buyer_info (Union[Unset, ItemBuyerInfo]): A single item's buyer information.
        buyer_requested_cancel (Union[Unset, BuyerRequestedCancel]): Information about whether or not a buyer requested
            cancellation.
        item_approval_context (Union[Unset, ItemApprovalContext]): Generic item approval context. Check the applicable
            restrictions at the specific approval type schemas.
        serial_numbers (Union[Unset, List[str]]): A list of serial numbers for electronic products that are shipped to
            customers. Returned for FBA orders only.
    """

    asin: str
    order_item_id: str
    quantity_ordered: int
    seller_sku: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    quantity_shipped: Union[Unset, int] = UNSET
    product_info: Union[Unset, "ProductInfoDetail"] = UNSET
    points_granted: Union[Unset, "PointsGrantedDetail"] = UNSET
    item_price: Union[Unset, "Money"] = UNSET
    shipping_price: Union[Unset, "Money"] = UNSET
    item_tax: Union[Unset, "Money"] = UNSET
    shipping_tax: Union[Unset, "Money"] = UNSET
    shipping_discount: Union[Unset, "Money"] = UNSET
    shipping_discount_tax: Union[Unset, "Money"] = UNSET
    promotion_discount: Union[Unset, "Money"] = UNSET
    promotion_discount_tax: Union[Unset, "Money"] = UNSET
    promotion_ids: Union[Unset, List[str]] = UNSET
    cod_fee: Union[Unset, "Money"] = UNSET
    cod_fee_discount: Union[Unset, "Money"] = UNSET
    is_gift: Union[Unset, bool] = UNSET
    condition_note: Union[Unset, str] = UNSET
    condition_id: Union[Unset, str] = UNSET
    condition_subtype_id: Union[Unset, str] = UNSET
    scheduled_delivery_start_date: Union[Unset, str] = UNSET
    scheduled_delivery_end_date: Union[Unset, str] = UNSET
    price_designation: Union[Unset, str] = UNSET
    tax_collection: Union[Unset, "TaxCollection"] = UNSET
    serial_number_required: Union[Unset, bool] = UNSET
    is_transparency: Union[Unset, bool] = UNSET
    ioss_number: Union[Unset, str] = UNSET
    store_chain_store_id: Union[Unset, str] = UNSET
    deemed_reseller_category: Union[Unset, OrderItemDeemedResellerCategory] = UNSET
    buyer_info: Union[Unset, "ItemBuyerInfo"] = UNSET
    buyer_requested_cancel: Union[Unset, "BuyerRequestedCancel"] = UNSET
    item_approval_context: Union[Unset, "ItemApprovalContext"] = UNSET
    serial_numbers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        order_item_id = self.order_item_id
        quantity_ordered = self.quantity_ordered
        seller_sku = self.seller_sku
        title = self.title
        quantity_shipped = self.quantity_shipped
        product_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_info, Unset):
            product_info = self.product_info.to_dict()

        points_granted: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.points_granted, Unset):
            points_granted = self.points_granted.to_dict()

        item_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_price, Unset):
            item_price = self.item_price.to_dict()

        shipping_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_price, Unset):
            shipping_price = self.shipping_price.to_dict()

        item_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_tax, Unset):
            item_tax = self.item_tax.to_dict()

        shipping_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_tax, Unset):
            shipping_tax = self.shipping_tax.to_dict()

        shipping_discount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_discount, Unset):
            shipping_discount = self.shipping_discount.to_dict()

        shipping_discount_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_discount_tax, Unset):
            shipping_discount_tax = self.shipping_discount_tax.to_dict()

        promotion_discount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promotion_discount, Unset):
            promotion_discount = self.promotion_discount.to_dict()

        promotion_discount_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promotion_discount_tax, Unset):
            promotion_discount_tax = self.promotion_discount_tax.to_dict()

        promotion_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.promotion_ids, Unset):
            promotion_ids = self.promotion_ids

        cod_fee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cod_fee, Unset):
            cod_fee = self.cod_fee.to_dict()

        cod_fee_discount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cod_fee_discount, Unset):
            cod_fee_discount = self.cod_fee_discount.to_dict()

        is_gift = self.is_gift
        condition_note = self.condition_note
        condition_id = self.condition_id
        condition_subtype_id = self.condition_subtype_id
        scheduled_delivery_start_date = self.scheduled_delivery_start_date
        scheduled_delivery_end_date = self.scheduled_delivery_end_date
        price_designation = self.price_designation
        tax_collection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_collection, Unset):
            tax_collection = self.tax_collection.to_dict()

        serial_number_required = self.serial_number_required
        is_transparency = self.is_transparency
        ioss_number = self.ioss_number
        store_chain_store_id = self.store_chain_store_id
        deemed_reseller_category: Union[Unset, str] = UNSET
        if not isinstance(self.deemed_reseller_category, Unset):
            deemed_reseller_category = self.deemed_reseller_category.value

        buyer_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyer_info, Unset):
            buyer_info = self.buyer_info.to_dict()

        buyer_requested_cancel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyer_requested_cancel, Unset):
            buyer_requested_cancel = self.buyer_requested_cancel.to_dict()

        item_approval_context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_approval_context, Unset):
            item_approval_context = self.item_approval_context.to_dict()

        serial_numbers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.serial_numbers, Unset):
            serial_numbers = self.serial_numbers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ASIN": asin,
                "OrderItemId": order_item_id,
                "QuantityOrdered": quantity_ordered,
            }
        )
        if seller_sku is not UNSET:
            field_dict["SellerSKU"] = seller_sku
        if title is not UNSET:
            field_dict["Title"] = title
        if quantity_shipped is not UNSET:
            field_dict["QuantityShipped"] = quantity_shipped
        if product_info is not UNSET:
            field_dict["ProductInfo"] = product_info
        if points_granted is not UNSET:
            field_dict["PointsGranted"] = points_granted
        if item_price is not UNSET:
            field_dict["ItemPrice"] = item_price
        if shipping_price is not UNSET:
            field_dict["ShippingPrice"] = shipping_price
        if item_tax is not UNSET:
            field_dict["ItemTax"] = item_tax
        if shipping_tax is not UNSET:
            field_dict["ShippingTax"] = shipping_tax
        if shipping_discount is not UNSET:
            field_dict["ShippingDiscount"] = shipping_discount
        if shipping_discount_tax is not UNSET:
            field_dict["ShippingDiscountTax"] = shipping_discount_tax
        if promotion_discount is not UNSET:
            field_dict["PromotionDiscount"] = promotion_discount
        if promotion_discount_tax is not UNSET:
            field_dict["PromotionDiscountTax"] = promotion_discount_tax
        if promotion_ids is not UNSET:
            field_dict["PromotionIds"] = promotion_ids
        if cod_fee is not UNSET:
            field_dict["CODFee"] = cod_fee
        if cod_fee_discount is not UNSET:
            field_dict["CODFeeDiscount"] = cod_fee_discount
        if is_gift is not UNSET:
            field_dict["IsGift"] = is_gift
        if condition_note is not UNSET:
            field_dict["ConditionNote"] = condition_note
        if condition_id is not UNSET:
            field_dict["ConditionId"] = condition_id
        if condition_subtype_id is not UNSET:
            field_dict["ConditionSubtypeId"] = condition_subtype_id
        if scheduled_delivery_start_date is not UNSET:
            field_dict["ScheduledDeliveryStartDate"] = scheduled_delivery_start_date
        if scheduled_delivery_end_date is not UNSET:
            field_dict["ScheduledDeliveryEndDate"] = scheduled_delivery_end_date
        if price_designation is not UNSET:
            field_dict["PriceDesignation"] = price_designation
        if tax_collection is not UNSET:
            field_dict["TaxCollection"] = tax_collection
        if serial_number_required is not UNSET:
            field_dict["SerialNumberRequired"] = serial_number_required
        if is_transparency is not UNSET:
            field_dict["IsTransparency"] = is_transparency
        if ioss_number is not UNSET:
            field_dict["IossNumber"] = ioss_number
        if store_chain_store_id is not UNSET:
            field_dict["StoreChainStoreId"] = store_chain_store_id
        if deemed_reseller_category is not UNSET:
            field_dict["DeemedResellerCategory"] = deemed_reseller_category
        if buyer_info is not UNSET:
            field_dict["BuyerInfo"] = buyer_info
        if buyer_requested_cancel is not UNSET:
            field_dict["BuyerRequestedCancel"] = buyer_requested_cancel
        if item_approval_context is not UNSET:
            field_dict["ItemApprovalContext"] = item_approval_context
        if serial_numbers is not UNSET:
            field_dict["SerialNumbers"] = serial_numbers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.buyer_requested_cancel import BuyerRequestedCancel
        from ..models.item_approval_context import ItemApprovalContext
        from ..models.item_buyer_info import ItemBuyerInfo
        from ..models.money import Money
        from ..models.points_granted_detail import PointsGrantedDetail
        from ..models.product_info_detail import ProductInfoDetail
        from ..models.tax_collection import TaxCollection

        d = src_dict.copy()
        asin = d.pop("ASIN")

        order_item_id = d.pop("OrderItemId")

        quantity_ordered = d.pop("QuantityOrdered")

        seller_sku = d.pop("SellerSKU", UNSET)

        title = d.pop("Title", UNSET)

        quantity_shipped = d.pop("QuantityShipped", UNSET)

        _product_info = d.pop("ProductInfo", UNSET)
        product_info: Union[Unset, ProductInfoDetail]
        if isinstance(_product_info, Unset):
            product_info = UNSET
        else:
            product_info = ProductInfoDetail.from_dict(_product_info)

        _points_granted = d.pop("PointsGranted", UNSET)
        points_granted: Union[Unset, PointsGrantedDetail]
        if isinstance(_points_granted, Unset):
            points_granted = UNSET
        else:
            points_granted = PointsGrantedDetail.from_dict(_points_granted)

        _item_price = d.pop("ItemPrice", UNSET)
        item_price: Union[Unset, Money]
        if isinstance(_item_price, Unset):
            item_price = UNSET
        else:
            item_price = Money.from_dict(_item_price)

        _shipping_price = d.pop("ShippingPrice", UNSET)
        shipping_price: Union[Unset, Money]
        if isinstance(_shipping_price, Unset):
            shipping_price = UNSET
        else:
            shipping_price = Money.from_dict(_shipping_price)

        _item_tax = d.pop("ItemTax", UNSET)
        item_tax: Union[Unset, Money]
        if isinstance(_item_tax, Unset):
            item_tax = UNSET
        else:
            item_tax = Money.from_dict(_item_tax)

        _shipping_tax = d.pop("ShippingTax", UNSET)
        shipping_tax: Union[Unset, Money]
        if isinstance(_shipping_tax, Unset):
            shipping_tax = UNSET
        else:
            shipping_tax = Money.from_dict(_shipping_tax)

        _shipping_discount = d.pop("ShippingDiscount", UNSET)
        shipping_discount: Union[Unset, Money]
        if isinstance(_shipping_discount, Unset):
            shipping_discount = UNSET
        else:
            shipping_discount = Money.from_dict(_shipping_discount)

        _shipping_discount_tax = d.pop("ShippingDiscountTax", UNSET)
        shipping_discount_tax: Union[Unset, Money]
        if isinstance(_shipping_discount_tax, Unset):
            shipping_discount_tax = UNSET
        else:
            shipping_discount_tax = Money.from_dict(_shipping_discount_tax)

        _promotion_discount = d.pop("PromotionDiscount", UNSET)
        promotion_discount: Union[Unset, Money]
        if isinstance(_promotion_discount, Unset):
            promotion_discount = UNSET
        else:
            promotion_discount = Money.from_dict(_promotion_discount)

        _promotion_discount_tax = d.pop("PromotionDiscountTax", UNSET)
        promotion_discount_tax: Union[Unset, Money]
        if isinstance(_promotion_discount_tax, Unset):
            promotion_discount_tax = UNSET
        else:
            promotion_discount_tax = Money.from_dict(_promotion_discount_tax)

        promotion_ids = cast(List[str], d.pop("PromotionIds", UNSET))

        _cod_fee = d.pop("CODFee", UNSET)
        cod_fee: Union[Unset, Money]
        if isinstance(_cod_fee, Unset):
            cod_fee = UNSET
        else:
            cod_fee = Money.from_dict(_cod_fee)

        _cod_fee_discount = d.pop("CODFeeDiscount", UNSET)
        cod_fee_discount: Union[Unset, Money]
        if isinstance(_cod_fee_discount, Unset):
            cod_fee_discount = UNSET
        else:
            cod_fee_discount = Money.from_dict(_cod_fee_discount)

        is_gift = d.pop("IsGift", UNSET)

        condition_note = d.pop("ConditionNote", UNSET)

        condition_id = d.pop("ConditionId", UNSET)

        condition_subtype_id = d.pop("ConditionSubtypeId", UNSET)

        scheduled_delivery_start_date = d.pop("ScheduledDeliveryStartDate", UNSET)

        scheduled_delivery_end_date = d.pop("ScheduledDeliveryEndDate", UNSET)

        price_designation = d.pop("PriceDesignation", UNSET)

        _tax_collection = d.pop("TaxCollection", UNSET)
        tax_collection: Union[Unset, TaxCollection]
        if isinstance(_tax_collection, Unset):
            tax_collection = UNSET
        else:
            tax_collection = TaxCollection.from_dict(_tax_collection)

        serial_number_required = d.pop("SerialNumberRequired", UNSET)

        is_transparency = d.pop("IsTransparency", UNSET)

        ioss_number = d.pop("IossNumber", UNSET)

        store_chain_store_id = d.pop("StoreChainStoreId", UNSET)

        _deemed_reseller_category = d.pop("DeemedResellerCategory", UNSET)
        deemed_reseller_category: Union[Unset, OrderItemDeemedResellerCategory]
        if isinstance(_deemed_reseller_category, Unset):
            deemed_reseller_category = UNSET
        else:
            deemed_reseller_category = OrderItemDeemedResellerCategory(_deemed_reseller_category)

        _buyer_info = d.pop("BuyerInfo", UNSET)
        buyer_info: Union[Unset, ItemBuyerInfo]
        if isinstance(_buyer_info, Unset):
            buyer_info = UNSET
        else:
            buyer_info = ItemBuyerInfo.from_dict(_buyer_info)

        _buyer_requested_cancel = d.pop("BuyerRequestedCancel", UNSET)
        buyer_requested_cancel: Union[Unset, BuyerRequestedCancel]
        if isinstance(_buyer_requested_cancel, Unset):
            buyer_requested_cancel = UNSET
        else:
            buyer_requested_cancel = BuyerRequestedCancel.from_dict(_buyer_requested_cancel)

        _item_approval_context = d.pop("ItemApprovalContext", UNSET)
        item_approval_context: Union[Unset, ItemApprovalContext]
        if isinstance(_item_approval_context, Unset):
            item_approval_context = UNSET
        else:
            item_approval_context = ItemApprovalContext.from_dict(_item_approval_context)

        serial_numbers = cast(List[str], d.pop("SerialNumbers", UNSET))

        result = cls(
            asin=asin,
            order_item_id=order_item_id,
            quantity_ordered=quantity_ordered,
            seller_sku=seller_sku,
            title=title,
            quantity_shipped=quantity_shipped,
            product_info=product_info,
            points_granted=points_granted,
            item_price=item_price,
            shipping_price=shipping_price,
            item_tax=item_tax,
            shipping_tax=shipping_tax,
            shipping_discount=shipping_discount,
            shipping_discount_tax=shipping_discount_tax,
            promotion_discount=promotion_discount,
            promotion_discount_tax=promotion_discount_tax,
            promotion_ids=promotion_ids,
            cod_fee=cod_fee,
            cod_fee_discount=cod_fee_discount,
            is_gift=is_gift,
            condition_note=condition_note,
            condition_id=condition_id,
            condition_subtype_id=condition_subtype_id,
            scheduled_delivery_start_date=scheduled_delivery_start_date,
            scheduled_delivery_end_date=scheduled_delivery_end_date,
            price_designation=price_designation,
            tax_collection=tax_collection,
            serial_number_required=serial_number_required,
            is_transparency=is_transparency,
            ioss_number=ioss_number,
            store_chain_store_id=store_chain_store_id,
            deemed_reseller_category=deemed_reseller_category,
            buyer_info=buyer_info,
            buyer_requested_cancel=buyer_requested_cancel,
            item_approval_context=item_approval_context,
            serial_numbers=serial_numbers,
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
