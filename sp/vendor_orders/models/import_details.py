from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.import_details_international_commercial_terms import ImportDetailsInternationalCommercialTerms
from ..models.import_details_method_of_payment import ImportDetailsMethodOfPayment
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportDetails")


@attr.s(auto_attribs=True)
class ImportDetails:
    r"""Import details for an import order.

    Attributes:
        method_of_payment (Union[Unset, ImportDetailsMethodOfPayment]): If the recipient requests, contains the shipment
            method of payment. This is for import PO's only.
        international_commercial_terms (Union[Unset, ImportDetailsInternationalCommercialTerms]): Incoterms
            (International Commercial Terms) are used to divide transaction costs and responsibilities between buyer and
            seller and reflect state-of-the-art transportation practices. This is for import purchase orders only.
        port_of_delivery (Union[Unset, str]): The port where goods on an import purchase order must be delivered by the
            vendor. This should only be specified when the internationalCommercialTerms is FOB.
        import_containers (Union[Unset, str]): Types and numbers of container(s) for import purchase orders. Can be a
            comma-separated list if the shipment has multiple containers. HC signifies a high-capacity container. Free-text
            field, limited to 64 characters. The format will be a comma-delimited list containing values of the type:
            $NUMBER_OF_CONTAINERS_OF_THIS_TYPE-$CONTAINER_TYPE. The list of values for the container type is: 40'(40-foot
            container), 40'HC (40-foot high-capacity container), 45', 45'HC, 30', 30'HC, 20', 20'HC.
        shipping_instructions (Union[Unset, str]): Special instructions regarding the shipment. This field is for import
            purchase orders.
    """

    method_of_payment: Union[Unset, ImportDetailsMethodOfPayment] = UNSET
    international_commercial_terms: Union[Unset, ImportDetailsInternationalCommercialTerms] = UNSET
    port_of_delivery: Union[Unset, str] = UNSET
    import_containers: Union[Unset, str] = UNSET
    shipping_instructions: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method_of_payment: Union[Unset, str] = UNSET
        if not isinstance(self.method_of_payment, Unset):
            method_of_payment = self.method_of_payment.value

        international_commercial_terms: Union[Unset, str] = UNSET
        if not isinstance(self.international_commercial_terms, Unset):
            international_commercial_terms = self.international_commercial_terms.value

        port_of_delivery = self.port_of_delivery
        import_containers = self.import_containers
        shipping_instructions = self.shipping_instructions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_of_payment is not UNSET:
            field_dict["methodOfPayment"] = method_of_payment
        if international_commercial_terms is not UNSET:
            field_dict["internationalCommercialTerms"] = international_commercial_terms
        if port_of_delivery is not UNSET:
            field_dict["portOfDelivery"] = port_of_delivery
        if import_containers is not UNSET:
            field_dict["importContainers"] = import_containers
        if shipping_instructions is not UNSET:
            field_dict["shippingInstructions"] = shipping_instructions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _method_of_payment = d.pop("methodOfPayment", UNSET)
        method_of_payment: Union[Unset, ImportDetailsMethodOfPayment]
        if isinstance(_method_of_payment, Unset):
            method_of_payment = UNSET
        else:
            method_of_payment = ImportDetailsMethodOfPayment(_method_of_payment)

        _international_commercial_terms = d.pop("internationalCommercialTerms", UNSET)
        international_commercial_terms: Union[Unset, ImportDetailsInternationalCommercialTerms]
        if isinstance(_international_commercial_terms, Unset):
            international_commercial_terms = UNSET
        else:
            international_commercial_terms = ImportDetailsInternationalCommercialTerms(_international_commercial_terms)

        port_of_delivery = d.pop("portOfDelivery", UNSET)

        import_containers = d.pop("importContainers", UNSET)

        shipping_instructions = d.pop("shippingInstructions", UNSET)

        result = cls(
            method_of_payment=method_of_payment,
            international_commercial_terms=international_commercial_terms,
            port_of_delivery=port_of_delivery,
            import_containers=import_containers,
            shipping_instructions=shipping_instructions,
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
