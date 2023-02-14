from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Buyer")


@attr.s(auto_attribs=True)
class Buyer:
    r"""Information about the buyer.

    Attributes:
        buyer_id (Union[Unset, str]): The identifier of the buyer.
        name (Union[Unset, str]): The name of the buyer.
        phone (Union[Unset, str]): The phone number of the buyer.
        is_prime_member (Union[Unset, bool]): When true, the service is for an Amazon Prime buyer.
    """

    buyer_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    is_prime_member: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        buyer_id = self.buyer_id
        name = self.name
        phone = self.phone
        is_prime_member = self.is_prime_member

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buyer_id is not UNSET:
            field_dict["buyerId"] = buyer_id
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if is_prime_member is not UNSET:
            field_dict["isPrimeMember"] = is_prime_member

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        buyer_id = d.pop("buyerId", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        is_prime_member = d.pop("isPrimeMember", UNSET)

        result = cls(
            buyer_id=buyer_id,
            name=name,
            phone=phone,
            is_prime_member=is_prime_member,
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
