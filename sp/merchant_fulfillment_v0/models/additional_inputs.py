from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.seller_input_definition import SellerInputDefinition


T = TypeVar("T", bound="AdditionalInputs")


@attr.s(auto_attribs=True)
class AdditionalInputs:
    r"""Maps the additional seller input to the definition. The key to the map is the field name.

    Attributes:
        additional_input_field_name (Union[Unset, str]): The field name.
        seller_input_definition (Union[Unset, SellerInputDefinition]): Specifies characteristics that apply to a seller
            input.
    """

    additional_input_field_name: Union[Unset, str] = UNSET
    seller_input_definition: Union[Unset, "SellerInputDefinition"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additional_input_field_name = self.additional_input_field_name
        seller_input_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seller_input_definition, Unset):
            seller_input_definition = self.seller_input_definition.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_input_field_name is not UNSET:
            field_dict["AdditionalInputFieldName"] = additional_input_field_name
        if seller_input_definition is not UNSET:
            field_dict["SellerInputDefinition"] = seller_input_definition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.seller_input_definition import SellerInputDefinition

        d = src_dict.copy()
        additional_input_field_name = d.pop("AdditionalInputFieldName", UNSET)

        _seller_input_definition = d.pop("SellerInputDefinition", UNSET)
        seller_input_definition: Union[Unset, SellerInputDefinition]
        if isinstance(_seller_input_definition, Unset):
            seller_input_definition = UNSET
        else:
            seller_input_definition = SellerInputDefinition.from_dict(_seller_input_definition)

        result = cls(
            additional_input_field_name=additional_input_field_name,
            seller_input_definition=seller_input_definition,
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
