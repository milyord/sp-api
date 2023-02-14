import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_component import ChargeComponent
    from ..models.currency import Currency
    from ..models.fee_component import FeeComponent
    from ..models.tax_withheld_component import TaxWithheldComponent


T = TypeVar("T", bound="RentalTransactionEvent")


@attr.s(auto_attribs=True)
class RentalTransactionEvent:
    r"""An event related to a rental transaction.

    Attributes:
        amazon_order_id (Union[Unset, str]): An Amazon-defined identifier for an order.
        rental_event_type (Union[Unset, str]): The type of rental event.

            Possible values:

            * RentalCustomerPayment-Buyout - Transaction type that represents when the customer wants to buy out a rented
            item.

            * RentalCustomerPayment-Extension - Transaction type that represents when the customer wants to extend the
            rental period.

            * RentalCustomerRefund-Buyout - Transaction type that represents when the customer requests a refund for the
            buyout of the rented item.

            * RentalCustomerRefund-Extension - Transaction type that represents when the customer requests a refund over the
            extension on the rented item.

            * RentalHandlingFee - Transaction type that represents the fee that Amazon charges sellers who rent through
            Amazon.

            * RentalChargeFailureReimbursement - Transaction type that represents when Amazon sends money to the seller to
            compensate for a failed charge.

            * RentalLostItemReimbursement - Transaction type that represents when Amazon sends money to the seller to
            compensate for a lost item.
        extension_length (Union[Unset, int]): The number of days that the buyer extended an already rented item. This
            value is only returned for RentalCustomerPayment-Extension and RentalCustomerRefund-Extension events.
        posted_date (Union[Unset, datetime.datetime]):
        rental_charge_list (Union[Unset, List['ChargeComponent']]): A list of charge information on the seller's
            account.
        rental_fee_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
        marketplace_name (Union[Unset, str]): The name of the marketplace.
        rental_initial_value (Union[Unset, Currency]): A currency type and amount.
        rental_reimbursement (Union[Unset, Currency]): A currency type and amount.
        rental_tax_withheld_list (Union[Unset, List['TaxWithheldComponent']]): A list of information about taxes
            withheld.
    """

    amazon_order_id: Union[Unset, str] = UNSET
    rental_event_type: Union[Unset, str] = UNSET
    extension_length: Union[Unset, int] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    rental_charge_list: Union[Unset, List["ChargeComponent"]] = UNSET
    rental_fee_list: Union[Unset, List["FeeComponent"]] = UNSET
    marketplace_name: Union[Unset, str] = UNSET
    rental_initial_value: Union[Unset, "Currency"] = UNSET
    rental_reimbursement: Union[Unset, "Currency"] = UNSET
    rental_tax_withheld_list: Union[Unset, List["TaxWithheldComponent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        rental_event_type = self.rental_event_type
        extension_length = self.extension_length
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        rental_charge_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rental_charge_list, Unset):
            rental_charge_list = []
            for componentsschemas_charge_component_list_item_data in self.rental_charge_list:
                componentsschemas_charge_component_list_item = (
                    componentsschemas_charge_component_list_item_data.to_dict()
                )

                rental_charge_list.append(componentsschemas_charge_component_list_item)

        rental_fee_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rental_fee_list, Unset):
            rental_fee_list = []
            for componentsschemas_fee_component_list_item_data in self.rental_fee_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                rental_fee_list.append(componentsschemas_fee_component_list_item)

        marketplace_name = self.marketplace_name
        rental_initial_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rental_initial_value, Unset):
            rental_initial_value = self.rental_initial_value.to_dict()

        rental_reimbursement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rental_reimbursement, Unset):
            rental_reimbursement = self.rental_reimbursement.to_dict()

        rental_tax_withheld_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rental_tax_withheld_list, Unset):
            rental_tax_withheld_list = []
            for componentsschemas_tax_withheld_component_list_item_data in self.rental_tax_withheld_list:
                componentsschemas_tax_withheld_component_list_item = (
                    componentsschemas_tax_withheld_component_list_item_data.to_dict()
                )

                rental_tax_withheld_list.append(componentsschemas_tax_withheld_component_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_order_id is not UNSET:
            field_dict["AmazonOrderId"] = amazon_order_id
        if rental_event_type is not UNSET:
            field_dict["RentalEventType"] = rental_event_type
        if extension_length is not UNSET:
            field_dict["ExtensionLength"] = extension_length
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if rental_charge_list is not UNSET:
            field_dict["RentalChargeList"] = rental_charge_list
        if rental_fee_list is not UNSET:
            field_dict["RentalFeeList"] = rental_fee_list
        if marketplace_name is not UNSET:
            field_dict["MarketplaceName"] = marketplace_name
        if rental_initial_value is not UNSET:
            field_dict["RentalInitialValue"] = rental_initial_value
        if rental_reimbursement is not UNSET:
            field_dict["RentalReimbursement"] = rental_reimbursement
        if rental_tax_withheld_list is not UNSET:
            field_dict["RentalTaxWithheldList"] = rental_tax_withheld_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_component import ChargeComponent
        from ..models.currency import Currency
        from ..models.fee_component import FeeComponent
        from ..models.tax_withheld_component import TaxWithheldComponent

        d = src_dict.copy()
        amazon_order_id = d.pop("AmazonOrderId", UNSET)

        rental_event_type = d.pop("RentalEventType", UNSET)

        extension_length = d.pop("ExtensionLength", UNSET)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        rental_charge_list = []
        _rental_charge_list = d.pop("RentalChargeList", UNSET)
        for componentsschemas_charge_component_list_item_data in _rental_charge_list or []:
            componentsschemas_charge_component_list_item = ChargeComponent.from_dict(
                componentsschemas_charge_component_list_item_data
            )

            rental_charge_list.append(componentsschemas_charge_component_list_item)

        rental_fee_list = []
        _rental_fee_list = d.pop("RentalFeeList", UNSET)
        for componentsschemas_fee_component_list_item_data in _rental_fee_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            rental_fee_list.append(componentsschemas_fee_component_list_item)

        marketplace_name = d.pop("MarketplaceName", UNSET)

        _rental_initial_value = d.pop("RentalInitialValue", UNSET)
        rental_initial_value: Union[Unset, Currency]
        if isinstance(_rental_initial_value, Unset):
            rental_initial_value = UNSET
        else:
            rental_initial_value = Currency.from_dict(_rental_initial_value)

        _rental_reimbursement = d.pop("RentalReimbursement", UNSET)
        rental_reimbursement: Union[Unset, Currency]
        if isinstance(_rental_reimbursement, Unset):
            rental_reimbursement = UNSET
        else:
            rental_reimbursement = Currency.from_dict(_rental_reimbursement)

        rental_tax_withheld_list = []
        _rental_tax_withheld_list = d.pop("RentalTaxWithheldList", UNSET)
        for componentsschemas_tax_withheld_component_list_item_data in _rental_tax_withheld_list or []:
            componentsschemas_tax_withheld_component_list_item = TaxWithheldComponent.from_dict(
                componentsschemas_tax_withheld_component_list_item_data
            )

            rental_tax_withheld_list.append(componentsschemas_tax_withheld_component_list_item)

        result = cls(
            amazon_order_id=amazon_order_id,
            rental_event_type=rental_event_type,
            extension_length=extension_length,
            posted_date=posted_date,
            rental_charge_list=rental_charge_list,
            rental_fee_list=rental_fee_list,
            marketplace_name=marketplace_name,
            rental_initial_value=rental_initial_value,
            rental_reimbursement=rental_reimbursement,
            rental_tax_withheld_list=rental_tax_withheld_list,
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
