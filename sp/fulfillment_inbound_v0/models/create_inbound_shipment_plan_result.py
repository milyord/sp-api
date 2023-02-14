from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_shipment_plan import InboundShipmentPlan


T = TypeVar("T", bound="CreateInboundShipmentPlanResult")


@attr.s(auto_attribs=True)
class CreateInboundShipmentPlanResult:
    r"""
    Attributes:
        inbound_shipment_plans (Union[Unset, List['InboundShipmentPlan']]): A list of inbound shipment plan information
    """

    inbound_shipment_plans: Union[Unset, List["InboundShipmentPlan"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inbound_shipment_plans: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inbound_shipment_plans, Unset):
            inbound_shipment_plans = []
            for componentsschemas_inbound_shipment_plan_list_item_data in self.inbound_shipment_plans:
                componentsschemas_inbound_shipment_plan_list_item = (
                    componentsschemas_inbound_shipment_plan_list_item_data.to_dict()
                )

                inbound_shipment_plans.append(componentsschemas_inbound_shipment_plan_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound_shipment_plans is not UNSET:
            field_dict["InboundShipmentPlans"] = inbound_shipment_plans

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inbound_shipment_plan import InboundShipmentPlan

        d = src_dict.copy()
        inbound_shipment_plans = []
        _inbound_shipment_plans = d.pop("InboundShipmentPlans", UNSET)
        for componentsschemas_inbound_shipment_plan_list_item_data in _inbound_shipment_plans or []:
            componentsschemas_inbound_shipment_plan_list_item = InboundShipmentPlan.from_dict(
                componentsschemas_inbound_shipment_plan_list_item_data
            )

            inbound_shipment_plans.append(componentsschemas_inbound_shipment_plan_list_item)

        result = cls(
            inbound_shipment_plans=inbound_shipment_plans,
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
