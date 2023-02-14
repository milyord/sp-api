from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.service_rate import ServiceRate


T = TypeVar("T", bound="GetRatesResult")


@attr.s(auto_attribs=True)
class GetRatesResult:
    r"""The payload schema for the getRates operation.

    Attributes:
        service_rates (List['ServiceRate']): A list of service rates.
    """

    service_rates: List["ServiceRate"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_rates = []
        for componentsschemas_service_rate_list_item_data in self.service_rates:
            componentsschemas_service_rate_list_item = componentsschemas_service_rate_list_item_data.to_dict()

            service_rates.append(componentsschemas_service_rate_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceRates": service_rates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_rate import ServiceRate

        d = src_dict.copy()
        service_rates = []
        _service_rates = d.pop("serviceRates")
        for componentsschemas_service_rate_list_item_data in _service_rates:
            componentsschemas_service_rate_list_item = ServiceRate.from_dict(
                componentsschemas_service_rate_list_item_data
            )

            service_rates.append(componentsschemas_service_rate_list_item)

        result = cls(
            service_rates=service_rates,
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
