from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.label_result import LabelResult
    from ..models.service_rate import ServiceRate


T = TypeVar("T", bound="PurchaseShipmentResult")


@attr.s(auto_attribs=True)
class PurchaseShipmentResult:
    r"""The payload schema for the purchaseShipment operation.

    Attributes:
        shipment_id (str): The unique shipment identifier.
        service_rate (ServiceRate): The specific rate for a shipping service, or null if no service available.
        label_results (List['LabelResult']): A list of label results
    """

    shipment_id: str
    service_rate: "ServiceRate"
    label_results: List["LabelResult"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_id = self.shipment_id
        service_rate = self.service_rate.to_dict()

        label_results = []
        for componentsschemas_label_result_list_item_data in self.label_results:
            componentsschemas_label_result_list_item = componentsschemas_label_result_list_item_data.to_dict()

            label_results.append(componentsschemas_label_result_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipmentId": shipment_id,
                "serviceRate": service_rate,
                "labelResults": label_results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label_result import LabelResult
        from ..models.service_rate import ServiceRate

        d = src_dict.copy()
        shipment_id = d.pop("shipmentId")

        service_rate = ServiceRate.from_dict(d.pop("serviceRate"))

        label_results = []
        _label_results = d.pop("labelResults")
        for componentsschemas_label_result_list_item_data in _label_results:
            componentsschemas_label_result_list_item = LabelResult.from_dict(
                componentsschemas_label_result_list_item_data
            )

            label_results.append(componentsschemas_label_result_list_item)

        result = cls(
            shipment_id=shipment_id,
            service_rate=service_rate,
            label_results=label_results,
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
