from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asin_prep_instructions import ASINPrepInstructions
    from ..models.invalid_asin import InvalidASIN
    from ..models.invalid_sku import InvalidSKU
    from ..models.sku_prep_instructions import SKUPrepInstructions


T = TypeVar("T", bound="GetPrepInstructionsResult")


@attr.s(auto_attribs=True)
class GetPrepInstructionsResult:
    r"""
    Attributes:
        sku_prep_instructions_list (Union[Unset, List['SKUPrepInstructions']]): A list of SKU labeling requirements and
            item preparation instructions.
        invalid_sku_list (Union[Unset, List['InvalidSKU']]): A list of invalid SKU values and the reason they are
            invalid.
        asin_prep_instructions_list (Union[Unset, List['ASINPrepInstructions']]): A list of item preparation
            instructions.
        invalid_asin_list (Union[Unset, List['InvalidASIN']]): A list of invalid ASIN values and the reasons they are
            invalid.
    """

    sku_prep_instructions_list: Union[Unset, List["SKUPrepInstructions"]] = UNSET
    invalid_sku_list: Union[Unset, List["InvalidSKU"]] = UNSET
    asin_prep_instructions_list: Union[Unset, List["ASINPrepInstructions"]] = UNSET
    invalid_asin_list: Union[Unset, List["InvalidASIN"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_prep_instructions_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sku_prep_instructions_list, Unset):
            sku_prep_instructions_list = []
            for componentsschemas_sku_prep_instructions_list_item_data in self.sku_prep_instructions_list:
                componentsschemas_sku_prep_instructions_list_item = (
                    componentsschemas_sku_prep_instructions_list_item_data.to_dict()
                )

                sku_prep_instructions_list.append(componentsschemas_sku_prep_instructions_list_item)

        invalid_sku_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invalid_sku_list, Unset):
            invalid_sku_list = []
            for componentsschemas_invalid_sku_list_item_data in self.invalid_sku_list:
                componentsschemas_invalid_sku_list_item = componentsschemas_invalid_sku_list_item_data.to_dict()

                invalid_sku_list.append(componentsschemas_invalid_sku_list_item)

        asin_prep_instructions_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.asin_prep_instructions_list, Unset):
            asin_prep_instructions_list = []
            for componentsschemas_asin_prep_instructions_list_item_data in self.asin_prep_instructions_list:
                componentsschemas_asin_prep_instructions_list_item = (
                    componentsschemas_asin_prep_instructions_list_item_data.to_dict()
                )

                asin_prep_instructions_list.append(componentsschemas_asin_prep_instructions_list_item)

        invalid_asin_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invalid_asin_list, Unset):
            invalid_asin_list = []
            for componentsschemas_invalid_asin_list_item_data in self.invalid_asin_list:
                componentsschemas_invalid_asin_list_item = componentsschemas_invalid_asin_list_item_data.to_dict()

                invalid_asin_list.append(componentsschemas_invalid_asin_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_prep_instructions_list is not UNSET:
            field_dict["SKUPrepInstructionsList"] = sku_prep_instructions_list
        if invalid_sku_list is not UNSET:
            field_dict["InvalidSKUList"] = invalid_sku_list
        if asin_prep_instructions_list is not UNSET:
            field_dict["ASINPrepInstructionsList"] = asin_prep_instructions_list
        if invalid_asin_list is not UNSET:
            field_dict["InvalidASINList"] = invalid_asin_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asin_prep_instructions import ASINPrepInstructions
        from ..models.invalid_asin import InvalidASIN
        from ..models.invalid_sku import InvalidSKU
        from ..models.sku_prep_instructions import SKUPrepInstructions

        d = src_dict.copy()
        sku_prep_instructions_list = []
        _sku_prep_instructions_list = d.pop("SKUPrepInstructionsList", UNSET)
        for componentsschemas_sku_prep_instructions_list_item_data in _sku_prep_instructions_list or []:
            componentsschemas_sku_prep_instructions_list_item = SKUPrepInstructions.from_dict(
                componentsschemas_sku_prep_instructions_list_item_data
            )

            sku_prep_instructions_list.append(componentsschemas_sku_prep_instructions_list_item)

        invalid_sku_list = []
        _invalid_sku_list = d.pop("InvalidSKUList", UNSET)
        for componentsschemas_invalid_sku_list_item_data in _invalid_sku_list or []:
            componentsschemas_invalid_sku_list_item = InvalidSKU.from_dict(componentsschemas_invalid_sku_list_item_data)

            invalid_sku_list.append(componentsschemas_invalid_sku_list_item)

        asin_prep_instructions_list = []
        _asin_prep_instructions_list = d.pop("ASINPrepInstructionsList", UNSET)
        for componentsschemas_asin_prep_instructions_list_item_data in _asin_prep_instructions_list or []:
            componentsschemas_asin_prep_instructions_list_item = ASINPrepInstructions.from_dict(
                componentsschemas_asin_prep_instructions_list_item_data
            )

            asin_prep_instructions_list.append(componentsschemas_asin_prep_instructions_list_item)

        invalid_asin_list = []
        _invalid_asin_list = d.pop("InvalidASINList", UNSET)
        for componentsschemas_invalid_asin_list_item_data in _invalid_asin_list or []:
            componentsschemas_invalid_asin_list_item = InvalidASIN.from_dict(
                componentsschemas_invalid_asin_list_item_data
            )

            invalid_asin_list.append(componentsschemas_invalid_asin_list_item)

        result = cls(
            sku_prep_instructions_list=sku_prep_instructions_list,
            invalid_sku_list=invalid_sku_list,
            asin_prep_instructions_list=asin_prep_instructions_list,
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
