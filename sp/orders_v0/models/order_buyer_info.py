from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buyer_tax_info import BuyerTaxInfo


T = TypeVar("T", bound="OrderBuyerInfo")


@attr.s(auto_attribs=True)
class OrderBuyerInfo:
    r"""Buyer information for an order.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier, in 3-7-7 format.
        buyer_email (Union[Unset, str]): The anonymized email address of the buyer.
        buyer_name (Union[Unset, str]): The buyer name or the recipient name.
        buyer_county (Union[Unset, str]): The county of the buyer.
        buyer_tax_info (Union[Unset, BuyerTaxInfo]): Tax information about the buyer.
        purchase_order_number (Union[Unset, str]): The purchase order (PO) number entered by the buyer at checkout.
            Returned only for orders where the buyer entered a PO number at checkout.
    """

    amazon_order_id: str
    buyer_email: Union[Unset, str] = UNSET
    buyer_name: Union[Unset, str] = UNSET
    buyer_county: Union[Unset, str] = UNSET
    buyer_tax_info: Union[Unset, "BuyerTaxInfo"] = UNSET
    purchase_order_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        buyer_email = self.buyer_email
        buyer_name = self.buyer_name
        buyer_county = self.buyer_county
        buyer_tax_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyer_tax_info, Unset):
            buyer_tax_info = self.buyer_tax_info.to_dict()

        purchase_order_number = self.purchase_order_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AmazonOrderId": amazon_order_id,
            }
        )
        if buyer_email is not UNSET:
            field_dict["BuyerEmail"] = buyer_email
        if buyer_name is not UNSET:
            field_dict["BuyerName"] = buyer_name
        if buyer_county is not UNSET:
            field_dict["BuyerCounty"] = buyer_county
        if buyer_tax_info is not UNSET:
            field_dict["BuyerTaxInfo"] = buyer_tax_info
        if purchase_order_number is not UNSET:
            field_dict["PurchaseOrderNumber"] = purchase_order_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.buyer_tax_info import BuyerTaxInfo

        d = src_dict.copy()
        amazon_order_id = d.pop("AmazonOrderId")

        buyer_email = d.pop("BuyerEmail", UNSET)

        buyer_name = d.pop("BuyerName", UNSET)

        buyer_county = d.pop("BuyerCounty", UNSET)

        _buyer_tax_info = d.pop("BuyerTaxInfo", UNSET)
        buyer_tax_info: Union[Unset, BuyerTaxInfo]
        if isinstance(_buyer_tax_info, Unset):
            buyer_tax_info = UNSET
        else:
            buyer_tax_info = BuyerTaxInfo.from_dict(_buyer_tax_info)

        purchase_order_number = d.pop("PurchaseOrderNumber", UNSET)

        result = cls(
            amazon_order_id=amazon_order_id,
            buyer_email=buyer_email,
            buyer_name=buyer_name,
            buyer_county=buyer_county,
            buyer_tax_info=buyer_tax_info,
            purchase_order_number=purchase_order_number,
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
