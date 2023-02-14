from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.barcode_instruction import BarcodeInstruction
from ..models.prep_guidance import PrepGuidance
from ..models.prep_instruction import PrepInstruction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon_prep_fees_details import AmazonPrepFeesDetails


T = TypeVar("T", bound="SKUPrepInstructions")


@attr.s(auto_attribs=True)
class SKUPrepInstructions:
    r"""Labeling requirements and item preparation instructions to help you prepare items for shipment to Amazon's
    fulfillment network.

        Attributes:
            seller_sku (Union[Unset, str]): The seller SKU of the item.
            asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
            barcode_instruction (Union[Unset, BarcodeInstruction]): Labeling requirements for the item. For more information
                about FBA labeling requirements, see the Seller Central Help for your marketplace.
            prep_guidance (Union[Unset, PrepGuidance]): Item preparation instructions.
            prep_instruction_list (Union[Unset, List[PrepInstruction]]): A list of preparation instructions to help with
                item sourcing decisions.
            amazon_prep_fees_details_list (Union[Unset, List['AmazonPrepFeesDetails']]): A list of preparation instructions
                and fees for Amazon to prep goods for shipment.
    """

    seller_sku: Union[Unset, str] = UNSET
    asin: Union[Unset, str] = UNSET
    barcode_instruction: Union[Unset, BarcodeInstruction] = UNSET
    prep_guidance: Union[Unset, PrepGuidance] = UNSET
    prep_instruction_list: Union[Unset, List[PrepInstruction]] = UNSET
    amazon_prep_fees_details_list: Union[Unset, List["AmazonPrepFeesDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        asin = self.asin
        barcode_instruction: Union[Unset, str] = UNSET
        if not isinstance(self.barcode_instruction, Unset):
            barcode_instruction = self.barcode_instruction.value

        prep_guidance: Union[Unset, str] = UNSET
        if not isinstance(self.prep_guidance, Unset):
            prep_guidance = self.prep_guidance.value

        prep_instruction_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.prep_instruction_list, Unset):
            prep_instruction_list = []
            for componentsschemas_prep_instruction_list_item_data in self.prep_instruction_list:
                componentsschemas_prep_instruction_list_item = componentsschemas_prep_instruction_list_item_data.value

                prep_instruction_list.append(componentsschemas_prep_instruction_list_item)

        amazon_prep_fees_details_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amazon_prep_fees_details_list, Unset):
            amazon_prep_fees_details_list = []
            for componentsschemas_amazon_prep_fees_details_list_item_data in self.amazon_prep_fees_details_list:
                componentsschemas_amazon_prep_fees_details_list_item = (
                    componentsschemas_amazon_prep_fees_details_list_item_data.to_dict()
                )

                amazon_prep_fees_details_list.append(componentsschemas_amazon_prep_fees_details_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seller_sku is not UNSET:
            field_dict["SellerSKU"] = seller_sku
        if asin is not UNSET:
            field_dict["ASIN"] = asin
        if barcode_instruction is not UNSET:
            field_dict["BarcodeInstruction"] = barcode_instruction
        if prep_guidance is not UNSET:
            field_dict["PrepGuidance"] = prep_guidance
        if prep_instruction_list is not UNSET:
            field_dict["PrepInstructionList"] = prep_instruction_list
        if amazon_prep_fees_details_list is not UNSET:
            field_dict["AmazonPrepFeesDetailsList"] = amazon_prep_fees_details_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amazon_prep_fees_details import AmazonPrepFeesDetails

        d = src_dict.copy()
        seller_sku = d.pop("SellerSKU", UNSET)

        asin = d.pop("ASIN", UNSET)

        _barcode_instruction = d.pop("BarcodeInstruction", UNSET)
        barcode_instruction: Union[Unset, BarcodeInstruction]
        if isinstance(_barcode_instruction, Unset):
            barcode_instruction = UNSET
        else:
            barcode_instruction = BarcodeInstruction(_barcode_instruction)

        _prep_guidance = d.pop("PrepGuidance", UNSET)
        prep_guidance: Union[Unset, PrepGuidance]
        if isinstance(_prep_guidance, Unset):
            prep_guidance = UNSET
        else:
            prep_guidance = PrepGuidance(_prep_guidance)

        prep_instruction_list = []
        _prep_instruction_list = d.pop("PrepInstructionList", UNSET)
        for componentsschemas_prep_instruction_list_item_data in _prep_instruction_list or []:
            componentsschemas_prep_instruction_list_item = PrepInstruction(
                componentsschemas_prep_instruction_list_item_data
            )

            prep_instruction_list.append(componentsschemas_prep_instruction_list_item)

        amazon_prep_fees_details_list = []
        _amazon_prep_fees_details_list = d.pop("AmazonPrepFeesDetailsList", UNSET)
        for componentsschemas_amazon_prep_fees_details_list_item_data in _amazon_prep_fees_details_list or []:
            componentsschemas_amazon_prep_fees_details_list_item = AmazonPrepFeesDetails.from_dict(
                componentsschemas_amazon_prep_fees_details_list_item_data
            )

            amazon_prep_fees_details_list.append(componentsschemas_amazon_prep_fees_details_list_item)

        result = cls(
            seller_sku=seller_sku,
            asin=asin,
            barcode_instruction=barcode_instruction,
            prep_guidance=prep_guidance,
            prep_instruction_list=prep_instruction_list,
            amazon_prep_fees_details_list=amazon_prep_fees_details_list,
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
