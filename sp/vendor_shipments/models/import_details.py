import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.import_details_method_of_payment import ImportDetailsMethodOfPayment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route import Route
    from ..models.weight import Weight


T = TypeVar("T", bound="ImportDetails")


@attr.s(auto_attribs=True)
class ImportDetails:
    r"""
    Attributes:
        method_of_payment (Union[Unset, ImportDetailsMethodOfPayment]): This is used for import purchase orders only. If
            the recipient requests, this field will contain the shipment method of payment.
        seal_number (Union[Unset, str]): The container's seal number.
        route (Union[Unset, Route]): This is used only for direct import shipment confirmations.
        import_containers (Union[Unset, str]): Types and numbers of container(s) for import purchase orders. Can be a
            comma-separated list if shipment has multiple containers.
        billable_weight (Union[Unset, Weight]): The weight.
        estimated_ship_by_date (Union[Unset, datetime.datetime]): Date on which the shipment is expected to be shipped.
            This value should not be in the past and not more than 60 days out in the future.
    """

    method_of_payment: Union[Unset, ImportDetailsMethodOfPayment] = UNSET
    seal_number: Union[Unset, str] = UNSET
    route: Union[Unset, "Route"] = UNSET
    import_containers: Union[Unset, str] = UNSET
    billable_weight: Union[Unset, "Weight"] = UNSET
    estimated_ship_by_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method_of_payment: Union[Unset, str] = UNSET
        if not isinstance(self.method_of_payment, Unset):
            method_of_payment = self.method_of_payment.value

        seal_number = self.seal_number
        route: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.route, Unset):
            route = self.route.to_dict()

        import_containers = self.import_containers
        billable_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billable_weight, Unset):
            billable_weight = self.billable_weight.to_dict()

        estimated_ship_by_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_ship_by_date, Unset):
            estimated_ship_by_date = self.estimated_ship_by_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_of_payment is not UNSET:
            field_dict["methodOfPayment"] = method_of_payment
        if seal_number is not UNSET:
            field_dict["sealNumber"] = seal_number
        if route is not UNSET:
            field_dict["route"] = route
        if import_containers is not UNSET:
            field_dict["importContainers"] = import_containers
        if billable_weight is not UNSET:
            field_dict["billableWeight"] = billable_weight
        if estimated_ship_by_date is not UNSET:
            field_dict["estimatedShipByDate"] = estimated_ship_by_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.route import Route
        from ..models.weight import Weight

        d = src_dict.copy()
        _method_of_payment = d.pop("methodOfPayment", UNSET)
        method_of_payment: Union[Unset, ImportDetailsMethodOfPayment]
        if isinstance(_method_of_payment, Unset):
            method_of_payment = UNSET
        else:
            method_of_payment = ImportDetailsMethodOfPayment(_method_of_payment)

        seal_number = d.pop("sealNumber", UNSET)

        _route = d.pop("route", UNSET)
        route: Union[Unset, Route]
        if isinstance(_route, Unset):
            route = UNSET
        else:
            route = Route.from_dict(_route)

        import_containers = d.pop("importContainers", UNSET)

        _billable_weight = d.pop("billableWeight", UNSET)
        billable_weight: Union[Unset, Weight]
        if isinstance(_billable_weight, Unset):
            billable_weight = UNSET
        else:
            billable_weight = Weight.from_dict(_billable_weight)

        _estimated_ship_by_date = d.pop("estimatedShipByDate", UNSET)
        estimated_ship_by_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_ship_by_date, Unset):
            estimated_ship_by_date = UNSET
        else:
            estimated_ship_by_date = isoparse(_estimated_ship_by_date)

        result = cls(
            method_of_payment=method_of_payment,
            seal_number=seal_number,
            route=route,
            import_containers=import_containers,
            billable_weight=billable_weight,
            estimated_ship_by_date=estimated_ship_by_date,
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
