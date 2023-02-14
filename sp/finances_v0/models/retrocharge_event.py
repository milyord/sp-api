import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.tax_withheld_component import TaxWithheldComponent


T = TypeVar("T", bound="RetrochargeEvent")


@attr.s(auto_attribs=True)
class RetrochargeEvent:
    r"""A retrocharge or retrocharge reversal.

    Attributes:
        retrocharge_event_type (Union[Unset, str]): The type of event.

            Possible values:

            * Retrocharge

            * RetrochargeReversal
        amazon_order_id (Union[Unset, str]): An Amazon-defined identifier for an order.
        posted_date (Union[Unset, datetime.datetime]):
        base_tax (Union[Unset, Currency]): A currency type and amount.
        shipping_tax (Union[Unset, Currency]): A currency type and amount.
        marketplace_name (Union[Unset, str]): The name of the marketplace where the retrocharge event occurred.
        retrocharge_tax_withheld_list (Union[Unset, List['TaxWithheldComponent']]): A list of information about taxes
            withheld.
    """

    retrocharge_event_type: Union[Unset, str] = UNSET
    amazon_order_id: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    base_tax: Union[Unset, "Currency"] = UNSET
    shipping_tax: Union[Unset, "Currency"] = UNSET
    marketplace_name: Union[Unset, str] = UNSET
    retrocharge_tax_withheld_list: Union[Unset, List["TaxWithheldComponent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        retrocharge_event_type = self.retrocharge_event_type
        amazon_order_id = self.amazon_order_id
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        base_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base_tax, Unset):
            base_tax = self.base_tax.to_dict()

        shipping_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_tax, Unset):
            shipping_tax = self.shipping_tax.to_dict()

        marketplace_name = self.marketplace_name
        retrocharge_tax_withheld_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.retrocharge_tax_withheld_list, Unset):
            retrocharge_tax_withheld_list = []
            for componentsschemas_tax_withheld_component_list_item_data in self.retrocharge_tax_withheld_list:
                componentsschemas_tax_withheld_component_list_item = (
                    componentsschemas_tax_withheld_component_list_item_data.to_dict()
                )

                retrocharge_tax_withheld_list.append(componentsschemas_tax_withheld_component_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retrocharge_event_type is not UNSET:
            field_dict["RetrochargeEventType"] = retrocharge_event_type
        if amazon_order_id is not UNSET:
            field_dict["AmazonOrderId"] = amazon_order_id
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if base_tax is not UNSET:
            field_dict["BaseTax"] = base_tax
        if shipping_tax is not UNSET:
            field_dict["ShippingTax"] = shipping_tax
        if marketplace_name is not UNSET:
            field_dict["MarketplaceName"] = marketplace_name
        if retrocharge_tax_withheld_list is not UNSET:
            field_dict["RetrochargeTaxWithheldList"] = retrocharge_tax_withheld_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.tax_withheld_component import TaxWithheldComponent

        d = src_dict.copy()
        retrocharge_event_type = d.pop("RetrochargeEventType", UNSET)

        amazon_order_id = d.pop("AmazonOrderId", UNSET)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        _base_tax = d.pop("BaseTax", UNSET)
        base_tax: Union[Unset, Currency]
        if isinstance(_base_tax, Unset):
            base_tax = UNSET
        else:
            base_tax = Currency.from_dict(_base_tax)

        _shipping_tax = d.pop("ShippingTax", UNSET)
        shipping_tax: Union[Unset, Currency]
        if isinstance(_shipping_tax, Unset):
            shipping_tax = UNSET
        else:
            shipping_tax = Currency.from_dict(_shipping_tax)

        marketplace_name = d.pop("MarketplaceName", UNSET)

        retrocharge_tax_withheld_list = []
        _retrocharge_tax_withheld_list = d.pop("RetrochargeTaxWithheldList", UNSET)
        for componentsschemas_tax_withheld_component_list_item_data in _retrocharge_tax_withheld_list or []:
            componentsschemas_tax_withheld_component_list_item = TaxWithheldComponent.from_dict(
                componentsschemas_tax_withheld_component_list_item_data
            )

            retrocharge_tax_withheld_list.append(componentsschemas_tax_withheld_component_list_item)

        result = cls(
            retrocharge_event_type=retrocharge_event_type,
            amazon_order_id=amazon_order_id,
            posted_date=posted_date,
            base_tax=base_tax,
            shipping_tax=shipping_tax,
            marketplace_name=marketplace_name,
            retrocharge_tax_withheld_list=retrocharge_tax_withheld_list,
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
