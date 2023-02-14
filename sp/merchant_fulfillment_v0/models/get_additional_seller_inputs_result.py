from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_inputs import AdditionalInputs
    from ..models.item_level_fields import ItemLevelFields


T = TypeVar("T", bound="GetAdditionalSellerInputsResult")


@attr.s(auto_attribs=True)
class GetAdditionalSellerInputsResult:
    r"""The payload for the getAdditionalSellerInputs operation.

    Attributes:
        shipment_level_fields (Union[Unset, List['AdditionalInputs']]): A list of additional inputs.
        item_level_fields_list (Union[Unset, List['ItemLevelFields']]): A list of item level fields.
    """

    shipment_level_fields: Union[Unset, List["AdditionalInputs"]] = UNSET
    item_level_fields_list: Union[Unset, List["ItemLevelFields"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_level_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_level_fields, Unset):
            shipment_level_fields = []
            for componentsschemas_additional_inputs_list_item_data in self.shipment_level_fields:
                componentsschemas_additional_inputs_list_item = (
                    componentsschemas_additional_inputs_list_item_data.to_dict()
                )

                shipment_level_fields.append(componentsschemas_additional_inputs_list_item)

        item_level_fields_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_level_fields_list, Unset):
            item_level_fields_list = []
            for componentsschemas_item_level_fields_list_item_data in self.item_level_fields_list:
                componentsschemas_item_level_fields_list_item = (
                    componentsschemas_item_level_fields_list_item_data.to_dict()
                )

                item_level_fields_list.append(componentsschemas_item_level_fields_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment_level_fields is not UNSET:
            field_dict["ShipmentLevelFields"] = shipment_level_fields
        if item_level_fields_list is not UNSET:
            field_dict["ItemLevelFieldsList"] = item_level_fields_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_inputs import AdditionalInputs
        from ..models.item_level_fields import ItemLevelFields

        d = src_dict.copy()
        shipment_level_fields = []
        _shipment_level_fields = d.pop("ShipmentLevelFields", UNSET)
        for componentsschemas_additional_inputs_list_item_data in _shipment_level_fields or []:
            componentsschemas_additional_inputs_list_item = AdditionalInputs.from_dict(
                componentsschemas_additional_inputs_list_item_data
            )

            shipment_level_fields.append(componentsschemas_additional_inputs_list_item)

        item_level_fields_list = []
        _item_level_fields_list = d.pop("ItemLevelFieldsList", UNSET)
        for componentsschemas_item_level_fields_list_item_data in _item_level_fields_list or []:
            componentsschemas_item_level_fields_list_item = ItemLevelFields.from_dict(
                componentsschemas_item_level_fields_list_item_data
            )

            item_level_fields_list.append(componentsschemas_item_level_fields_list_item)

        result = cls(
            shipment_level_fields=shipment_level_fields,
            item_level_fields_list=item_level_fields_list,
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
