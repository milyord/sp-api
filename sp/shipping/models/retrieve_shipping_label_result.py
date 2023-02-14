from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.label_specification import LabelSpecification


T = TypeVar("T", bound="RetrieveShippingLabelResult")


@attr.s(auto_attribs=True)
class RetrieveShippingLabelResult:
    r"""The payload schema for the retrieveShippingLabel operation.

    Attributes:
        label_stream (str): Contains binary image data encoded as a base-64 string.
        label_specification (LabelSpecification): The label specification info.
    """

    label_stream: str
    label_specification: "LabelSpecification"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label_stream = self.label_stream
        label_specification = self.label_specification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labelStream": label_stream,
                "labelSpecification": label_specification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label_specification import LabelSpecification

        d = src_dict.copy()
        label_stream = d.pop("labelStream")

        label_specification = LabelSpecification.from_dict(d.pop("labelSpecification"))

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
