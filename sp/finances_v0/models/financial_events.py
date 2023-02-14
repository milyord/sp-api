from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adhoc_disbursement_event import AdhocDisbursementEvent
    from ..models.adjustment_event import AdjustmentEvent
    from ..models.affordability_expense_event import AffordabilityExpenseEvent
    from ..models.capacity_reservation_billing_event import CapacityReservationBillingEvent
    from ..models.charge_refund_event import ChargeRefundEvent
    from ..models.coupon_payment_event import CouponPaymentEvent
    from ..models.debt_recovery_event import DebtRecoveryEvent
    from ..models.failed_adhoc_disbursement_event_list import FailedAdhocDisbursementEventList
    from ..models.fba_liquidation_event import FBALiquidationEvent
    from ..models.imaging_services_fee_event import ImagingServicesFeeEvent
    from ..models.loan_servicing_event import LoanServicingEvent
    from ..models.network_commingling_transaction_event import NetworkComminglingTransactionEvent
    from ..models.pay_with_amazon_event import PayWithAmazonEvent
    from ..models.product_ads_payment_event import ProductAdsPaymentEvent
    from ..models.removal_shipment_adjustment_event import RemovalShipmentAdjustmentEvent
    from ..models.removal_shipment_event import RemovalShipmentEvent
    from ..models.rental_transaction_event import RentalTransactionEvent
    from ..models.retrocharge_event import RetrochargeEvent
    from ..models.safet_reimbursement_event import SAFETReimbursementEvent
    from ..models.seller_deal_payment_event import SellerDealPaymentEvent
    from ..models.seller_review_enrollment_payment_event import SellerReviewEnrollmentPaymentEvent
    from ..models.service_fee_event import ServiceFeeEvent
    from ..models.shipment_event import ShipmentEvent
    from ..models.solution_provider_credit_event import SolutionProviderCreditEvent
    from ..models.tax_withholding_event import TaxWithholdingEvent
    from ..models.tds_reimbursement_event import TDSReimbursementEvent
    from ..models.trial_shipment_event import TrialShipmentEvent
    from ..models.value_added_service_charge_event_list import ValueAddedServiceChargeEventList


T = TypeVar("T", bound="FinancialEvents")


