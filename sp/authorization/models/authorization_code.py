from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizationCode")


@attr.s(auto_attribs=True)
class AuthorizationCode:
    r"""A Login with Amazon (LWA) authorization code.

    Attributes:
        authorization_code (Union[Unset, str]): A Login with Amazon (LWA) authorization code that can be exchanged for a
            refresh token and access token that authorize you to make calls to a Selling Partner API.
    """

    authorization_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization_code = self.authorization_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_code is not UNSET:
            field_dict["authorizationCode"] = authorization_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authorization_code = d.pop("authorizationCode", UNSET)

        result = cls(
            authorization_code=authorization_code,
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
