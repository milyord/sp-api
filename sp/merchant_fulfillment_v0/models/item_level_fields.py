from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.additional_inputs import AdditionalInputs


T = TypeVar("T", bound="ItemLevelFields")


@attr.s(auto_attribs=True)
class ItemLevelFields:
    r"""
    Attributes:
        asin (str): The Amazon Standard Identification Number (ASIN) of the item.
        additional_inputs (List['AdditionalInputs']): A list of additional inputs.
    """

    asin: str
    additional_inputs: List["AdditionalInputs"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        additional_inputs = []
        for componentsschemas_additional_inputs_list_item_data in self.additional_inputs:
            componentsschemas_additional_inputs_list_item = componentsschemas_additional_inputs_list_item_data.to_dict()

            additional_inputs.append(componentsschemas_additional_inputs_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Asin": asin,
                "AdditionalInputs": additional_inputs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_inputs import AdditionalInputs

        d = src_dict.copy()
        asin = d.pop("Asin")

        additional_inputs = []
        _additional_inputs = d.pop("AdditionalInputs")
        for componentsschemas_additional_inputs_list_item_data in _additional_inputs:
            componentsschemas_additional_inputs_list_item = AdditionalInputs.from_dict(
                componentsschemas_additional_inputs_list_item_data
            )

            additional_inputs.append(componentsschemas_additional_inputs_list_item)

        result = cls(
            asin=asin,
            additional_inputs=additional_inputs,
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
