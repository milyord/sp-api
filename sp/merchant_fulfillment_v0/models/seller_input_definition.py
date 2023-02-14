from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.input_target_type import InputTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_seller_input import AdditionalSellerInput
    from ..models.constraint import Constraint


T = TypeVar("T", bound="SellerInputDefinition")


@attr.s(auto_attribs=True)
class SellerInputDefinition:
    r"""Specifies characteristics that apply to a seller input.

    Attributes:
        is_required (bool): When true, the additional input field is required.
        data_type (str): The data type of the additional input field.
        constraints (List['Constraint']): List of constraints.
        input_display_text (str): The display text for the additional input field.
        stored_value (AdditionalSellerInput): Additional information required to purchase shipping.
        input_target (Union[Unset, InputTargetType]): Indicates whether the additional seller input is at the item or
            shipment level.
        restricted_set_values (Union[Unset, List[str]]): The set of fixed values in an additional seller input.
    """

    is_required: bool
    data_type: str
    constraints: List["Constraint"]
    input_display_text: str
    stored_value: "AdditionalSellerInput"
    input_target: Union[Unset, InputTargetType] = UNSET
    restricted_set_values: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_required = self.is_required
        data_type = self.data_type
        constraints = []
        for componentsschemas_constraints_item_data in self.constraints:
            componentsschemas_constraints_item = componentsschemas_constraints_item_data.to_dict()

            constraints.append(componentsschemas_constraints_item)

        input_display_text = self.input_display_text
        stored_value = self.stored_value.to_dict()

        input_target: Union[Unset, str] = UNSET
        if not isinstance(self.input_target, Unset):
            input_target = self.input_target.value

        restricted_set_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.restricted_set_values, Unset):
            restricted_set_values = self.restricted_set_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "IsRequired": is_required,
                "DataType": data_type,
                "Constraints": constraints,
                "InputDisplayText": input_display_text,
                "StoredValue": stored_value,
            }
        )
        if input_target is not UNSET:
            field_dict["InputTarget"] = input_target
        if restricted_set_values is not UNSET:
            field_dict["RestrictedSetValues"] = restricted_set_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_seller_input import AdditionalSellerInput
        from ..models.constraint import Constraint

        d = src_dict.copy()
        is_required = d.pop("IsRequired")

        data_type = d.pop("DataType")

        constraints = []
        _constraints = d.pop("Constraints")
        for componentsschemas_constraints_item_data in _constraints:
            componentsschemas_constraints_item = Constraint.from_dict(componentsschemas_constraints_item_data)

            constraints.append(componentsschemas_constraints_item)

        input_display_text = d.pop("InputDisplayText")

        stored_value = AdditionalSellerInput.from_dict(d.pop("StoredValue"))

        _input_target = d.pop("InputTarget", UNSET)
        input_target: Union[Unset, InputTargetType]
        if isinstance(_input_target, Unset):
            input_target = UNSET
        else:
            input_target = InputTargetType(_input_target)

        restricted_set_values = cast(List[str], d.pop("RestrictedSetValues", UNSET))

        result = cls(
            is_required=is_required,
            data_type=data_type,
            constraints=constraints,
            input_display_text=input_display_text,
            stored_value=stored_value,
            input_target=input_target,
            restricted_set_values=restricted_set_values,
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
