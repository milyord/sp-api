from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_acknowledgement import OrderAcknowledgement


T = TypeVar("T", bound="SubmitAcknowledgementRequest")


@attr.s(auto_attribs=True)
class SubmitAcknowledgementRequest:
    r"""The request schema for the submitAcknowledgment operation.

    Attributes:
        acknowledgements (Union[Unset, List['OrderAcknowledgement']]):
    """

    acknowledgements: Union[Unset, List["OrderAcknowledgement"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acknowledgements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acknowledgements, Unset):
            acknowledgements = []
            for acknowledgements_item_data in self.acknowledgements:
                acknowledgements_item = acknowledgements_item_data.to_dict()

                acknowledgements.append(acknowledgements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledgements is not UNSET:
            field_dict["acknowledgements"] = acknowledgements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_acknowledgement import OrderAcknowledgement

        d = src_dict.copy()
        acknowledgements = []
        _acknowledgements = d.pop("acknowledgements", UNSET)
        for acknowledgements_item_data in _acknowledgements or []:
            acknowledgements_item = OrderAcknowledgement.from_dict(acknowledgements_item_data)

            acknowledgements.append(acknowledgements_item)

        result = cls(
            acknowledgements=acknowledgements,
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
