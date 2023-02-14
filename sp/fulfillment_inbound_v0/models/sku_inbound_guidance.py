from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.guidance_reason import GuidanceReason
from ..models.inbound_guidance import InboundGuidance
from ..types import UNSET, Unset

T = TypeVar("T", bound="SKUInboundGuidance")


@attr.s(auto_attribs=True)
class SKUInboundGuidance:
    r"""Reasons why a given seller SKU is not recommended for shipment to Amazon's fulfillment network.

    Attributes:
        seller_sku (str): The seller SKU of the item.
        asin (str): The Amazon Standard Identification Number (ASIN) of the item.
        inbound_guidance (InboundGuidance): Specific inbound guidance for an item.
        guidance_reason_list (Union[Unset, List[GuidanceReason]]): A list of inbound guidance reason information.
    """

    seller_sku: str
    asin: str
    inbound_guidance: InboundGuidance
    guidance_reason_list: Union[Unset, List[GuidanceReason]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        asin = self.asin
        inbound_guidance = self.inbound_guidance.value

        guidance_reason_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.guidance_reason_list, Unset):
            guidance_reason_list = []
            for componentsschemas_guidance_reason_list_item_data in self.guidance_reason_list:
                componentsschemas_guidance_reason_list_item = componentsschemas_guidance_reason_list_item_data.value

                guidance_reason_list.append(componentsschemas_guidance_reason_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SellerSKU": seller_sku,
                "ASIN": asin,
                "InboundGuidance": inbound_guidance,
            }
        )
        if guidance_reason_list is not UNSET:
            field_dict["GuidanceReasonList"] = guidance_reason_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seller_sku = d.pop("SellerSKU")

        asin = d.pop("ASIN")

        inbound_guidance = InboundGuidance(d.pop("InboundGuidance"))

        guidance_reason_list = []
        _guidance_reason_list = d.pop("GuidanceReasonList", UNSET)
        for componentsschemas_guidance_reason_list_item_data in _guidance_reason_list or []:
            componentsschemas_guidance_reason_list_item = GuidanceReason(
                componentsschemas_guidance_reason_list_item_data
            )

            guidance_reason_list.append(componentsschemas_guidance_reason_list_item)

        result = cls(
            seller_sku=seller_sku,
            asin=asin,
            inbound_guidance=inbound_guidance,
            guidance_reason_list=guidance_reason_list,
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
