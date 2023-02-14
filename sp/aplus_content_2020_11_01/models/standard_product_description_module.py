from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.paragraph_component import ParagraphComponent


T = TypeVar("T", bound="StandardProductDescriptionModule")


@attr.s(auto_attribs=True)
class StandardProductDescriptionModule:
    r"""Standard product description text.

    Attributes:
        body (ParagraphComponent): A list of rich text content, usually presented in a text box.
    """

    body: "ParagraphComponent"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.paragraph_component import ParagraphComponent

        d = src_dict.copy()
        body = ParagraphComponent.from_dict(d.pop("body"))

        result = cls(
            body=body,
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