@attr.s(auto_attribs=True)
class FinancialEvents:
    r"""Contains all information related to a financial event.

    Attributes:
        shipment_event_list (Union[Unset, List['ShipmentEvent']]): A list of shipment event information.
        shipment_settle_event_list (Union[Unset, List['ShipmentEvent']]): A list of `ShipmentEvent` items.
        refund_event_list (Union[Unset, List['ShipmentEvent']]): A list of shipment event information.
        guarantee_claim_event_list (Union[Unset, List['ShipmentEvent']]): A list of shipment event information.
        chargeback_event_list (Union[Unset, List['ShipmentEvent']]): A list of shipment event information.
        pay_with_amazon_event_list (Union[Unset, List['PayWithAmazonEvent']]): A list of events related to the seller's
            Pay with Amazon account.
        service_provider_credit_event_list (Union[Unset, List['SolutionProviderCreditEvent']]): A list of information
            about solution provider credits.
        retrocharge_event_list (Union[Unset, List['RetrochargeEvent']]): A list of information about Retrocharge or
            RetrochargeReversal events.
        rental_transaction_event_list (Union[Unset, List['RentalTransactionEvent']]): A list of rental transaction event
            information.
        product_ads_payment_event_list (Union[Unset, List['ProductAdsPaymentEvent']]): A list of sponsored products
            payment events.
        service_fee_event_list (Union[Unset, List['ServiceFeeEvent']]): A list of information about service fee events.
        seller_deal_payment_event_list (Union[Unset, List['SellerDealPaymentEvent']]): A list of payment events for
            deal-related fees.
        debt_recovery_event_list (Union[Unset, List['DebtRecoveryEvent']]): A list of debt recovery event information.
        loan_servicing_event_list (Union[Unset, List['LoanServicingEvent']]): A list of loan servicing events.
        adjustment_event_list (Union[Unset, List['AdjustmentEvent']]): A list of adjustment event information for the
            seller's account.
        safet_reimbursement_event_list (Union[Unset, List['SAFETReimbursementEvent']]): A list of
            SAFETReimbursementEvents.
        seller_review_enrollment_payment_event_list (Union[Unset, List['SellerReviewEnrollmentPaymentEvent']]): A list
            of information about fee events for the Early Reviewer Program.
        fba_liquidation_event_list (Union[Unset, List['FBALiquidationEvent']]): A list of FBA inventory liquidation
            payment events.
        coupon_payment_event_list (Union[Unset, List['CouponPaymentEvent']]): A list of coupon payment event
            information.
        imaging_services_fee_event_list (Union[Unset, List['ImagingServicesFeeEvent']]): A list of fee events related to
            Amazon Imaging services.
        network_commingling_transaction_event_list (Union[Unset, List['NetworkComminglingTransactionEvent']]): A list of
            network commingling transaction events.
        affordability_expense_event_list (Union[Unset, List['AffordabilityExpenseEvent']]): A list of expense
            information related to an affordability promotion.
        affordability_expense_reversal_event_list (Union[Unset, List['AffordabilityExpenseEvent']]): A list of expense
            information related to an affordability promotion.
        removal_shipment_event_list (Union[Unset, List['RemovalShipmentEvent']]): A list of removal shipment event
            information.
        removal_shipment_adjustment_event_list (Union[Unset, List['RemovalShipmentAdjustmentEvent']]): A comma-delimited
            list of Removal shipmentAdjustment details for FBA inventory.
        trial_shipment_event_list (Union[Unset, List['TrialShipmentEvent']]): A list of information about trial shipment
            financial events.
        tds_reimbursement_event_list (Union[Unset, List['TDSReimbursementEvent']]): A list of `TDSReimbursementEvent`
            items.
        adhoc_disbursement_event_list (Union[Unset, List['AdhocDisbursementEvent']]): A list of `AdhocDisbursement`
            events.
        tax_withholding_event_list (Union[Unset, List['TaxWithholdingEvent']]): A list of `TaxWithholding` events.
        charge_refund_event_list (Union[Unset, List['ChargeRefundEvent']]): A list of charge refund events.
        failed_adhoc_disbursement_event_list (Union[Unset, FailedAdhocDisbursementEventList]): Failed ad hoc
            disbursement event list.
        value_added_service_charge_event_list (Union[Unset, ValueAddedServiceChargeEventList]): An event related to a
            value added service charge.
        capacity_reservation_billing_event_list (Union[Unset, List['CapacityReservationBillingEvent']]): A list of
            `CapacityReservationBillingEvent` events.
    """

    shipment_event_list: Union[Unset, List["ShipmentEvent"]] = UNSET
    shipment_settle_event_list: Union[Unset, List["ShipmentEvent"]] = UNSET
    refund_event_list: Union[Unset, List["ShipmentEvent"]] = UNSET
    guarantee_claim_event_list: Union[Unset, List["ShipmentEvent"]] = UNSET
    chargeback_event_list: Union[Unset, List["ShipmentEvent"]] = UNSET
    pay_with_amazon_event_list: Union[Unset, List["PayWithAmazonEvent"]] = UNSET
    service_provider_credit_event_list: Union[Unset, List["SolutionProviderCreditEvent"]] = UNSET
    retrocharge_event_list: Union[Unset, List["RetrochargeEvent"]] = UNSET
    rental_transaction_event_list: Union[Unset, List["RentalTransactionEvent"]] = UNSET
    product_ads_payment_event_list: Union[Unset, List["ProductAdsPaymentEvent"]] = UNSET
    service_fee_event_list: Union[Unset, List["ServiceFeeEvent"]] = UNSET
    seller_deal_payment_event_list: Union[Unset, List["SellerDealPaymentEvent"]] = UNSET
    debt_recovery_event_list: Union[Unset, List["DebtRecoveryEvent"]] = UNSET
    loan_servicing_event_list: Union[Unset, List["LoanServicingEvent"]] = UNSET
    adjustment_event_list: Union[Unset, List["AdjustmentEvent"]] = UNSET
    safet_reimbursement_event_list: Union[Unset, List["SAFETReimbursementEvent"]] = UNSET
    seller_review_enrollment_payment_event_list: Union[Unset, List["SellerReviewEnrollmentPaymentEvent"]] = UNSET
    fba_liquidation_event_list: Union[Unset, List["FBALiquidationEvent"]] = UNSET
    coupon_payment_event_list: Union[Unset, List["CouponPaymentEvent"]] = UNSET
    imaging_services_fee_event_list: Union[Unset, List["ImagingServicesFeeEvent"]] = UNSET
    network_commingling_transaction_event_list: Union[Unset, List["NetworkComminglingTransactionEvent"]] = UNSET
    affordability_expense_event_list: Union[Unset, List["AffordabilityExpenseEvent"]] = UNSET
    affordability_expense_reversal_event_list: Union[Unset, List["AffordabilityExpenseEvent"]] = UNSET
    removal_shipment_event_list: Union[Unset, List["RemovalShipmentEvent"]] = UNSET
    removal_shipment_adjustment_event_list: Union[Unset, List["RemovalShipmentAdjustmentEvent"]] = UNSET
    trial_shipment_event_list: Union[Unset, List["TrialShipmentEvent"]] = UNSET
    tds_reimbursement_event_list: Union[Unset, List["TDSReimbursementEvent"]] = UNSET
    adhoc_disbursement_event_list: Union[Unset, List["AdhocDisbursementEvent"]] = UNSET
    tax_withholding_event_list: Union[Unset, List["TaxWithholdingEvent"]] = UNSET
    charge_refund_event_list: Union[Unset, List["ChargeRefundEvent"]] = UNSET
    failed_adhoc_disbursement_event_list: Union[Unset, "FailedAdhocDisbursementEventList"] = UNSET
    value_added_service_charge_event_list: Union[Unset, "ValueAddedServiceChargeEventList"] = UNSET
    capacity_reservation_billing_event_list: Union[Unset, List["CapacityReservationBillingEvent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_event_list, Unset):
            shipment_event_list = []
            for componentsschemas_shipment_event_list_item_data in self.shipment_event_list:
                componentsschemas_shipment_event_list_item = componentsschemas_shipment_event_list_item_data.to_dict()

                shipment_event_list.append(componentsschemas_shipment_event_list_item)

        shipment_settle_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_settle_event_list, Unset):
            shipment_settle_event_list = []
            for componentsschemas_shipment_settle_event_list_item_data in self.shipment_settle_event_list:
                componentsschemas_shipment_settle_event_list_item = (
                    componentsschemas_shipment_settle_event_list_item_data.to_dict()
                )

                shipment_settle_event_list.append(componentsschemas_shipment_settle_event_list_item)

        refund_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.refund_event_list, Unset):
            refund_event_list = []
            for componentsschemas_shipment_event_list_item_data in self.refund_event_list:
                componentsschemas_shipment_event_list_item = componentsschemas_shipment_event_list_item_data.to_dict()

                refund_event_list.append(componentsschemas_shipment_event_list_item)

        guarantee_claim_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.guarantee_claim_event_list, Unset):
            guarantee_claim_event_list = []
            for componentsschemas_shipment_event_list_item_data in self.guarantee_claim_event_list:
                componentsschemas_shipment_event_list_item = componentsschemas_shipment_event_list_item_data.to_dict()

                guarantee_claim_event_list.append(componentsschemas_shipment_event_list_item)

        chargeback_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.chargeback_event_list, Unset):
            chargeback_event_list = []
            for componentsschemas_shipment_event_list_item_data in self.chargeback_event_list:
                componentsschemas_shipment_event_list_item = componentsschemas_shipment_event_list_item_data.to_dict()

                chargeback_event_list.append(componentsschemas_shipment_event_list_item)

        pay_with_amazon_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pay_with_amazon_event_list, Unset):
            pay_with_amazon_event_list = []
            for componentsschemas_pay_with_amazon_event_list_item_data in self.pay_with_amazon_event_list:
                componentsschemas_pay_with_amazon_event_list_item = (
                    componentsschemas_pay_with_amazon_event_list_item_data.to_dict()
                )

                pay_with_amazon_event_list.append(componentsschemas_pay_with_amazon_event_list_item)

        service_provider_credit_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.service_provider_credit_event_list, Unset):
            service_provider_credit_event_list = []
            for (
                componentsschemas_solution_provider_credit_event_list_item_data
            ) in self.service_provider_credit_event_list:
                componentsschemas_solution_provider_credit_event_list_item = (
                    componentsschemas_solution_provider_credit_event_list_item_data.to_dict()
                )

                service_provider_credit_event_list.append(componentsschemas_solution_provider_credit_event_list_item)

        retrocharge_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.retrocharge_event_list, Unset):
            retrocharge_event_list = []
            for componentsschemas_retrocharge_event_list_item_data in self.retrocharge_event_list:
                componentsschemas_retrocharge_event_list_item = (
                    componentsschemas_retrocharge_event_list_item_data.to_dict()
                )

                retrocharge_event_list.append(componentsschemas_retrocharge_event_list_item)

        rental_transaction_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rental_transaction_event_list, Unset):
            rental_transaction_event_list = []
            for componentsschemas_rental_transaction_event_list_item_data in self.rental_transaction_event_list:
                componentsschemas_rental_transaction_event_list_item = (
                    componentsschemas_rental_transaction_event_list_item_data.to_dict()
                )

                rental_transaction_event_list.append(componentsschemas_rental_transaction_event_list_item)

        product_ads_payment_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_ads_payment_event_list, Unset):
            product_ads_payment_event_list = []
            for componentsschemas_product_ads_payment_event_list_item_data in self.product_ads_payment_event_list:
                componentsschemas_product_ads_payment_event_list_item = (
                    componentsschemas_product_ads_payment_event_list_item_data.to_dict()
                )

                product_ads_payment_event_list.append(componentsschemas_product_ads_payment_event_list_item)

        service_fee_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.service_fee_event_list, Unset):
            service_fee_event_list = []
            for componentsschemas_service_fee_event_list_item_data in self.service_fee_event_list:
                componentsschemas_service_fee_event_list_item = (
                    componentsschemas_service_fee_event_list_item_data.to_dict()
                )

                service_fee_event_list.append(componentsschemas_service_fee_event_list_item)

        seller_deal_payment_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.seller_deal_payment_event_list, Unset):
            seller_deal_payment_event_list = []
            for componentsschemas_seller_deal_payment_event_list_item_data in self.seller_deal_payment_event_list:
                componentsschemas_seller_deal_payment_event_list_item = (
                    componentsschemas_seller_deal_payment_event_list_item_data.to_dict()
                )

                seller_deal_payment_event_list.append(componentsschemas_seller_deal_payment_event_list_item)

        debt_recovery_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.debt_recovery_event_list, Unset):
            debt_recovery_event_list = []
            for componentsschemas_debt_recovery_event_list_item_data in self.debt_recovery_event_list:
                componentsschemas_debt_recovery_event_list_item = (
                    componentsschemas_debt_recovery_event_list_item_data.to_dict()
                )

                debt_recovery_event_list.append(componentsschemas_debt_recovery_event_list_item)

        loan_servicing_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.loan_servicing_event_list, Unset):
            loan_servicing_event_list = []
            for componentsschemas_loan_servicing_event_list_item_data in self.loan_servicing_event_list:
                componentsschemas_loan_servicing_event_list_item = (
                    componentsschemas_loan_servicing_event_list_item_data.to_dict()
                )

                loan_servicing_event_list.append(componentsschemas_loan_servicing_event_list_item)

        adjustment_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.adjustment_event_list, Unset):
            adjustment_event_list = []
            for componentsschemas_adjustment_event_list_item_data in self.adjustment_event_list:
                componentsschemas_adjustment_event_list_item = (
                    componentsschemas_adjustment_event_list_item_data.to_dict()
                )

                adjustment_event_list.append(componentsschemas_adjustment_event_list_item)

        safet_reimbursement_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.safet_reimbursement_event_list, Unset):
            safet_reimbursement_event_list = []
            for componentsschemas_safet_reimbursement_event_list_item_data in self.safet_reimbursement_event_list:
                componentsschemas_safet_reimbursement_event_list_item = (
                    componentsschemas_safet_reimbursement_event_list_item_data.to_dict()
                )

                safet_reimbursement_event_list.append(componentsschemas_safet_reimbursement_event_list_item)

        seller_review_enrollment_payment_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.seller_review_enrollment_payment_event_list, Unset):
            seller_review_enrollment_payment_event_list = []
            for (
                componentsschemas_seller_review_enrollment_payment_event_list_item_data
            ) in self.seller_review_enrollment_payment_event_list:
                componentsschemas_seller_review_enrollment_payment_event_list_item = (
                    componentsschemas_seller_review_enrollment_payment_event_list_item_data.to_dict()
                )

                seller_review_enrollment_payment_event_list.append(
                    componentsschemas_seller_review_enrollment_payment_event_list_item
                )

        fba_liquidation_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fba_liquidation_event_list, Unset):
            fba_liquidation_event_list = []
            for componentsschemas_fba_liquidation_event_list_item_data in self.fba_liquidation_event_list:
                componentsschemas_fba_liquidation_event_list_item = (
                    componentsschemas_fba_liquidation_event_list_item_data.to_dict()
                )

                fba_liquidation_event_list.append(componentsschemas_fba_liquidation_event_list_item)

        coupon_payment_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.coupon_payment_event_list, Unset):
            coupon_payment_event_list = []
            for componentsschemas_coupon_payment_event_list_item_data in self.coupon_payment_event_list:
                componentsschemas_coupon_payment_event_list_item = (
                    componentsschemas_coupon_payment_event_list_item_data.to_dict()
                )

                coupon_payment_event_list.append(componentsschemas_coupon_payment_event_list_item)

        imaging_services_fee_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.imaging_services_fee_event_list, Unset):
            imaging_services_fee_event_list = []
            for componentsschemas_imaging_services_fee_event_list_item_data in self.imaging_services_fee_event_list:
                componentsschemas_imaging_services_fee_event_list_item = (
                    componentsschemas_imaging_services_fee_event_list_item_data.to_dict()
                )

                imaging_services_fee_event_list.append(componentsschemas_imaging_services_fee_event_list_item)

        network_commingling_transaction_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.network_commingling_transaction_event_list, Unset):
            network_commingling_transaction_event_list = []
            for (
                componentsschemas_network_commingling_transaction_event_list_item_data
            ) in self.network_commingling_transaction_event_list:
                componentsschemas_network_commingling_transaction_event_list_item = (
                    componentsschemas_network_commingling_transaction_event_list_item_data.to_dict()
                )

                network_commingling_transaction_event_list.append(
                    componentsschemas_network_commingling_transaction_event_list_item
                )

        affordability_expense_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.affordability_expense_event_list, Unset):
            affordability_expense_event_list = []
            for componentsschemas_affordability_expense_event_list_item_data in self.affordability_expense_event_list:
                componentsschemas_affordability_expense_event_list_item = (
                    componentsschemas_affordability_expense_event_list_item_data.to_dict()
                )

                affordability_expense_event_list.append(componentsschemas_affordability_expense_event_list_item)

        affordability_expense_reversal_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.affordability_expense_reversal_event_list, Unset):
            affordability_expense_reversal_event_list = []
            for (
                componentsschemas_affordability_expense_event_list_item_data
            ) in self.affordability_expense_reversal_event_list:
                componentsschemas_affordability_expense_event_list_item = (
                    componentsschemas_affordability_expense_event_list_item_data.to_dict()
                )

                affordability_expense_reversal_event_list.append(
                    componentsschemas_affordability_expense_event_list_item
                )

        removal_shipment_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.removal_shipment_event_list, Unset):
            removal_shipment_event_list = []
            for componentsschemas_removal_shipment_event_list_item_data in self.removal_shipment_event_list:
                componentsschemas_removal_shipment_event_list_item = (
                    componentsschemas_removal_shipment_event_list_item_data.to_dict()
                )

                removal_shipment_event_list.append(componentsschemas_removal_shipment_event_list_item)

        removal_shipment_adjustment_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.removal_shipment_adjustment_event_list, Unset):
            removal_shipment_adjustment_event_list = []
            for (
                componentsschemas_removal_shipment_adjustment_event_list_item_data
            ) in self.removal_shipment_adjustment_event_list:
                componentsschemas_removal_shipment_adjustment_event_list_item = (
                    componentsschemas_removal_shipment_adjustment_event_list_item_data.to_dict()
                )

                removal_shipment_adjustment_event_list.append(
                    componentsschemas_removal_shipment_adjustment_event_list_item
                )

        trial_shipment_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.trial_shipment_event_list, Unset):
            trial_shipment_event_list = []
            for componentsschemas_trial_shipment_event_list_item_data in self.trial_shipment_event_list:
                componentsschemas_trial_shipment_event_list_item = (
                    componentsschemas_trial_shipment_event_list_item_data.to_dict()
                )

                trial_shipment_event_list.append(componentsschemas_trial_shipment_event_list_item)

        tds_reimbursement_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tds_reimbursement_event_list, Unset):
            tds_reimbursement_event_list = []
            for componentsschemas_tds_reimbursement_event_list_item_data in self.tds_reimbursement_event_list:
                componentsschemas_tds_reimbursement_event_list_item = (
                    componentsschemas_tds_reimbursement_event_list_item_data.to_dict()
                )

                tds_reimbursement_event_list.append(componentsschemas_tds_reimbursement_event_list_item)

        adhoc_disbursement_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.adhoc_disbursement_event_list, Unset):
            adhoc_disbursement_event_list = []
            for componentsschemas_adhoc_disbursement_event_list_item_data in self.adhoc_disbursement_event_list:
                componentsschemas_adhoc_disbursement_event_list_item = (
                    componentsschemas_adhoc_disbursement_event_list_item_data.to_dict()
                )

                adhoc_disbursement_event_list.append(componentsschemas_adhoc_disbursement_event_list_item)

        tax_withholding_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_withholding_event_list, Unset):
            tax_withholding_event_list = []
            for componentsschemas_tax_withholding_event_list_item_data in self.tax_withholding_event_list:
                componentsschemas_tax_withholding_event_list_item = (
                    componentsschemas_tax_withholding_event_list_item_data.to_dict()
                )

                tax_withholding_event_list.append(componentsschemas_tax_withholding_event_list_item)

        charge_refund_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.charge_refund_event_list, Unset):
            charge_refund_event_list = []
            for componentsschemas_charge_refund_event_list_item_data in self.charge_refund_event_list:
                componentsschemas_charge_refund_event_list_item = (
                    componentsschemas_charge_refund_event_list_item_data.to_dict()
                )

                charge_refund_event_list.append(componentsschemas_charge_refund_event_list_item)

        failed_adhoc_disbursement_event_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.failed_adhoc_disbursement_event_list, Unset):
            failed_adhoc_disbursement_event_list = self.failed_adhoc_disbursement_event_list.to_dict()

        value_added_service_charge_event_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_added_service_charge_event_list, Unset):
            value_added_service_charge_event_list = self.value_added_service_charge_event_list.to_dict()

        capacity_reservation_billing_event_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.capacity_reservation_billing_event_list, Unset):
            capacity_reservation_billing_event_list = []
            for (
                componentsschemas_capacity_reservation_billing_event_list_item_data
            ) in self.capacity_reservation_billing_event_list:
                componentsschemas_capacity_reservation_billing_event_list_item = (
                    componentsschemas_capacity_reservation_billing_event_list_item_data.to_dict()
                )

                capacity_reservation_billing_event_list.append(
                    componentsschemas_capacity_reservation_billing_event_list_item
                )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment_event_list is not UNSET:
            field_dict["ShipmentEventList"] = shipment_event_list
        if shipment_settle_event_list is not UNSET:
            field_dict["ShipmentSettleEventList"] = shipment_settle_event_list
        if refund_event_list is not UNSET:
            field_dict["RefundEventList"] = refund_event_list
        if guarantee_claim_event_list is not UNSET:
            field_dict["GuaranteeClaimEventList"] = guarantee_claim_event_list
        if chargeback_event_list is not UNSET:
            field_dict["ChargebackEventList"] = chargeback_event_list
        if pay_with_amazon_event_list is not UNSET:
            field_dict["PayWithAmazonEventList"] = pay_with_amazon_event_list
        if service_provider_credit_event_list is not UNSET:
            field_dict["ServiceProviderCreditEventList"] = service_provider_credit_event_list
        if retrocharge_event_list is not UNSET:
            field_dict["RetrochargeEventList"] = retrocharge_event_list
        if rental_transaction_event_list is not UNSET:
            field_dict["RentalTransactionEventList"] = rental_transaction_event_list
        if product_ads_payment_event_list is not UNSET:
            field_dict["ProductAdsPaymentEventList"] = product_ads_payment_event_list
        if service_fee_event_list is not UNSET:
            field_dict["ServiceFeeEventList"] = service_fee_event_list
        if seller_deal_payment_event_list is not UNSET:
            field_dict["SellerDealPaymentEventList"] = seller_deal_payment_event_list
        if debt_recovery_event_list is not UNSET:
            field_dict["DebtRecoveryEventList"] = debt_recovery_event_list
        if loan_servicing_event_list is not UNSET:
            field_dict["LoanServicingEventList"] = loan_servicing_event_list
        if adjustment_event_list is not UNSET:
            field_dict["AdjustmentEventList"] = adjustment_event_list
        if safet_reimbursement_event_list is not UNSET:
            field_dict["SAFETReimbursementEventList"] = safet_reimbursement_event_list
        if seller_review_enrollment_payment_event_list is not UNSET:
            field_dict["SellerReviewEnrollmentPaymentEventList"] = seller_review_enrollment_payment_event_list
        if fba_liquidation_event_list is not UNSET:
            field_dict["FBALiquidationEventList"] = fba_liquidation_event_list
        if coupon_payment_event_list is not UNSET:
            field_dict["CouponPaymentEventList"] = coupon_payment_event_list
        if imaging_services_fee_event_list is not UNSET:
            field_dict["ImagingServicesFeeEventList"] = imaging_services_fee_event_list
        if network_commingling_transaction_event_list is not UNSET:
            field_dict["NetworkComminglingTransactionEventList"] = network_commingling_transaction_event_list
        if affordability_expense_event_list is not UNSET:
            field_dict["AffordabilityExpenseEventList"] = affordability_expense_event_list
        if affordability_expense_reversal_event_list is not UNSET:
            field_dict["AffordabilityExpenseReversalEventList"] = affordability_expense_reversal_event_list
        if removal_shipment_event_list is not UNSET:
            field_dict["RemovalShipmentEventList"] = removal_shipment_event_list
        if removal_shipment_adjustment_event_list is not UNSET:
            field_dict["RemovalShipmentAdjustmentEventList"] = removal_shipment_adjustment_event_list
        if trial_shipment_event_list is not UNSET:
            field_dict["TrialShipmentEventList"] = trial_shipment_event_list
        if tds_reimbursement_event_list is not UNSET:
            field_dict["TDSReimbursementEventList"] = tds_reimbursement_event_list
        if adhoc_disbursement_event_list is not UNSET:
            field_dict["AdhocDisbursementEventList"] = adhoc_disbursement_event_list
        if tax_withholding_event_list is not UNSET:
            field_dict["TaxWithholdingEventList"] = tax_withholding_event_list
        if charge_refund_event_list is not UNSET:
            field_dict["ChargeRefundEventList"] = charge_refund_event_list
        if failed_adhoc_disbursement_event_list is not UNSET:
            field_dict["FailedAdhocDisbursementEventList"] = failed_adhoc_disbursement_event_list
        if value_added_service_charge_event_list is not UNSET:
            field_dict["ValueAddedServiceChargeEventList"] = value_added_service_charge_event_list
        if capacity_reservation_billing_event_list is not UNSET:
            field_dict["CapacityReservationBillingEventList"] = capacity_reservation_billing_event_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adhoc_disbursement_event import AdhocDisbursementEvent
        from ..models.adjustment_event import AdjustmentEvent
        from ..models.affordability_expense_event import AffordabilityExpenseEvent
        from ..models.capacity_reservation_billing_event import CapacityReservationBillingEvent
        from ..models.charge_refund_event import ChargeRefundEvent
        from ..models.coupon_payment_event import CouponPaymentEvent
        from ..models.debt_recovery_event import DebtRecoveryEvent
        from ..models.failed_adhoc_disbursement_event_list import FailedAdhocDisbursementEventList
        from ..models.fba_liquidation_event import FBALiquidationEvent
        from ..models.imaging_services_fee_event import ImagingServicesFeeEvent
        from ..models.loan_servicing_event import LoanServicingEvent
        from ..models.network_commingling_transaction_event import NetworkComminglingTransactionEvent
        from ..models.pay_with_amazon_event import PayWithAmazonEvent
        from ..models.product_ads_payment_event import ProductAdsPaymentEvent
        from ..models.removal_shipment_adjustment_event import RemovalShipmentAdjustmentEvent
        from ..models.removal_shipment_event import RemovalShipmentEvent
        from ..models.rental_transaction_event import RentalTransactionEvent
        from ..models.retrocharge_event import RetrochargeEvent
        from ..models.safet_reimbursement_event import SAFETReimbursementEvent
        from ..models.seller_deal_payment_event import SellerDealPaymentEvent
        from ..models.seller_review_enrollment_payment_event import SellerReviewEnrollmentPaymentEvent
        from ..models.service_fee_event import ServiceFeeEvent
        from ..models.shipment_event import ShipmentEvent
        from ..models.solution_provider_credit_event import SolutionProviderCreditEvent
        from ..models.tax_withholding_event import TaxWithholdingEvent
        from ..models.tds_reimbursement_event import TDSReimbursementEvent
        from ..models.trial_shipment_event import TrialShipmentEvent
        from ..models.value_added_service_charge_event_list import ValueAddedServiceChargeEventList

        d = src_dict.copy()
        shipment_event_list = []
        _shipment_event_list = d.pop("ShipmentEventList", UNSET)
        for componentsschemas_shipment_event_list_item_data in _shipment_event_list or []:
            componentsschemas_shipment_event_list_item = ShipmentEvent.from_dict(
                componentsschemas_shipment_event_list_item_data
            )

            shipment_event_list.append(componentsschemas_shipment_event_list_item)

        shipment_settle_event_list = []
        _shipment_settle_event_list = d.pop("ShipmentSettleEventList", UNSET)
        for componentsschemas_shipment_settle_event_list_item_data in _shipment_settle_event_list or []:
            componentsschemas_shipment_settle_event_list_item = ShipmentEvent.from_dict(
                componentsschemas_shipment_settle_event_list_item_data
            )

            shipment_settle_event_list.append(componentsschemas_shipment_settle_event_list_item)

        refund_event_list = []
        _refund_event_list = d.pop("RefundEventList", UNSET)
        for componentsschemas_shipment_event_list_item_data in _refund_event_list or []:
            componentsschemas_shipment_event_list_item = ShipmentEvent.from_dict(
                componentsschemas_shipment_event_list_item_data
            )

            refund_event_list.append(componentsschemas_shipment_event_list_item)

        guarantee_claim_event_list = []
        _guarantee_claim_event_list = d.pop("GuaranteeClaimEventList", UNSET)
        for componentsschemas_shipment_event_list_item_data in _guarantee_claim_event_list or []:
            componentsschemas_shipment_event_list_item = ShipmentEvent.from_dict(
                componentsschemas_shipment_event_list_item_data
            )

            guarantee_claim_event_list.append(componentsschemas_shipment_event_list_item)

        chargeback_event_list = []
        _chargeback_event_list = d.pop("ChargebackEventList", UNSET)
        for componentsschemas_shipment_event_list_item_data in _chargeback_event_list or []:
            componentsschemas_shipment_event_list_item = ShipmentEvent.from_dict(
                componentsschemas_shipment_event_list_item_data
            )

            chargeback_event_list.append(componentsschemas_shipment_event_list_item)

        pay_with_amazon_event_list = []
        _pay_with_amazon_event_list = d.pop("PayWithAmazonEventList", UNSET)
        for componentsschemas_pay_with_amazon_event_list_item_data in _pay_with_amazon_event_list or []:
            componentsschemas_pay_with_amazon_event_list_item = PayWithAmazonEvent.from_dict(
                componentsschemas_pay_with_amazon_event_list_item_data
            )

            pay_with_amazon_event_list.append(componentsschemas_pay_with_amazon_event_list_item)

        service_provider_credit_event_list = []
        _service_provider_credit_event_list = d.pop("ServiceProviderCreditEventList", UNSET)
        for componentsschemas_solution_provider_credit_event_list_item_data in (
            _service_provider_credit_event_list or []
        ):
            componentsschemas_solution_provider_credit_event_list_item = SolutionProviderCreditEvent.from_dict(
                componentsschemas_solution_provider_credit_event_list_item_data
            )

            service_provider_credit_event_list.append(componentsschemas_solution_provider_credit_event_list_item)

        retrocharge_event_list = []
        _retrocharge_event_list = d.pop("RetrochargeEventList", UNSET)
        for componentsschemas_retrocharge_event_list_item_data in _retrocharge_event_list or []:
            componentsschemas_retrocharge_event_list_item = RetrochargeEvent.from_dict(
                componentsschemas_retrocharge_event_list_item_data
            )

            retrocharge_event_list.append(componentsschemas_retrocharge_event_list_item)

        rental_transaction_event_list = []
        _rental_transaction_event_list = d.pop("RentalTransactionEventList", UNSET)
        for componentsschemas_rental_transaction_event_list_item_data in _rental_transaction_event_list or []:
            componentsschemas_rental_transaction_event_list_item = RentalTransactionEvent.from_dict(
                componentsschemas_rental_transaction_event_list_item_data
            )

            rental_transaction_event_list.append(componentsschemas_rental_transaction_event_list_item)

        product_ads_payment_event_list = []
        _product_ads_payment_event_list = d.pop("ProductAdsPaymentEventList", UNSET)
        for componentsschemas_product_ads_payment_event_list_item_data in _product_ads_payment_event_list or []:
            componentsschemas_product_ads_payment_event_list_item = ProductAdsPaymentEvent.from_dict(
                componentsschemas_product_ads_payment_event_list_item_data
            )

            product_ads_payment_event_list.append(componentsschemas_product_ads_payment_event_list_item)

        service_fee_event_list = []
        _service_fee_event_list = d.pop("ServiceFeeEventList", UNSET)
        for componentsschemas_service_fee_event_list_item_data in _service_fee_event_list or []:
            componentsschemas_service_fee_event_list_item = ServiceFeeEvent.from_dict(
                componentsschemas_service_fee_event_list_item_data
            )

            service_fee_event_list.append(componentsschemas_service_fee_event_list_item)

        seller_deal_payment_event_list = []
        _seller_deal_payment_event_list = d.pop("SellerDealPaymentEventList", UNSET)
        for componentsschemas_seller_deal_payment_event_list_item_data in _seller_deal_payment_event_list or []:
            componentsschemas_seller_deal_payment_event_list_item = SellerDealPaymentEvent.from_dict(
                componentsschemas_seller_deal_payment_event_list_item_data
            )

            seller_deal_payment_event_list.append(componentsschemas_seller_deal_payment_event_list_item)

        debt_recovery_event_list = []
        _debt_recovery_event_list = d.pop("DebtRecoveryEventList", UNSET)
        for componentsschemas_debt_recovery_event_list_item_data in _debt_recovery_event_list or []:
            componentsschemas_debt_recovery_event_list_item = DebtRecoveryEvent.from_dict(
                componentsschemas_debt_recovery_event_list_item_data
            )

            debt_recovery_event_list.append(componentsschemas_debt_recovery_event_list_item)

        loan_servicing_event_list = []
        _loan_servicing_event_list = d.pop("LoanServicingEventList", UNSET)
        for componentsschemas_loan_servicing_event_list_item_data in _loan_servicing_event_list or []:
            componentsschemas_loan_servicing_event_list_item = LoanServicingEvent.from_dict(
                componentsschemas_loan_servicing_event_list_item_data
            )

            loan_servicing_event_list.append(componentsschemas_loan_servicing_event_list_item)

        adjustment_event_list = []
        _adjustment_event_list = d.pop("AdjustmentEventList", UNSET)
        for componentsschemas_adjustment_event_list_item_data in _adjustment_event_list or []:
            componentsschemas_adjustment_event_list_item = AdjustmentEvent.from_dict(
                componentsschemas_adjustment_event_list_item_data
            )

            adjustment_event_list.append(componentsschemas_adjustment_event_list_item)

        safet_reimbursement_event_list = []
        _safet_reimbursement_event_list = d.pop("SAFETReimbursementEventList", UNSET)
        for componentsschemas_safet_reimbursement_event_list_item_data in _safet_reimbursement_event_list or []:
            componentsschemas_safet_reimbursement_event_list_item = SAFETReimbursementEvent.from_dict(
                componentsschemas_safet_reimbursement_event_list_item_data
            )

            safet_reimbursement_event_list.append(componentsschemas_safet_reimbursement_event_list_item)

        seller_review_enrollment_payment_event_list = []
        _seller_review_enrollment_payment_event_list = d.pop("SellerReviewEnrollmentPaymentEventList", UNSET)
        for componentsschemas_seller_review_enrollment_payment_event_list_item_data in (
            _seller_review_enrollment_payment_event_list or []
        ):
            componentsschemas_seller_review_enrollment_payment_event_list_item = (
                SellerReviewEnrollmentPaymentEvent.from_dict(
                    componentsschemas_seller_review_enrollment_payment_event_list_item_data
                )
            )

            seller_review_enrollment_payment_event_list.append(
                componentsschemas_seller_review_enrollment_payment_event_list_item
            )

        fba_liquidation_event_list = []
        _fba_liquidation_event_list = d.pop("FBALiquidationEventList", UNSET)
        for componentsschemas_fba_liquidation_event_list_item_data in _fba_liquidation_event_list or []:
            componentsschemas_fba_liquidation_event_list_item = FBALiquidationEvent.from_dict(
                componentsschemas_fba_liquidation_event_list_item_data
            )

            fba_liquidation_event_list.append(componentsschemas_fba_liquidation_event_list_item)

        coupon_payment_event_list = []
        _coupon_payment_event_list = d.pop("CouponPaymentEventList", UNSET)
        for componentsschemas_coupon_payment_event_list_item_data in _coupon_payment_event_list or []:
            componentsschemas_coupon_payment_event_list_item = CouponPaymentEvent.from_dict(
                componentsschemas_coupon_payment_event_list_item_data
            )

            coupon_payment_event_list.append(componentsschemas_coupon_payment_event_list_item)

        imaging_services_fee_event_list = []
        _imaging_services_fee_event_list = d.pop("ImagingServicesFeeEventList", UNSET)
        for componentsschemas_imaging_services_fee_event_list_item_data in _imaging_services_fee_event_list or []:
            componentsschemas_imaging_services_fee_event_list_item = ImagingServicesFeeEvent.from_dict(
                componentsschemas_imaging_services_fee_event_list_item_data
            )

            imaging_services_fee_event_list.append(componentsschemas_imaging_services_fee_event_list_item)

        network_commingling_transaction_event_list = []
        _network_commingling_transaction_event_list = d.pop("NetworkComminglingTransactionEventList", UNSET)
        for componentsschemas_network_commingling_transaction_event_list_item_data in (
            _network_commingling_transaction_event_list or []
        ):
            componentsschemas_network_commingling_transaction_event_list_item = (
                NetworkComminglingTransactionEvent.from_dict(
                    componentsschemas_network_commingling_transaction_event_list_item_data
                )
            )

            network_commingling_transaction_event_list.append(
                componentsschemas_network_commingling_transaction_event_list_item
            )

        affordability_expense_event_list = []
        _affordability_expense_event_list = d.pop("AffordabilityExpenseEventList", UNSET)
        for componentsschemas_affordability_expense_event_list_item_data in _affordability_expense_event_list or []:
            componentsschemas_affordability_expense_event_list_item = AffordabilityExpenseEvent.from_dict(
                componentsschemas_affordability_expense_event_list_item_data
            )

            affordability_expense_event_list.append(componentsschemas_affordability_expense_event_list_item)

        affordability_expense_reversal_event_list = []
        _affordability_expense_reversal_event_list = d.pop("AffordabilityExpenseReversalEventList", UNSET)
        for componentsschemas_affordability_expense_event_list_item_data in (
            _affordability_expense_reversal_event_list or []
        ):
            componentsschemas_affordability_expense_event_list_item = AffordabilityExpenseEvent.from_dict(
                componentsschemas_affordability_expense_event_list_item_data
            )

            affordability_expense_reversal_event_list.append(componentsschemas_affordability_expense_event_list_item)

        removal_shipment_event_list = []
        _removal_shipment_event_list = d.pop("RemovalShipmentEventList", UNSET)
        for componentsschemas_removal_shipment_event_list_item_data in _removal_shipment_event_list or []:
            componentsschemas_removal_shipment_event_list_item = RemovalShipmentEvent.from_dict(
                componentsschemas_removal_shipment_event_list_item_data
            )

            removal_shipment_event_list.append(componentsschemas_removal_shipment_event_list_item)

        removal_shipment_adjustment_event_list = []
        _removal_shipment_adjustment_event_list = d.pop("RemovalShipmentAdjustmentEventList", UNSET)
        for componentsschemas_removal_shipment_adjustment_event_list_item_data in (
            _removal_shipment_adjustment_event_list or []
        ):
            componentsschemas_removal_shipment_adjustment_event_list_item = RemovalShipmentAdjustmentEvent.from_dict(
                componentsschemas_removal_shipment_adjustment_event_list_item_data
            )

            removal_shipment_adjustment_event_list.append(componentsschemas_removal_shipment_adjustment_event_list_item)

        trial_shipment_event_list = []
        _trial_shipment_event_list = d.pop("TrialShipmentEventList", UNSET)
        for componentsschemas_trial_shipment_event_list_item_data in _trial_shipment_event_list or []:
            componentsschemas_trial_shipment_event_list_item = TrialShipmentEvent.from_dict(
                componentsschemas_trial_shipment_event_list_item_data
            )

            trial_shipment_event_list.append(componentsschemas_trial_shipment_event_list_item)

        tds_reimbursement_event_list = []
        _tds_reimbursement_event_list = d.pop("TDSReimbursementEventList", UNSET)
        for componentsschemas_tds_reimbursement_event_list_item_data in _tds_reimbursement_event_list or []:
            componentsschemas_tds_reimbursement_event_list_item = TDSReimbursementEvent.from_dict(
                componentsschemas_tds_reimbursement_event_list_item_data
            )

            tds_reimbursement_event_list.append(componentsschemas_tds_reimbursement_event_list_item)

        adhoc_disbursement_event_list = []
        _adhoc_disbursement_event_list = d.pop("AdhocDisbursementEventList", UNSET)
        for componentsschemas_adhoc_disbursement_event_list_item_data in _adhoc_disbursement_event_list or []:
            componentsschemas_adhoc_disbursement_event_list_item = AdhocDisbursementEvent.from_dict(
                componentsschemas_adhoc_disbursement_event_list_item_data
            )

            adhoc_disbursement_event_list.append(componentsschemas_adhoc_disbursement_event_list_item)

        tax_withholding_event_list = []
        _tax_withholding_event_list = d.pop("TaxWithholdingEventList", UNSET)
        for componentsschemas_tax_withholding_event_list_item_data in _tax_withholding_event_list or []:
            componentsschemas_tax_withholding_event_list_item = TaxWithholdingEvent.from_dict(
                componentsschemas_tax_withholding_event_list_item_data
            )

            tax_withholding_event_list.append(componentsschemas_tax_withholding_event_list_item)

        charge_refund_event_list = []
        _charge_refund_event_list = d.pop("ChargeRefundEventList", UNSET)
        for componentsschemas_charge_refund_event_list_item_data in _charge_refund_event_list or []:
            componentsschemas_charge_refund_event_list_item = ChargeRefundEvent.from_dict(
                componentsschemas_charge_refund_event_list_item_data
            )

            charge_refund_event_list.append(componentsschemas_charge_refund_event_list_item)

        _failed_adhoc_disbursement_event_list = d.pop("FailedAdhocDisbursementEventList", UNSET)
        failed_adhoc_disbursement_event_list: Union[Unset, FailedAdhocDisbursementEventList]
        if isinstance(_failed_adhoc_disbursement_event_list, Unset):
            failed_adhoc_disbursement_event_list = UNSET
        else:
            failed_adhoc_disbursement_event_list = FailedAdhocDisbursementEventList.from_dict(
                _failed_adhoc_disbursement_event_list
            )

        _value_added_service_charge_event_list = d.pop("ValueAddedServiceChargeEventList", UNSET)
        value_added_service_charge_event_list: Union[Unset, ValueAddedServiceChargeEventList]
        if isinstance(_value_added_service_charge_event_list, Unset):
            value_added_service_charge_event_list = UNSET
        else:
            value_added_service_charge_event_list = ValueAddedServiceChargeEventList.from_dict(
                _value_added_service_charge_event_list
            )

        capacity_reservation_billing_event_list = []
        _capacity_reservation_billing_event_list = d.pop("CapacityReservationBillingEventList", UNSET)
        for componentsschemas_capacity_reservation_billing_event_list_item_data in (
            _capacity_reservation_billing_event_list or []
        ):
            componentsschemas_capacity_reservation_billing_event_list_item = CapacityReservationBillingEvent.from_dict(
                componentsschemas_capacity_reservation_billing_event_list_item_data
            )

            capacity_reservation_billing_event_list.append(
                componentsschemas_capacity_reservation_billing_event_list_item
            )

        result = cls(
            shipment_event_list=shipment_event_list,
            shipment_settle_event_list=shipment_settle_event_list,
            refund_event_list=refund_event_list,
            guarantee_claim_event_list=guarantee_claim_event_list,
            chargeback_event_list=chargeback_event_list,
            pay_with_amazon_event_list=pay_with_amazon_event_list,
            service_provider_credit_event_list=service_provider_credit_event_list,
            retrocharge_event_list=retrocharge_event_list,
            rental_transaction_event_list=rental_transaction_event_list,
            product_ads_payment_event_list=product_ads_payment_event_list,
            service_fee_event_list=service_fee_event_list,
            seller_deal_payment_event_list=seller_deal_payment_event_list,
            debt_recovery_event_list=debt_recovery_event_list,
            loan_servicing_event_list=loan_servicing_event_list,
            adjustment_event_list=adjustment_event_list,
            safet_reimbursement_event_list=safet_reimbursement_event_list,
            seller_review_enrollment_payment_event_list=seller_review_enrollment_payment_event_list,
            fba_liquidation_event_list=fba_liquidation_event_list,
            coupon_payment_event_list=coupon_payment_event_list,
            imaging_services_fee_event_list=imaging_services_fee_event_list,
            network_commingling_transaction_event_list=network_commingling_transaction_event_list,
            affordability_expense_event_list=affordability_expense_event_list,
            affordability_expense_reversal_event_list=affordability_expense_reversal_event_list,
            removal_shipment_event_list=removal_shipment_event_list,
            removal_shipment_adjustment_event_list=removal_shipment_adjustment_event_list,
            trial_shipment_event_list=trial_shipment_event_list,
            tds_reimbursement_event_list=tds_reimbursement_event_list,
            adhoc_disbursement_event_list=adhoc_disbursement_event_list,
            tax_withholding_event_list=tax_withholding_event_list,
            charge_refund_event_list=charge_refund_event_list,
            failed_adhoc_disbursement_event_list=failed_adhoc_disbursement_event_list,
            value_added_service_charge_event_list=value_added_service_charge_event_list,
            capacity_reservation_billing_event_list=capacity_reservation_billing_event_list,
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
