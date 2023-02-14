from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment_resource import AppointmentResource
    from ..models.fulfillment_document import FulfillmentDocument
    from ..models.fulfillment_time import FulfillmentTime


T = TypeVar("T", bound="SetAppointmentFulfillmentDataRequest")


@attr.s(auto_attribs=True)
class SetAppointmentFulfillmentDataRequest:
    r"""Input for set appointment fulfillment data operation.

    Attributes:
        fulfillment_time (Union[Unset, FulfillmentTime]): Input for fulfillment time details
        appointment_resources (Union[Unset, List['AppointmentResource']]): List of resources that performs or performed
            job appointment fulfillment.
        fulfillment_documents (Union[Unset, List['FulfillmentDocument']]): List of documents captured during service
            appointment fulfillment.
    """

    fulfillment_time: Union[Unset, "FulfillmentTime"] = UNSET
    appointment_resources: Union[Unset, List["AppointmentResource"]] = UNSET
    fulfillment_documents: Union[Unset, List["FulfillmentDocument"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fulfillment_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fulfillment_time, Unset):
            fulfillment_time = self.fulfillment_time.to_dict()

        appointment_resources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.appointment_resources, Unset):
            appointment_resources = []
            for componentsschemas_appointment_resources_item_data in self.appointment_resources:
                componentsschemas_appointment_resources_item = (
                    componentsschemas_appointment_resources_item_data.to_dict()
                )

                appointment_resources.append(componentsschemas_appointment_resources_item)

        fulfillment_documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulfillment_documents, Unset):
            fulfillment_documents = []
            for componentsschemas_fulfillment_documents_item_data in self.fulfillment_documents:
                componentsschemas_fulfillment_documents_item = (
                    componentsschemas_fulfillment_documents_item_data.to_dict()
                )

                fulfillment_documents.append(componentsschemas_fulfillment_documents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fulfillment_time is not UNSET:
            field_dict["fulfillmentTime"] = fulfillment_time
        if appointment_resources is not UNSET:
            field_dict["appointmentResources"] = appointment_resources
        if fulfillment_documents is not UNSET:
            field_dict["fulfillmentDocuments"] = fulfillment_documents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_resource import AppointmentResource
        from ..models.fulfillment_document import FulfillmentDocument
        from ..models.fulfillment_time import FulfillmentTime

        d = src_dict.copy()
        _fulfillment_time = d.pop("fulfillmentTime", UNSET)
        fulfillment_time: Union[Unset, FulfillmentTime]
        if isinstance(_fulfillment_time, Unset):
            fulfillment_time = UNSET
        else:
            fulfillment_time = FulfillmentTime.from_dict(_fulfillment_time)

        appointment_resources = []
        _appointment_resources = d.pop("appointmentResources", UNSET)
        for componentsschemas_appointment_resources_item_data in _appointment_resources or []:
            componentsschemas_appointment_resources_item = AppointmentResource.from_dict(
                componentsschemas_appointment_resources_item_data
            )

            appointment_resources.append(componentsschemas_appointment_resources_item)

        fulfillment_documents = []
        _fulfillment_documents = d.pop("fulfillmentDocuments", UNSET)
        for componentsschemas_fulfillment_documents_item_data in _fulfillment_documents or []:
            componentsschemas_fulfillment_documents_item = FulfillmentDocument.from_dict(
                componentsschemas_fulfillment_documents_item_data
            )

            fulfillment_documents.append(componentsschemas_fulfillment_documents_item)

        result = cls(
            fulfillment_time=fulfillment_time,
            appointment_resources=appointment_resources,
            fulfillment_documents=fulfillment_documents,
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
