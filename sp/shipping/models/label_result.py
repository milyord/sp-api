from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label import Label


T = TypeVar("T", bound="LabelResult")


@attr.s(auto_attribs=True)
class LabelResult:
    r"""Label details including label stream, format, size.

    Attributes:
        container_reference_id (Union[Unset, str]): An identifier for the container. This must be unique within all the
            containers in the same shipment.
        tracking_id (Union[Unset, str]): The tracking identifier assigned to the container.
        label (Union[Unset, Label]): The label details of the container.
    """

    container_reference_id: Union[Unset, str] = UNSET
    tracking_id: Union[Unset, str] = UNSET
    label: Union[Unset, "Label"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container_reference_id = self.container_reference_id
        tracking_id = self.tracking_id
        label: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_reference_id is not UNSET:
            field_dict["containerReferenceId"] = container_reference_id
        if tracking_id is not UNSET:
            field_dict["trackingId"] = tracking_id
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label import Label

        d = src_dict.copy()
        container_reference_id = d.pop("containerReferenceId", UNSET)

        tracking_id = d.pop("trackingId", UNSET)

        _label = d.pop("label", UNSET)
        label: Union[Unset, Label]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = Label.from_dict(_label)

        result = cls(
            container_reference_id=container_reference_id,
            tracking_id=tracking_id,
            label=label,
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
