from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.additional_seller_input import AdditionalSellerInput


T = TypeVar("T", bound="AdditionalSellerInputs")


@attr.s(auto_attribs=True)
class AdditionalSellerInputs:
    r"""An additional set of seller inputs required to purchase shipping.

    Attributes:
        additional_input_field_name (str): The name of the additional input field.
        additional_seller_input (AdditionalSellerInput): Additional information required to purchase shipping.
    """

    additional_input_field_name: str
    additional_seller_input: "AdditionalSellerInput"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additional_input_field_name = self.additional_input_field_name
        additional_seller_input = self.additional_seller_input.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AdditionalInputFieldName": additional_input_field_name,
                "AdditionalSellerInput": additional_seller_input,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_seller_input import AdditionalSellerInput

        d = src_dict.copy()
        additional_input_field_name = d.pop("AdditionalInputFieldName")

        additional_seller_input = AdditionalSellerInput.from_dict(d.pop("AdditionalSellerInput"))

        result = cls(
            additional_input_field_name=additional_input_field_name,
            additional_seller_input=additional_seller_input,
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
