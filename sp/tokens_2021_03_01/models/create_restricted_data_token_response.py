from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRestrictedDataTokenResponse")


@attr.s(auto_attribs=True)
class CreateRestrictedDataTokenResponse:
    r"""The response schema for the createRestrictedDataToken operation.

    Attributes:
        restricted_data_token (Union[Unset, str]): A Restricted Data Token (RDT). This is a short-lived access token
            that authorizes calls to restricted operations. Pass this value with the x-amz-access-token header when making
            subsequent calls to these restricted resources.
        expires_in (Union[Unset, int]): The lifetime of the Restricted Data Token, in seconds.
    """

    restricted_data_token: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        restricted_data_token = self.restricted_data_token
        expires_in = self.expires_in

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restricted_data_token is not UNSET:
            field_dict["restrictedDataToken"] = restricted_data_token
        if expires_in is not UNSET:
            field_dict["expiresIn"] = expires_in

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        restricted_data_token = d.pop("restrictedDataToken", UNSET)

        expires_in = d.pop("expiresIn", UNSET)

        result = cls(
            restricted_data_token=restricted_data_token,
            expires_in=expires_in,
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
