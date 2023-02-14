from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.easy_ship_shipment_status import EasyShipShipmentStatus
from ..models.electronic_invoice_status import ElectronicInvoiceStatus
from ..models.item_approval_status import ItemApprovalStatus
from ..models.item_approval_type import ItemApprovalType
from ..models.order_buyer_invoice_preference import OrderBuyerInvoicePreference
from ..models.order_fulfillment_channel import OrderFulfillmentChannel
from ..models.order_order_status import OrderOrderStatus
from ..models.order_order_type import OrderOrderType
from ..models.order_payment_method import OrderPaymentMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.automated_shipping_settings import AutomatedShippingSettings
    from ..models.buyer_info import BuyerInfo
    from ..models.buyer_tax_information import BuyerTaxInformation
    from ..models.fulfillment_instruction import FulfillmentInstruction
    from ..models.marketplace_tax_info import MarketplaceTaxInfo
    from ..models.money import Money
    from ..models.payment_execution_detail_item import PaymentExecutionDetailItem


T = TypeVar("T", bound="Order")


@attr.s(auto_attribs=True)
class Order:
    r"""Order information.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier, in 3-7-7 format.
        purchase_date (str): The date when the order was created.
        last_update_date (str): The date when the order was last updated.

            __Note__: LastUpdateDate is returned with an incorrect date for orders that were last updated before 2009-04-01.
        order_status (OrderOrderStatus): The current order status.
        seller_order_id (Union[Unset, str]): A seller-defined order identifier.
        fulfillment_channel (Union[Unset, OrderFulfillmentChannel]): Whether the order was fulfilled by Amazon (AFN) or
            by the seller (MFN).
        sales_channel (Union[Unset, str]): The sales channel of the first item in the order.
        order_channel (Union[Unset, str]): The order channel of the first item in the order.
        ship_service_level (Union[Unset, str]): The shipment service level of the order.
        order_total (Union[Unset, Money]): The monetary value of the order.
        number_of_items_shipped (Union[Unset, int]): The number of items shipped.
        number_of_items_unshipped (Union[Unset, int]): The number of items unshipped.
        payment_execution_detail (Union[Unset, List['PaymentExecutionDetailItem']]): A list of payment execution detail
            items.
        payment_method (Union[Unset, OrderPaymentMethod]): The payment method for the order. This property is limited to
            Cash On Delivery (COD) and Convenience Store (CVS) payment methods. Unless you need the specific COD payment
            information provided by the PaymentExecutionDetailItem object, we recommend using the PaymentMethodDetails
            property to get payment method information.
        payment_method_details (Union[Unset, List[str]]): A list of payment method detail items.
        marketplace_id (Union[Unset, str]): The identifier for the marketplace where the order was placed.
        shipment_service_level_category (Union[Unset, str]): The shipment service level category of the order.

            Possible values: Expedited, FreeEconomy, NextDay, SameDay, SecondDay, Scheduled, Standard.
        easy_ship_shipment_status (Union[Unset, EasyShipShipmentStatus]): The status of the Amazon Easy Ship order. This
            property is included only for Amazon Easy Ship orders.
        cba_displayable_shipping_label (Union[Unset, str]): Custom ship label for Checkout by Amazon (CBA).
        order_type (Union[Unset, OrderOrderType]): The type of the order.
        earliest_ship_date (Union[Unset, str]): The start of the time period within which you have committed to ship the
            order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.

            __Note__: EarliestShipDate might not be returned for orders placed before February 1, 2013.
        latest_ship_date (Union[Unset, str]): The end of the time period within which you have committed to ship the
            order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.

            __Note__: LatestShipDate might not be returned for orders placed before February 1, 2013.
        earliest_delivery_date (Union[Unset, str]): The start of the time period within which you have committed to
            fulfill the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.
        latest_delivery_date (Union[Unset, str]): The end of the time period within which you have committed to fulfill
            the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders that do not have a
            PendingAvailability, Pending, or Canceled status.
        is_business_order (Union[Unset, bool]): When true, the order is an Amazon Business order. An Amazon Business
            order is an order where the buyer is a Verified Business Buyer.
        is_prime (Union[Unset, bool]): When true, the order is a seller-fulfilled Amazon Prime order.
        is_premium_order (Union[Unset, bool]): When true, the order has a Premium Shipping Service Level Agreement. For
            more information about Premium Shipping orders, see "Premium Shipping Options" in the Seller Central Help for
            your marketplace.
        is_global_express_enabled (Union[Unset, bool]): When true, the order is a GlobalExpress order.
        replaced_order_id (Union[Unset, str]): The order ID value for the order that is being replaced. Returned only if
            IsReplacementOrder = true.
        is_replacement_order (Union[Unset, bool]): When true, this is a replacement order.
        promise_response_due_date (Union[Unset, str]): Indicates the date by which the seller must respond to the buyer
            with an estimated ship date. Returned only for Sourcing on Demand orders.
        is_estimated_ship_date_set (Union[Unset, bool]): When true, the estimated ship date is set for the order.
            Returned only for Sourcing on Demand orders.
        is_sold_by_ab (Union[Unset, bool]): When true, the item within this order was bought and re-sold by Amazon
            Business EU SARL (ABEU). By buying and instantly re-selling your items, ABEU becomes the seller of record,
            making your inventory available for sale to customers who would not otherwise purchase from a third-party
            seller.
        is_iba (Union[Unset, bool]): When true, the item within this order was bought and re-sold by Amazon Business EU
            SARL (ABEU). By buying and instantly re-selling your items, ABEU becomes the seller of record, making your
            inventory available for sale to customers who would not otherwise purchase from a third-party seller.
        default_ship_from_location_address (Union[Unset, Address]): The shipping address for the order.
        buyer_invoice_preference (Union[Unset, OrderBuyerInvoicePreference]): The buyer's invoicing preference.
            Available only in the TR marketplace.
        buyer_tax_information (Union[Unset, BuyerTaxInformation]): Contains the business invoice tax information.
            Available only in the TR marketplace.
        fulfillment_instruction (Union[Unset, FulfillmentInstruction]): Contains the instructions about the fulfillment
            like where should it be fulfilled from.
        is_ispu (Union[Unset, bool]): When true, this order is marked to be picked up from a store rather than
            delivered.
        is_access_point_order (Union[Unset, bool]): When true, this order is marked to be delivered to an Access Point.
            The access location is chosen by the customer. Access Points include Amazon Hub Lockers, Amazon Hub Counters,
            and pickup points operated by carriers.
        marketplace_tax_info (Union[Unset, MarketplaceTaxInfo]): Tax information about the marketplace.
        seller_display_name (Union[Unset, str]): The seller’s friendly name registered in the marketplace.
        shipping_address (Union[Unset, Address]): The shipping address for the order.
        buyer_info (Union[Unset, BuyerInfo]): Buyer information.
        automated_shipping_settings (Union[Unset, AutomatedShippingSettings]): Contains information regarding the
            Shipping Settings Automation program, such as whether the order's shipping settings were generated
            automatically, and what those settings are.
        has_regulated_items (Union[Unset, bool]): Whether the order contains regulated items which may require
            additional approval steps before being fulfilled.
        electronic_invoice_status (Union[Unset, ElectronicInvoiceStatus]): The status of the electronic invoice.
        item_approval_types (Union[Unset, List[ItemApprovalType]]): Set of approval types which applies to at least one
            order item in the order.
        item_approval_status (Union[Unset, List[ItemApprovalStatus]]): Subset of all ItemApprovalStatus that are set in
            at least one of the order items subject to approvals.
    """

    amazon_order_id: str
    purchase_date: str
    last_update_date: str
    order_status: OrderOrderStatus
    seller_order_id: Union[Unset, str] = UNSET
    fulfillment_channel: Union[Unset, OrderFulfillmentChannel] = UNSET
    sales_channel: Union[Unset, str] = UNSET
    order_channel: Union[Unset, str] = UNSET
    ship_service_level: Union[Unset, str] = UNSET
    order_total: Union[Unset, "Money"] = UNSET
    number_of_items_shipped: Union[Unset, int] = UNSET
    number_of_items_unshipped: Union[Unset, int] = UNSET
    payment_execution_detail: Union[Unset, List["PaymentExecutionDetailItem"]] = UNSET
    payment_method: Union[Unset, OrderPaymentMethod] = UNSET
    payment_method_details: Union[Unset, List[str]] = UNSET
    marketplace_id: Union[Unset, str] = UNSET
    shipment_service_level_category: Union[Unset, str] = UNSET
    easy_ship_shipment_status: Union[Unset, EasyShipShipmentStatus] = UNSET
    cba_displayable_shipping_label: Union[Unset, str] = UNSET
    order_type: Union[Unset, OrderOrderType] = UNSET
    earliest_ship_date: Union[Unset, str] = UNSET
    latest_ship_date: Union[Unset, str] = UNSET
    earliest_delivery_date: Union[Unset, str] = UNSET
    latest_delivery_date: Union[Unset, str] = UNSET
    is_business_order: Union[Unset, bool] = UNSET
    is_prime: Union[Unset, bool] = UNSET
    is_premium_order: Union[Unset, bool] = UNSET
    is_global_express_enabled: Union[Unset, bool] = UNSET
    replaced_order_id: Union[Unset, str] = UNSET
    is_replacement_order: Union[Unset, bool] = UNSET
    promise_response_due_date: Union[Unset, str] = UNSET
    is_estimated_ship_date_set: Union[Unset, bool] = UNSET
    is_sold_by_ab: Union[Unset, bool] = UNSET
    is_iba: Union[Unset, bool] = UNSET
    default_ship_from_location_address: Union[Unset, "Address"] = UNSET
    buyer_invoice_preference: Union[Unset, OrderBuyerInvoicePreference] = UNSET
    buyer_tax_information: Union[Unset, "BuyerTaxInformation"] = UNSET
    fulfillment_instruction: Union[Unset, "FulfillmentInstruction"] = UNSET
    is_ispu: Union[Unset, bool] = UNSET
    is_access_point_order: Union[Unset, bool] = UNSET
    marketplace_tax_info: Union[Unset, "MarketplaceTaxInfo"] = UNSET
    seller_display_name: Union[Unset, str] = UNSET
    shipping_address: Union[Unset, "Address"] = UNSET
    buyer_info: Union[Unset, "BuyerInfo"] = UNSET
    automated_shipping_settings: Union[Unset, "AutomatedShippingSettings"] = UNSET
    has_regulated_items: Union[Unset, bool] = UNSET
    electronic_invoice_status: Union[Unset, ElectronicInvoiceStatus] = UNSET
    item_approval_types: Union[Unset, List[ItemApprovalType]] = UNSET
    item_approval_status: Union[Unset, List[ItemApprovalStatus]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        purchase_date = self.purchase_date
        last_update_date = self.last_update_date
        order_status = self.order_status.value

        seller_order_id = self.seller_order_id
        fulfillment_channel: Union[Unset, str] = UNSET
        if not isinstance(self.fulfillment_channel, Unset):
            fulfillment_channel = self.fulfillment_channel.value

        sales_channel = self.sales_channel
        order_channel = self.order_channel
        ship_service_level = self.ship_service_level
        order_total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_total, Unset):
            order_total = self.order_total.to_dict()

        number_of_items_shipped = self.number_of_items_shipped
        number_of_items_unshipped = self.number_of_items_unshipped
        payment_execution_detail: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payment_execution_detail, Unset):
            payment_execution_detail = []
            for componentsschemas_payment_execution_detail_item_list_item_data in self.payment_execution_detail:
                componentsschemas_payment_execution_detail_item_list_item = (
                    componentsschemas_payment_execution_detail_item_list_item_data.to_dict()
                )

                payment_execution_detail.append(componentsschemas_payment_execution_detail_item_list_item)

        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.value

        payment_method_details: Union[Unset, List[str]] = UNSET
        if not isinstance(self.payment_method_details, Unset):
            payment_method_details = self.payment_method_details

        marketplace_id = self.marketplace_id
        shipment_service_level_category = self.shipment_service_level_category
        easy_ship_shipment_status: Union[Unset, str] = UNSET
        if not isinstance(self.easy_ship_shipment_status, Unset):
            easy_ship_shipment_status = self.easy_ship_shipment_status.value

        cba_displayable_shipping_label = self.cba_displayable_shipping_label
        order_type: Union[Unset, str] = UNSET
        if not isinstance(self.order_type, Unset):
            order_type = self.order_type.value

        earliest_ship_date = self.earliest_ship_date
        latest_ship_date = self.latest_ship_date
        earliest_delivery_date = self.earliest_delivery_date
        latest_delivery_date = self.latest_delivery_date
        is_business_order = self.is_business_order
        is_prime = self.is_prime
        is_premium_order = self.is_premium_order
        is_global_express_enabled = self.is_global_express_enabled
        replaced_order_id = self.replaced_order_id
        is_replacement_order = self.is_replacement_order
        promise_response_due_date = self.promise_response_due_date
        is_estimated_ship_date_set = self.is_estimated_ship_date_set
        is_sold_by_ab = self.is_sold_by_ab
        is_iba = self.is_iba
        default_ship_from_location_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_ship_from_location_address, Unset):
            default_ship_from_location_address = self.default_ship_from_location_address.to_dict()

        buyer_invoice_preference: Union[Unset, str] = UNSET
        if not isinstance(self.buyer_invoice_preference, Unset):
            buyer_invoice_preference = self.buyer_invoice_preference.value

        buyer_tax_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyer_tax_information, Unset):
            buyer_tax_information = self.buyer_tax_information.to_dict()

        fulfillment_instruction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fulfillment_instruction, Unset):
            fulfillment_instruction = self.fulfillment_instruction.to_dict()

        is_ispu = self.is_ispu
        is_access_point_order = self.is_access_point_order
        marketplace_tax_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.marketplace_tax_info, Unset):
            marketplace_tax_info = self.marketplace_tax_info.to_dict()

        seller_display_name = self.seller_display_name
        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        buyer_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyer_info, Unset):
            buyer_info = self.buyer_info.to_dict()

        automated_shipping_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.automated_shipping_settings, Unset):
            automated_shipping_settings = self.automated_shipping_settings.to_dict()

        has_regulated_items = self.has_regulated_items
        electronic_invoice_status: Union[Unset, str] = UNSET
        if not isinstance(self.electronic_invoice_status, Unset):
            electronic_invoice_status = self.electronic_invoice_status.value

        item_approval_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.item_approval_types, Unset):
            item_approval_types = []
            for item_approval_types_item_data in self.item_approval_types:
                item_approval_types_item = item_approval_types_item_data.value

                item_approval_types.append(item_approval_types_item)

        item_approval_status: Union[Unset, List[str]] = UNSET
        if not isinstance(self.item_approval_status, Unset):
            item_approval_status = []
            for item_approval_status_item_data in self.item_approval_status:
                item_approval_status_item = item_approval_status_item_data.value

                item_approval_status.append(item_approval_status_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AmazonOrderId": amazon_order_id,
                "PurchaseDate": purchase_date,
                "LastUpdateDate": last_update_date,
                "OrderStatus": order_status,
            }
        )
        if seller_order_id is not UNSET:
            field_dict["SellerOrderId"] = seller_order_id
        if fulfillment_channel is not UNSET:
            field_dict["FulfillmentChannel"] = fulfillment_channel
        if sales_channel is not UNSET:
            field_dict["SalesChannel"] = sales_channel
        if order_channel is not UNSET:
            field_dict["OrderChannel"] = order_channel
        if ship_service_level is not UNSET:
            field_dict["ShipServiceLevel"] = ship_service_level
        if order_total is not UNSET:
            field_dict["OrderTotal"] = order_total
        if number_of_items_shipped is not UNSET:
            field_dict["NumberOfItemsShipped"] = number_of_items_shipped
        if number_of_items_unshipped is not UNSET:
            field_dict["NumberOfItemsUnshipped"] = number_of_items_unshipped
        if payment_execution_detail is not UNSET:
            field_dict["PaymentExecutionDetail"] = payment_execution_detail
        if payment_method is not UNSET:
            field_dict["PaymentMethod"] = payment_method
        if payment_method_details is not UNSET:
            field_dict["PaymentMethodDetails"] = payment_method_details
        if marketplace_id is not UNSET:
            field_dict["MarketplaceId"] = marketplace_id
        if shipment_service_level_category is not UNSET:
            field_dict["ShipmentServiceLevelCategory"] = shipment_service_level_category
        if easy_ship_shipment_status is not UNSET:
            field_dict["EasyShipShipmentStatus"] = easy_ship_shipment_status
        if cba_displayable_shipping_label is not UNSET:
            field_dict["CbaDisplayableShippingLabel"] = cba_displayable_shipping_label
        if order_type is not UNSET:
            field_dict["OrderType"] = order_type
        if earliest_ship_date is not UNSET:
            field_dict["EarliestShipDate"] = earliest_ship_date
        if latest_ship_date is not UNSET:
            field_dict["LatestShipDate"] = latest_ship_date
        if earliest_delivery_date is not UNSET:
            field_dict["EarliestDeliveryDate"] = earliest_delivery_date
        if latest_delivery_date is not UNSET:
            field_dict["LatestDeliveryDate"] = latest_delivery_date
        if is_business_order is not UNSET:
            field_dict["IsBusinessOrder"] = is_business_order
        if is_prime is not UNSET:
            field_dict["IsPrime"] = is_prime
        if is_premium_order is not UNSET:
            field_dict["IsPremiumOrder"] = is_premium_order
        if is_global_express_enabled is not UNSET:
            field_dict["IsGlobalExpressEnabled"] = is_global_express_enabled
        if replaced_order_id is not UNSET:
            field_dict["ReplacedOrderId"] = replaced_order_id
        if is_replacement_order is not UNSET:
            field_dict["IsReplacementOrder"] = is_replacement_order
        if promise_response_due_date is not UNSET:
            field_dict["PromiseResponseDueDate"] = promise_response_due_date
        if is_estimated_ship_date_set is not UNSET:
            field_dict["IsEstimatedShipDateSet"] = is_estimated_ship_date_set
        if is_sold_by_ab is not UNSET:
            field_dict["IsSoldByAB"] = is_sold_by_ab
        if is_iba is not UNSET:
            field_dict["IsIBA"] = is_iba
        if default_ship_from_location_address is not UNSET:
            field_dict["DefaultShipFromLocationAddress"] = default_ship_from_location_address
        if buyer_invoice_preference is not UNSET:
            field_dict["BuyerInvoicePreference"] = buyer_invoice_preference
        if buyer_tax_information is not UNSET:
            field_dict["BuyerTaxInformation"] = buyer_tax_information
        if fulfillment_instruction is not UNSET:
            field_dict["FulfillmentInstruction"] = fulfillment_instruction
        if is_ispu is not UNSET:
            field_dict["IsISPU"] = is_ispu
        if is_access_point_order is not UNSET:
            field_dict["IsAccessPointOrder"] = is_access_point_order
        if marketplace_tax_info is not UNSET:
            field_dict["MarketplaceTaxInfo"] = marketplace_tax_info
        if seller_display_name is not UNSET:
            field_dict["SellerDisplayName"] = seller_display_name
        if shipping_address is not UNSET:
            field_dict["ShippingAddress"] = shipping_address
        if buyer_info is not UNSET:
            field_dict["BuyerInfo"] = buyer_info
        if automated_shipping_settings is not UNSET:
            field_dict["AutomatedShippingSettings"] = automated_shipping_settings
        if has_regulated_items is not UNSET:
            field_dict["HasRegulatedItems"] = has_regulated_items
        if electronic_invoice_status is not UNSET:
            field_dict["ElectronicInvoiceStatus"] = electronic_invoice_status
        if item_approval_types is not UNSET:
            field_dict["ItemApprovalTypes"] = item_approval_types
        if item_approval_status is not UNSET:
            field_dict["ItemApprovalStatus"] = item_approval_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.automated_shipping_settings import AutomatedShippingSettings
        from ..models.buyer_info import BuyerInfo
        from ..models.buyer_tax_information import BuyerTaxInformation
        from ..models.fulfillment_instruction import FulfillmentInstruction
        from ..models.marketplace_tax_info import MarketplaceTaxInfo
        from ..models.money import Money
        from ..models.payment_execution_detail_item import PaymentExecutionDetailItem

        d = src_dict.copy()
        amazon_order_id = d.pop("AmazonOrderId")

        purchase_date = d.pop("PurchaseDate")

        last_update_date = d.pop("LastUpdateDate")

        order_status = OrderOrderStatus(d.pop("OrderStatus"))

        seller_order_id = d.pop("SellerOrderId", UNSET)

        _fulfillment_channel = d.pop("FulfillmentChannel", UNSET)
        fulfillment_channel: Union[Unset, OrderFulfillmentChannel]
        if isinstance(_fulfillment_channel, Unset):
            fulfillment_channel = UNSET
        else:
            fulfillment_channel = OrderFulfillmentChannel(_fulfillment_channel)

        sales_channel = d.pop("SalesChannel", UNSET)

        order_channel = d.pop("OrderChannel", UNSET)

        ship_service_level = d.pop("ShipServiceLevel", UNSET)

        _order_total = d.pop("OrderTotal", UNSET)
        order_total: Union[Unset, Money]
        if isinstance(_order_total, Unset):
            order_total = UNSET
        else:
            order_total = Money.from_dict(_order_total)

        number_of_items_shipped = d.pop("NumberOfItemsShipped", UNSET)

        number_of_items_unshipped = d.pop("NumberOfItemsUnshipped", UNSET)

        payment_execution_detail = []
        _payment_execution_detail = d.pop("PaymentExecutionDetail", UNSET)
        for componentsschemas_payment_execution_detail_item_list_item_data in _payment_execution_detail or []:
            componentsschemas_payment_execution_detail_item_list_item = PaymentExecutionDetailItem.from_dict(
                componentsschemas_payment_execution_detail_item_list_item_data
            )

            payment_execution_detail.append(componentsschemas_payment_execution_detail_item_list_item)

        _payment_method = d.pop("PaymentMethod", UNSET)
        payment_method: Union[Unset, OrderPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = OrderPaymentMethod(_payment_method)

        payment_method_details = cast(List[str], d.pop("PaymentMethodDetails", UNSET))

        marketplace_id = d.pop("MarketplaceId", UNSET)

        shipment_service_level_category = d.pop("ShipmentServiceLevelCategory", UNSET)

        _easy_ship_shipment_status = d.pop("EasyShipShipmentStatus", UNSET)
        easy_ship_shipment_status: Union[Unset, EasyShipShipmentStatus]
        if isinstance(_easy_ship_shipment_status, Unset):
            easy_ship_shipment_status = UNSET
        else:
            easy_ship_shipment_status = EasyShipShipmentStatus(_easy_ship_shipment_status)

        cba_displayable_shipping_label = d.pop("CbaDisplayableShippingLabel", UNSET)

        _order_type = d.pop("OrderType", UNSET)
        order_type: Union[Unset, OrderOrderType]
        if isinstance(_order_type, Unset):
            order_type = UNSET
        else:
            order_type = OrderOrderType(_order_type)

        earliest_ship_date = d.pop("EarliestShipDate", UNSET)

        latest_ship_date = d.pop("LatestShipDate", UNSET)

        earliest_delivery_date = d.pop("EarliestDeliveryDate", UNSET)

        latest_delivery_date = d.pop("LatestDeliveryDate", UNSET)

        is_business_order = d.pop("IsBusinessOrder", UNSET)

        is_prime = d.pop("IsPrime", UNSET)

        is_premium_order = d.pop("IsPremiumOrder", UNSET)

        is_global_express_enabled = d.pop("IsGlobalExpressEnabled", UNSET)

        replaced_order_id = d.pop("ReplacedOrderId", UNSET)

        is_replacement_order = d.pop("IsReplacementOrder", UNSET)

        promise_response_due_date = d.pop("PromiseResponseDueDate", UNSET)

        is_estimated_ship_date_set = d.pop("IsEstimatedShipDateSet", UNSET)

        is_sold_by_ab = d.pop("IsSoldByAB", UNSET)

        is_iba = d.pop("IsIBA", UNSET)

        _default_ship_from_location_address = d.pop("DefaultShipFromLocationAddress", UNSET)
        default_ship_from_location_address: Union[Unset, Address]
        if isinstance(_default_ship_from_location_address, Unset):
            default_ship_from_location_address = UNSET
        else:
            default_ship_from_location_address = Address.from_dict(_default_ship_from_location_address)

        _buyer_invoice_preference = d.pop("BuyerInvoicePreference", UNSET)
        buyer_invoice_preference: Union[Unset, OrderBuyerInvoicePreference]
        if isinstance(_buyer_invoice_preference, Unset):
            buyer_invoice_preference = UNSET
        else:
            buyer_invoice_preference = OrderBuyerInvoicePreference(_buyer_invoice_preference)

        _buyer_tax_information = d.pop("BuyerTaxInformation", UNSET)
        buyer_tax_information: Union[Unset, BuyerTaxInformation]
        if isinstance(_buyer_tax_information, Unset):
            buyer_tax_information = UNSET
        else:
            buyer_tax_information = BuyerTaxInformation.from_dict(_buyer_tax_information)

        _fulfillment_instruction = d.pop("FulfillmentInstruction", UNSET)
        fulfillment_instruction: Union[Unset, FulfillmentInstruction]
        if isinstance(_fulfillment_instruction, Unset):
            fulfillment_instruction = UNSET
        else:
            fulfillment_instruction = FulfillmentInstruction.from_dict(_fulfillment_instruction)

        is_ispu = d.pop("IsISPU", UNSET)

        is_access_point_order = d.pop("IsAccessPointOrder", UNSET)

        _marketplace_tax_info = d.pop("MarketplaceTaxInfo", UNSET)
        marketplace_tax_info: Union[Unset, MarketplaceTaxInfo]
        if isinstance(_marketplace_tax_info, Unset):
            marketplace_tax_info = UNSET
        else:
            marketplace_tax_info = MarketplaceTaxInfo.from_dict(_marketplace_tax_info)

        seller_display_name = d.pop("SellerDisplayName", UNSET)

        _shipping_address = d.pop("ShippingAddress", UNSET)
        shipping_address: Union[Unset, Address]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = Address.from_dict(_shipping_address)

        _buyer_info = d.pop("BuyerInfo", UNSET)
        buyer_info: Union[Unset, BuyerInfo]
        if isinstance(_buyer_info, Unset):
            buyer_info = UNSET
        else:
            buyer_info = BuyerInfo.from_dict(_buyer_info)

        _automated_shipping_settings = d.pop("AutomatedShippingSettings", UNSET)
        automated_shipping_settings: Union[Unset, AutomatedShippingSettings]
        if isinstance(_automated_shipping_settings, Unset):
            automated_shipping_settings = UNSET
        else:
            automated_shipping_settings = AutomatedShippingSettings.from_dict(_automated_shipping_settings)

        has_regulated_items = d.pop("HasRegulatedItems", UNSET)

        _electronic_invoice_status = d.pop("ElectronicInvoiceStatus", UNSET)
        electronic_invoice_status: Union[Unset, ElectronicInvoiceStatus]
        if isinstance(_electronic_invoice_status, Unset):
            electronic_invoice_status = UNSET
        else:
            electronic_invoice_status = ElectronicInvoiceStatus(_electronic_invoice_status)

        item_approval_types = []
        _item_approval_types = d.pop("ItemApprovalTypes", UNSET)
        for item_approval_types_item_data in _item_approval_types or []:
            item_approval_types_item = ItemApprovalType(item_approval_types_item_data)

            item_approval_types.append(item_approval_types_item)

        item_approval_status = []
        _item_approval_status = d.pop("ItemApprovalStatus", UNSET)
        for item_approval_status_item_data in _item_approval_status or []:
            item_approval_status_item = ItemApprovalStatus(item_approval_status_item_data)

            item_approval_status.append(item_approval_status_item)

        result = cls(
            amazon_order_id=amazon_order_id,
            purchase_date=purchase_date,
            last_update_date=last_update_date,
            order_status=order_status,
            seller_order_id=seller_order_id,
            fulfillment_channel=fulfillment_channel,
            sales_channel=sales_channel,
            order_channel=order_channel,
            ship_service_level=ship_service_level,
            order_total=order_total,
            number_of_items_shipped=number_of_items_shipped,
            number_of_items_unshipped=number_of_items_unshipped,
            payment_execution_detail=payment_execution_detail,
            payment_method=payment_method,
            payment_method_details=payment_method_details,
            marketplace_id=marketplace_id,
            shipment_service_level_category=shipment_service_level_category,
            easy_ship_shipment_status=easy_ship_shipment_status,
            cba_displayable_shipping_label=cba_displayable_shipping_label,
            order_type=order_type,
            earliest_ship_date=earliest_ship_date,
            latest_ship_date=latest_ship_date,
            earliest_delivery_date=earliest_delivery_date,
            latest_delivery_date=latest_delivery_date,
            is_business_order=is_business_order,
            is_prime=is_prime,
            is_premium_order=is_premium_order,
            is_global_express_enabled=is_global_express_enabled,
            replaced_order_id=replaced_order_id,
            is_replacement_order=is_replacement_order,
            promise_response_due_date=promise_response_due_date,
            is_estimated_ship_date_set=is_estimated_ship_date_set,
            is_sold_by_ab=is_sold_by_ab,
            is_iba=is_iba,
            default_ship_from_location_address=default_ship_from_location_address,
            buyer_invoice_preference=buyer_invoice_preference,
            buyer_tax_information=buyer_tax_information,
            fulfillment_instruction=fulfillment_instruction,
            is_ispu=is_ispu,
            is_access_point_order=is_access_point_order,
            marketplace_tax_info=marketplace_tax_info,
            seller_display_name=seller_display_name,
            shipping_address=shipping_address,
            buyer_info=buyer_info,
            automated_shipping_settings=automated_shipping_settings,
            has_regulated_items=has_regulated_items,
            electronic_invoice_status=electronic_invoice_status,
            item_approval_types=item_approval_types,
            item_approval_status=item_approval_status,
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
