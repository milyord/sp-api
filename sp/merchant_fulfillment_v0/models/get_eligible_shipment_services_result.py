from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rejected_shipping_service import RejectedShippingService
    from ..models.shipping_service import ShippingService
    from ..models.temporarily_unavailable_carrier import TemporarilyUnavailableCarrier
    from ..models.terms_and_conditions_not_accepted_carrier import TermsAndConditionsNotAcceptedCarrier


T = TypeVar("T", bound="GetEligibleShipmentServicesResult")


@attr.s(auto_attribs=True)
class GetEligibleShipmentServicesResult:
    r"""The payload for the getEligibleShipmentServices operation.

    Attributes:
        shipping_service_list (List['ShippingService']): A list of shipping services offers.
        rejected_shipping_service_list (Union[Unset, List['RejectedShippingService']]): List of services that were for
            some reason unavailable for this request
        temporarily_unavailable_carrier_list (Union[Unset, List['TemporarilyUnavailableCarrier']]): A list of
            temporarily unavailable carriers.
        terms_and_conditions_not_accepted_carrier_list (Union[Unset, List['TermsAndConditionsNotAcceptedCarrier']]):
            List of carriers whose terms and conditions were not accepted by the seller.
    """

    shipping_service_list: List["ShippingService"]
    rejected_shipping_service_list: Union[Unset, List["RejectedShippingService"]] = UNSET
    temporarily_unavailable_carrier_list: Union[Unset, List["TemporarilyUnavailableCarrier"]] = UNSET
    terms_and_conditions_not_accepted_carrier_list: Union[Unset, List["TermsAndConditionsNotAcceptedCarrier"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_service_list = []
        for componentsschemas_shipping_service_list_item_data in self.shipping_service_list:
            componentsschemas_shipping_service_list_item = componentsschemas_shipping_service_list_item_data.to_dict()

            shipping_service_list.append(componentsschemas_shipping_service_list_item)

        rejected_shipping_service_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rejected_shipping_service_list, Unset):
            rejected_shipping_service_list = []
            for componentsschemas_rejected_shipping_service_list_item_data in self.rejected_shipping_service_list:
                componentsschemas_rejected_shipping_service_list_item = (
                    componentsschemas_rejected_shipping_service_list_item_data.to_dict()
                )

                rejected_shipping_service_list.append(componentsschemas_rejected_shipping_service_list_item)

        temporarily_unavailable_carrier_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.temporarily_unavailable_carrier_list, Unset):
            temporarily_unavailable_carrier_list = []
            for (
                componentsschemas_temporarily_unavailable_carrier_list_item_data
            ) in self.temporarily_unavailable_carrier_list:
                componentsschemas_temporarily_unavailable_carrier_list_item = (
                    componentsschemas_temporarily_unavailable_carrier_list_item_data.to_dict()
                )

                temporarily_unavailable_carrier_list.append(componentsschemas_temporarily_unavailable_carrier_list_item)

        terms_and_conditions_not_accepted_carrier_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.terms_and_conditions_not_accepted_carrier_list, Unset):
            terms_and_conditions_not_accepted_carrier_list = []
            for (
                componentsschemas_terms_and_conditions_not_accepted_carrier_list_item_data
            ) in self.terms_and_conditions_not_accepted_carrier_list:
                componentsschemas_terms_and_conditions_not_accepted_carrier_list_item = (
                    componentsschemas_terms_and_conditions_not_accepted_carrier_list_item_data.to_dict()
                )

                terms_and_conditions_not_accepted_carrier_list.append(
                    componentsschemas_terms_and_conditions_not_accepted_carrier_list_item
                )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShippingServiceList": shipping_service_list,
            }
        )
        if rejected_shipping_service_list is not UNSET:
            field_dict["RejectedShippingServiceList"] = rejected_shipping_service_list
        if temporarily_unavailable_carrier_list is not UNSET:
            field_dict["TemporarilyUnavailableCarrierList"] = temporarily_unavailable_carrier_list
        if terms_and_conditions_not_accepted_carrier_list is not UNSET:
            field_dict["TermsAndConditionsNotAcceptedCarrierList"] = terms_and_conditions_not_accepted_carrier_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rejected_shipping_service import RejectedShippingService
        from ..models.shipping_service import ShippingService
        from ..models.temporarily_unavailable_carrier import TemporarilyUnavailableCarrier
        from ..models.terms_and_conditions_not_accepted_carrier import TermsAndConditionsNotAcceptedCarrier

        d = src_dict.copy()
        shipping_service_list = []
        _shipping_service_list = d.pop("ShippingServiceList")
        for componentsschemas_shipping_service_list_item_data in _shipping_service_list:
            componentsschemas_shipping_service_list_item = ShippingService.from_dict(
                componentsschemas_shipping_service_list_item_data
            )

            shipping_service_list.append(componentsschemas_shipping_service_list_item)

        rejected_shipping_service_list = []
        _rejected_shipping_service_list = d.pop("RejectedShippingServiceList", UNSET)
        for componentsschemas_rejected_shipping_service_list_item_data in _rejected_shipping_service_list or []:
            componentsschemas_rejected_shipping_service_list_item = RejectedShippingService.from_dict(
                componentsschemas_rejected_shipping_service_list_item_data
            )

            rejected_shipping_service_list.append(componentsschemas_rejected_shipping_service_list_item)

        temporarily_unavailable_carrier_list = []
        _temporarily_unavailable_carrier_list = d.pop("TemporarilyUnavailableCarrierList", UNSET)
        for componentsschemas_temporarily_unavailable_carrier_list_item_data in (
            _temporarily_unavailable_carrier_list or []
        ):
            componentsschemas_temporarily_unavailable_carrier_list_item = TemporarilyUnavailableCarrier.from_dict(
                componentsschemas_temporarily_unavailable_carrier_list_item_data
            )

            temporarily_unavailable_carrier_list.append(componentsschemas_temporarily_unavailable_carrier_list_item)

        terms_and_conditions_not_accepted_carrier_list = []
        _terms_and_conditions_not_accepted_carrier_list = d.pop("TermsAndConditionsNotAcceptedCarrierList", UNSET)
        for componentsschemas_terms_and_conditions_not_accepted_carrier_list_item_data in (
            _terms_and_conditions_not_accepted_carrier_list or []
        ):
            componentsschemas_terms_and_conditions_not_accepted_carrier_list_item = (
                TermsAndConditionsNotAcceptedCarrier.from_dict(
                    componentsschemas_terms_and_conditions_not_accepted_carrier_list_item_data
                )
            )

            terms_and_conditions_not_accepted_carrier_list.append(
                componentsschemas_terms_and_conditions_not_accepted_carrier_list_item
            )

        result = cls(
            shipping_service_list=shipping_service_list,
            rejected_shipping_service_list=rejected_shipping_service_list,
            temporarily_unavailable_carrier_list=temporarily_unavailable_carrier_list,
            terms_and_conditions_not_accepted_carrier_list=terms_and_conditions_not_accepted_carrier_list,
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
