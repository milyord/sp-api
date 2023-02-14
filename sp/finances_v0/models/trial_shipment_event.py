import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_component import FeeComponent


T = TypeVar("T", bound="TrialShipmentEvent")


@attr.s(auto_attribs=True)
class TrialShipmentEvent:
    r"""An event related to a trial shipment.

    Attributes:
        amazon_order_id (Union[Unset, str]): An Amazon-defined identifier for an order.
        financial_event_group_id (Union[Unset, str]): The identifier of the financial event group.
        posted_date (Union[Unset, datetime.datetime]):
        sku (Union[Unset, str]): The seller SKU of the item. The seller SKU is qualified by the seller's seller ID,
            which is included with every call to the Selling Partner API.
        fee_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
    """

    amazon_order_id: Union[Unset, str] = UNSET
    financial_event_group_id: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    sku: Union[Unset, str] = UNSET
    fee_list: Union[Unset, List["FeeComponent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        financial_event_group_id = self.financial_event_group_id
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        sku = self.sku
        fee_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fee_list, Unset):
            fee_list = []
            for componentsschemas_fee_component_list_item_data in self.fee_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                fee_list.append(componentsschemas_fee_component_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_order_id is not UNSET:
            field_dict["AmazonOrderId"] = amazon_order_id
        if financial_event_group_id is not UNSET:
            field_dict["FinancialEventGroupId"] = financial_event_group_id
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if sku is not UNSET:
            field_dict["SKU"] = sku
        if fee_list is not UNSET:
            field_dict["FeeList"] = fee_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fee_component import FeeComponent

        d = src_dict.copy()
        amazon_order_id = d.pop("AmazonOrderId", UNSET)

        financial_event_group_id = d.pop("FinancialEventGroupId", UNSET)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        sku = d.pop("SKU", UNSET)

        fee_list = []
        _fee_list = d.pop("FeeList", UNSET)
        for componentsschemas_fee_component_list_item_data in _fee_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            fee_list.append(componentsschemas_fee_component_list_item)

        result = cls(
            amazon_order_id=amazon_order_id,
            financial_event_group_id=financial_event_group_id,
            posted_date=posted_date,
            sku=sku,
            fee_list=fee_list,
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
