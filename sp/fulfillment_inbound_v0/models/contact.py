from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Contact")


@attr.s(auto_attribs=True)
class Contact:
    r"""Contact information for the person in the seller's organization who is responsible for a Less Than Truckload/Full
    Truckload (LTL/FTL) shipment.

        Attributes:
            name (str): The name of the contact person.
            phone (str): The phone number of the contact person.
            email (str): The email address of the contact person.
            fax (Union[Unset, str]): The fax number of the contact person.
    """

    name: str
    phone: str
    email: str
    fax: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        phone = self.phone
        email = self.email
        fax = self.fax

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
                "Phone": phone,
                "Email": email,
            }
        )
        if fax is not UNSET:
            field_dict["Fax"] = fax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        phone = d.pop("Phone")

        email = d.pop("Email")

        fax = d.pop("Fax", UNSET)

        result = cls(
            name=name,
            phone=phone,
            email=email,
            fax=fax,
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
