from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reason_reason_code import ReasonReasonCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="Reason")


@attr.s(auto_attribs=True)
class Reason:
    r"""A reason for the restriction, including path forward links that may allow Selling Partners to remove the
    restriction, if available.

        Attributes:
            message (str): A message describing the reason for the restriction.
            reason_code (Union[Unset, ReasonReasonCode]): A code indicating why the listing is restricted.
            links (Union[Unset, List['Link']]): A list of path forward links that may allow Selling Partners to remove the
                restriction.
    """

    message: str
    reason_code: Union[Unset, ReasonReasonCode] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        reason_code: Union[Unset, str] = UNSET
        if not isinstance(self.reason_code, Unset):
            reason_code = self.reason_code.value

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()

                links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if reason_code is not UNSET:
            field_dict["reasonCode"] = reason_code
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        message = d.pop("message")

        _reason_code = d.pop("reasonCode", UNSET)
        reason_code: Union[Unset, ReasonReasonCode]
        if isinstance(_reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = ReasonReasonCode(_reason_code)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        result = cls(
            message=message,
            reason_code=reason_code,
            links=links,
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
