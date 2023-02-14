from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_component import FeeComponent


T = TypeVar("T", bound="ServiceFeeEvent")


@attr.s(auto_attribs=True)
class ServiceFeeEvent:
    r"""A service fee on the seller's account.

    Attributes:
        amazon_order_id (Union[Unset, str]): An Amazon-defined identifier for an order.
        fee_reason (Union[Unset, str]): A short description of the service fee reason.
        fee_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
        seller_sku (Union[Unset, str]): The seller SKU of the item. The seller SKU is qualified by the seller's seller
            ID, which is included with every call to the Selling Partner API.
        fn_sku (Union[Unset, str]): A unique identifier assigned by Amazon to products stored in and fulfilled from an
            Amazon fulfillment center.
        fee_description (Union[Unset, str]): A short description of the service fee event.
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
    """

    amazon_order_id: Union[Unset, str] = UNSET
    fee_reason: Union[Unset, str] = UNSET
    fee_list: Union[Unset, List["FeeComponent"]] = UNSET
    seller_sku: Union[Unset, str] = UNSET
    fn_sku: Union[Unset, str] = UNSET
    fee_description: Union[Unset, str] = UNSET
    asin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        fee_reason = self.fee_reason
        fee_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fee_list, Unset):
            fee_list = []
            for componentsschemas_fee_component_list_item_data in self.fee_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                fee_list.append(componentsschemas_fee_component_list_item)

        seller_sku = self.seller_sku
        fn_sku = self.fn_sku
        fee_description = self.fee_description
        asin = self.asin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_order_id is not UNSET:
            field_dict["AmazonOrderId"] = amazon_order_id
        if fee_reason is not UNSET:
            field_dict["FeeReason"] = fee_reason
        if fee_list is not UNSET:
            field_dict["FeeList"] = fee_list
        if seller_sku is not UNSET:
            field_dict["SellerSKU"] = seller_sku
        if fn_sku is not UNSET:
            field_dict["FnSKU"] = fn_sku
        if fee_description is not UNSET:
            field_dict["FeeDescription"] = fee_description
        if asin is not UNSET:
            field_dict["ASIN"] = asin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fee_component import FeeComponent

        d = src_dict.copy()
        amazon_order_id = d.pop("AmazonOrderId", UNSET)

        fee_reason = d.pop("FeeReason", UNSET)

        fee_list = []
        _fee_list = d.pop("FeeList", UNSET)
        for componentsschemas_fee_component_list_item_data in _fee_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            fee_list.append(componentsschemas_fee_component_list_item)

        seller_sku = d.pop("SellerSKU", UNSET)

        fn_sku = d.pop("FnSKU", UNSET)

        fee_description = d.pop("FeeDescription", UNSET)

        asin = d.pop("ASIN", UNSET)

        result = cls(
            amazon_order_id=amazon_order_id,
            fee_reason=fee_reason,
            fee_list=fee_list,
            seller_sku=seller_sku,
            fn_sku=fn_sku,
            fee_description=fee_description,
            asin=asin,
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
