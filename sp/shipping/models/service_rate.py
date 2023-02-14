from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.service_type import ServiceType

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.shipping_promise_set import ShippingPromiseSet
    from ..models.weight import Weight


T = TypeVar("T", bound="ServiceRate")


@attr.s(auto_attribs=True)
class ServiceRate:
    r"""The specific rate for a shipping service, or null if no service available.

    Attributes:
        total_charge (Currency): The total value of all items in the container.
        billable_weight (Weight): The weight.
        service_type (ServiceType): The type of shipping service that will be used for the service offering.
        promise (ShippingPromiseSet): The promised delivery time and pickup time.
    """

    total_charge: "Currency"
    billable_weight: "Weight"
    service_type: ServiceType
    promise: "ShippingPromiseSet"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_charge = self.total_charge.to_dict()

        billable_weight = self.billable_weight.to_dict()

        service_type = self.service_type.value

        promise = self.promise.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCharge": total_charge,
                "billableWeight": billable_weight,
                "serviceType": service_type,
                "promise": promise,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.shipping_promise_set import ShippingPromiseSet
        from ..models.weight import Weight

        d = src_dict.copy()
        total_charge = Currency.from_dict(d.pop("totalCharge"))

        billable_weight = Weight.from_dict(d.pop("billableWeight"))

        service_type = ServiceType(d.pop("serviceType"))

        promise = ShippingPromiseSet.from_dict(d.pop("promise"))

        result = cls(
            total_charge=total_charge,
            billable_weight=billable_weight,
            service_type=service_type,
            promise=promise,
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
