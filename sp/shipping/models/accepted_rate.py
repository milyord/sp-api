from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.service_type import ServiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.shipping_promise_set import ShippingPromiseSet
    from ..models.weight import Weight


T = TypeVar("T", bound="AcceptedRate")


@attr.s(auto_attribs=True)
class AcceptedRate:
    r"""The specific rate purchased for the shipment, or null if unpurchased.

    Attributes:
        total_charge (Union[Unset, Currency]): The total value of all items in the container.
        billed_weight (Union[Unset, Weight]): The weight.
        service_type (Union[Unset, ServiceType]): The type of shipping service that will be used for the service
            offering.
        promise (Union[Unset, ShippingPromiseSet]): The promised delivery time and pickup time.
    """

    total_charge: Union[Unset, "Currency"] = UNSET
    billed_weight: Union[Unset, "Weight"] = UNSET
    service_type: Union[Unset, ServiceType] = UNSET
    promise: Union[Unset, "ShippingPromiseSet"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_charge: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_charge, Unset):
            total_charge = self.total_charge.to_dict()

        billed_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billed_weight, Unset):
            billed_weight = self.billed_weight.to_dict()

        service_type: Union[Unset, str] = UNSET
        if not isinstance(self.service_type, Unset):
            service_type = self.service_type.value

        promise: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promise, Unset):
            promise = self.promise.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_charge is not UNSET:
            field_dict["totalCharge"] = total_charge
        if billed_weight is not UNSET:
            field_dict["billedWeight"] = billed_weight
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if promise is not UNSET:
            field_dict["promise"] = promise

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.shipping_promise_set import ShippingPromiseSet
        from ..models.weight import Weight

        d = src_dict.copy()
        _total_charge = d.pop("totalCharge", UNSET)
        total_charge: Union[Unset, Currency]
        if isinstance(_total_charge, Unset):
            total_charge = UNSET
        else:
            total_charge = Currency.from_dict(_total_charge)

        _billed_weight = d.pop("billedWeight", UNSET)
        billed_weight: Union[Unset, Weight]
        if isinstance(_billed_weight, Unset):
            billed_weight = UNSET
        else:
            billed_weight = Weight.from_dict(_billed_weight)

        _service_type = d.pop("serviceType", UNSET)
        service_type: Union[Unset, ServiceType]
        if isinstance(_service_type, Unset):
            service_type = UNSET
        else:
            service_type = ServiceType(_service_type)

        _promise = d.pop("promise", UNSET)
        promise: Union[Unset, ShippingPromiseSet]
        if isinstance(_promise, Unset):
            promise = UNSET
        else:
            promise = ShippingPromiseSet.from_dict(_promise)

        result = cls(
            total_charge=total_charge,
            billed_weight=billed_weight,
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
