from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyerCustomizedInfoDetail")


@attr.s(auto_attribs=True)
class BuyerCustomizedInfoDetail:
    r"""Buyer information for custom orders from the Amazon Custom program.

    Attributes:
        customized_url (Union[Unset, str]): The location of a zip file containing Amazon Custom data.
    """

    customized_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customized_url = self.customized_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customized_url is not UNSET:
            field_dict["CustomizedURL"] = customized_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customized_url = d.pop("CustomizedURL", UNSET)

        result = cls(
            customized_url=customized_url,
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
