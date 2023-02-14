from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScopeOfWork")


@attr.s(auto_attribs=True)
class ScopeOfWork:
    r"""The scope of work for the order.

    Attributes:
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the service job.
        title (Union[Unset, str]): The title of the service job.
        quantity (Union[Unset, int]): The number of service jobs.
        required_skills (Union[Unset, List[str]]): A list of skills required to perform the job.
    """

    asin: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    required_skills: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        title = self.title
        quantity = self.quantity
        required_skills: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_skills, Unset):
            required_skills = self.required_skills

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asin is not UNSET:
            field_dict["asin"] = asin
        if title is not UNSET:
            field_dict["title"] = title
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if required_skills is not UNSET:
            field_dict["requiredSkills"] = required_skills

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asin = d.pop("asin", UNSET)

        title = d.pop("title", UNSET)

        quantity = d.pop("quantity", UNSET)

        required_skills = cast(List[str], d.pop("requiredSkills", UNSET))

        result = cls(
            asin=asin,
            title=title,
            quantity=quantity,
            required_skills=required_skills,
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
