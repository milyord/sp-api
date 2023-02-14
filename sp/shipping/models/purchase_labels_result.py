from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accepted_rate import AcceptedRate
    from ..models.label_result import LabelResult


T = TypeVar("T", bound="PurchaseLabelsResult")


@attr.s(auto_attribs=True)
class PurchaseLabelsResult:
    r"""The payload schema for the purchaseLabels operation.

    Attributes:
        shipment_id (str): The unique shipment identifier.
        accepted_rate (AcceptedRate): The specific rate purchased for the shipment, or null if unpurchased.
        label_results (List['LabelResult']): A list of label results
        client_reference_id (Union[Unset, str]): Client reference id.
    """

    shipment_id: str
    accepted_rate: "AcceptedRate"
    label_results: List["LabelResult"]
    client_reference_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_id = self.shipment_id
        accepted_rate = self.accepted_rate.to_dict()

        label_results = []
        for componentsschemas_label_result_list_item_data in self.label_results:
            componentsschemas_label_result_list_item = componentsschemas_label_result_list_item_data.to_dict()

            label_results.append(componentsschemas_label_result_list_item)

        client_reference_id = self.client_reference_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipmentId": shipment_id,
                "acceptedRate": accepted_rate,
                "labelResults": label_results,
            }
        )
        if client_reference_id is not UNSET:
            field_dict["clientReferenceId"] = client_reference_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.accepted_rate import AcceptedRate
        from ..models.label_result import LabelResult

        d = src_dict.copy()
        shipment_id = d.pop("shipmentId")

        accepted_rate = AcceptedRate.from_dict(d.pop("acceptedRate"))

        label_results = []
        _label_results = d.pop("labelResults")
        for componentsschemas_label_result_list_item_data in _label_results:
            componentsschemas_label_result_list_item = LabelResult.from_dict(
                componentsschemas_label_result_list_item_data
            )

            label_results.append(componentsschemas_label_result_list_item)

        client_reference_id = d.pop("clientReferenceId", UNSET)

        result = cls(
            shipment_id=shipment_id,
            accepted_rate=accepted_rate,
            label_results=label_results,
            client_reference_id=client_reference_id,
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
