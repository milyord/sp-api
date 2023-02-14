from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FulfillmentInstruction")


@attr.s(auto_attribs=True)
class FulfillmentInstruction:
    r"""Contains the instructions about the fulfillment like where should it be fulfilled from.

    Attributes:
        fulfillment_supply_source_id (Union[Unset, str]): Denotes the recommended sourceId where the order should be
            fulfilled from.
    """

    fulfillment_supply_source_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fulfillment_supply_source_id = self.fulfillment_supply_source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fulfillment_supply_source_id is not UNSET:
            field_dict["FulfillmentSupplySourceId"] = fulfillment_supply_source_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fulfillment_supply_source_id = d.pop("FulfillmentSupplySourceId", UNSET)

        result = cls(
            fulfillment_supply_source_id=fulfillment_supply_source_id,
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
