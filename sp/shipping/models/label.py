from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_specification import LabelSpecification


T = TypeVar("T", bound="Label")


@attr.s(auto_attribs=True)
class Label:
    r"""The label details of the container.

    Attributes:
        label_stream (Union[Unset, str]): Contains binary image data encoded as a base-64 string.
        label_specification (Union[Unset, LabelSpecification]): The label specification info.
    """

    label_stream: Union[Unset, str] = UNSET
    label_specification: Union[Unset, "LabelSpecification"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label_stream = self.label_stream
        label_specification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label_specification, Unset):
            label_specification = self.label_specification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label_stream is not UNSET:
            field_dict["labelStream"] = label_stream
        if label_specification is not UNSET:
            field_dict["labelSpecification"] = label_specification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label_specification import LabelSpecification

        d = src_dict.copy()
        label_stream = d.pop("labelStream", UNSET)

        _label_specification = d.pop("labelSpecification", UNSET)
        label_specification: Union[Unset, LabelSpecification]
        if isinstance(_label_specification, Unset):
            label_specification = UNSET
        else:
            label_specification = LabelSpecification.from_dict(_label_specification)

        result = cls(
            label_stream=label_stream,
            label_specification=label_specification,
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
