from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asin_inbound_guidance import ASINInboundGuidance
    from ..models.invalid_asin import InvalidASIN
    from ..models.invalid_sku import InvalidSKU
    from ..models.sku_inbound_guidance import SKUInboundGuidance


T = TypeVar("T", bound="GetInboundGuidanceResult")


@attr.s(auto_attribs=True)
class GetInboundGuidanceResult:
    r"""
    Attributes:
        sku_inbound_guidance_list (Union[Unset, List['SKUInboundGuidance']]): A list of SKU inbound guidance
            information.
        invalid_sku_list (Union[Unset, List['InvalidSKU']]): A list of invalid SKU values and the reason they are
            invalid.
        asin_inbound_guidance_list (Union[Unset, List['ASINInboundGuidance']]): A list of ASINs and their associated
            inbound guidance.
        invalid_asin_list (Union[Unset, List['InvalidASIN']]): A list of invalid ASIN values and the reasons they are
            invalid.
    """

    sku_inbound_guidance_list: Union[Unset, List["SKUInboundGuidance"]] = UNSET
    invalid_sku_list: Union[Unset, List["InvalidSKU"]] = UNSET
    asin_inbound_guidance_list: Union[Unset, List["ASINInboundGuidance"]] = UNSET
    invalid_asin_list: Union[Unset, List["InvalidASIN"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_inbound_guidance_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sku_inbound_guidance_list, Unset):
            sku_inbound_guidance_list = []
            for componentsschemas_sku_inbound_guidance_list_item_data in self.sku_inbound_guidance_list:
                componentsschemas_sku_inbound_guidance_list_item = (
                    componentsschemas_sku_inbound_guidance_list_item_data.to_dict()
                )

                sku_inbound_guidance_list.append(componentsschemas_sku_inbound_guidance_list_item)

        invalid_sku_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invalid_sku_list, Unset):
            invalid_sku_list = []
            for componentsschemas_invalid_sku_list_item_data in self.invalid_sku_list:
                componentsschemas_invalid_sku_list_item = componentsschemas_invalid_sku_list_item_data.to_dict()

                invalid_sku_list.append(componentsschemas_invalid_sku_list_item)

        asin_inbound_guidance_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.asin_inbound_guidance_list, Unset):
            asin_inbound_guidance_list = []
            for componentsschemas_asin_inbound_guidance_list_item_data in self.asin_inbound_guidance_list:
                componentsschemas_asin_inbound_guidance_list_item = (
                    componentsschemas_asin_inbound_guidance_list_item_data.to_dict()
                )

                asin_inbound_guidance_list.append(componentsschemas_asin_inbound_guidance_list_item)

        invalid_asin_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invalid_asin_list, Unset):
            invalid_asin_list = []
            for componentsschemas_invalid_asin_list_item_data in self.invalid_asin_list:
                componentsschemas_invalid_asin_list_item = componentsschemas_invalid_asin_list_item_data.to_dict()

                invalid_asin_list.append(componentsschemas_invalid_asin_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_inbound_guidance_list is not UNSET:
            field_dict["SKUInboundGuidanceList"] = sku_inbound_guidance_list
        if invalid_sku_list is not UNSET:
            field_dict["InvalidSKUList"] = invalid_sku_list
        if asin_inbound_guidance_list is not UNSET:
            field_dict["ASINInboundGuidanceList"] = asin_inbound_guidance_list
        if invalid_asin_list is not UNSET:
            field_dict["InvalidASINList"] = invalid_asin_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asin_inbound_guidance import ASINInboundGuidance
        from ..models.invalid_asin import InvalidASIN
        from ..models.invalid_sku import InvalidSKU
        from ..models.sku_inbound_guidance import SKUInboundGuidance

        d = src_dict.copy()
        sku_inbound_guidance_list = []
        _sku_inbound_guidance_list = d.pop("SKUInboundGuidanceList", UNSET)
        for componentsschemas_sku_inbound_guidance_list_item_data in _sku_inbound_guidance_list or []:
            componentsschemas_sku_inbound_guidance_list_item = SKUInboundGuidance.from_dict(
                componentsschemas_sku_inbound_guidance_list_item_data
            )

            sku_inbound_guidance_list.append(componentsschemas_sku_inbound_guidance_list_item)

        invalid_sku_list = []
        _invalid_sku_list = d.pop("InvalidSKUList", UNSET)
        for componentsschemas_invalid_sku_list_item_data in _invalid_sku_list or []:
            componentsschemas_invalid_sku_list_item = InvalidSKU.from_dict(componentsschemas_invalid_sku_list_item_data)

            invalid_sku_list.append(componentsschemas_invalid_sku_list_item)

        asin_inbound_guidance_list = []
        _asin_inbound_guidance_list = d.pop("ASINInboundGuidanceList", UNSET)
        for componentsschemas_asin_inbound_guidance_list_item_data in _asin_inbound_guidance_list or []:
            componentsschemas_asin_inbound_guidance_list_item = ASINInboundGuidance.from_dict(
                componentsschemas_asin_inbound_guidance_list_item_data
            )

            asin_inbound_guidance_list.append(componentsschemas_asin_inbound_guidance_list_item)

        invalid_asin_list = []
        _invalid_asin_list = d.pop("InvalidASINList", UNSET)
        for componentsschemas_invalid_asin_list_item_data in _invalid_asin_list or []:
            componentsschemas_invalid_asin_list_item = InvalidASIN.from_dict(
                componentsschemas_invalid_asin_list_item_data
            )

            invalid_asin_list.append(componentsschemas_invalid_asin_list_item)

        result = cls(
            sku_inbound_guidance_list=sku_inbound_guidance_list,
            invalid_sku_list=invalid_sku_list,
            asin_inbound_guidance_list=asin_inbound_guidance_list,
            invalid_asin_list=invalid_asin_list,
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
