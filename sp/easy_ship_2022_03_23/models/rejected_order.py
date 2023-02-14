from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error


T = TypeVar("T", bound="RejectedOrder")


@attr.s(auto_attribs=True)
class RejectedOrder:
    r"""A order which we couldn't schedule on your behalf. It contains its id, and information on the error.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier. Identifies the order that the seller wants to deliver
            using Amazon Easy Ship.
        error (Union[Unset, Error]): Error response returned when the request is unsuccessful.
    """

    amazon_order_id: str
    error: Union[Unset, "Error"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amazonOrderId": amazon_order_id,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error

        d = src_dict.copy()
        amazon_order_id = d.pop("amazonOrderId")

        _error = d.pop("error", UNSET)
        error: Union[Unset, Error]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = Error.from_dict(_error)

        result = cls(
            amazon_order_id=amazon_order_id,
            error=error,
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
