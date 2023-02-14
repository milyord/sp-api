from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.rate import Rate


T = TypeVar("T", bound="CreateShipmentResult")


@attr.s(auto_attribs=True)
class CreateShipmentResult:
    r"""The payload schema for the createShipment operation.

    Attributes:
        shipment_id (str): The unique shipment identifier.
        eligible_rates (List['Rate']): A list of all the available rates that can be used to send the shipment.
    """

    shipment_id: str
    eligible_rates: List["Rate"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_id = self.shipment_id
        eligible_rates = []
        for componentsschemas_rate_list_item_data in self.eligible_rates:
            componentsschemas_rate_list_item = componentsschemas_rate_list_item_data.to_dict()

            eligible_rates.append(componentsschemas_rate_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipmentId": shipment_id,
                "eligibleRates": eligible_rates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rate import Rate

        d = src_dict.copy()
        shipment_id = d.pop("shipmentId")

        eligible_rates = []
        _eligible_rates = d.pop("eligibleRates")
        for componentsschemas_rate_list_item_data in _eligible_rates:
            componentsschemas_rate_list_item = Rate.from_dict(componentsschemas_rate_list_item_data)

            eligible_rates.append(componentsschemas_rate_list_item)

        result = cls(
            shipment_id=shipment_id,
            eligible_rates=eligible_rates,
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
