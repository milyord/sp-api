from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.stop import Stop


T = TypeVar("T", bound="Route")


@attr.s(auto_attribs=True)
class Route:
    r"""This is used only for direct import shipment confirmations.

    Attributes:
        stops (List['Stop']):
    """

    stops: List["Stop"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stops = []
        for stops_item_data in self.stops:
            stops_item = stops_item_data.to_dict()

            stops.append(stops_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stops": stops,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stop import Stop

        d = src_dict.copy()
        stops = []
        _stops = d.pop("stops")
        for stops_item_data in _stops:
            stops_item = Stop.from_dict(stops_item_data)

            stops.append(stops_item)

        result = cls(
            stops=stops,
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
