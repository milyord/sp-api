from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.time_slot import TimeSlot


T = TypeVar("T", bound="ListHandoverSlotsResponse")


@attr.s(auto_attribs=True)
class ListHandoverSlotsResponse:
    r"""The response schema for the `listHandoverSlots` operation.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier. Identifies the order that the seller wants to deliver
            using Amazon Easy Ship.
        time_slots (List['TimeSlot']): A list of time slots.
    """

    amazon_order_id: str
    time_slots: List["TimeSlot"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        time_slots = []
        for componentsschemas_time_slots_item_data in self.time_slots:
            componentsschemas_time_slots_item = componentsschemas_time_slots_item_data.to_dict()

            time_slots.append(componentsschemas_time_slots_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amazonOrderId": amazon_order_id,
                "timeSlots": time_slots,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.time_slot import TimeSlot

        d = src_dict.copy()
        amazon_order_id = d.pop("amazonOrderId")

        time_slots = []
        _time_slots = d.pop("timeSlots")
        for componentsschemas_time_slots_item_data in _time_slots:
            componentsschemas_time_slots_item = TimeSlot.from_dict(componentsschemas_time_slots_item_data)

            time_slots.append(componentsschemas_time_slots_item)

        result = cls(
            amazon_order_id=amazon_order_id,
            time_slots=time_slots,
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
