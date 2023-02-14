from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.id_type import IdType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fees_estimate_request import FeesEstimateRequest


T = TypeVar("T", bound="FeesEstimateByIdRequest")


@attr.s(auto_attribs=True)
class FeesEstimateByIdRequest:
    r"""A product, marketplace, and proposed price used to request estimated fees.

    Attributes:
        id_type (IdType): The type of product identifier used in a `FeesEstimateByIdRequest`.
        id_value (str): The item identifier.
        fees_estimate_request (Union[Unset, FeesEstimateRequest]):
    """

    id_type: IdType
    id_value: str
    fees_estimate_request: Union[Unset, "FeesEstimateRequest"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_type = self.id_type.value

        id_value = self.id_value
        fees_estimate_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fees_estimate_request, Unset):
            fees_estimate_request = self.fees_estimate_request.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "IdType": id_type,
                "IdValue": id_value,
            }
        )
        if fees_estimate_request is not UNSET:
            field_dict["FeesEstimateRequest"] = fees_estimate_request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fees_estimate_request import FeesEstimateRequest

        d = src_dict.copy()
        id_type = IdType(d.pop("IdType"))

        id_value = d.pop("IdValue")

        _fees_estimate_request = d.pop("FeesEstimateRequest", UNSET)
        fees_estimate_request: Union[Unset, FeesEstimateRequest]
        if isinstance(_fees_estimate_request, Unset):
            fees_estimate_request = UNSET
        else:
            fees_estimate_request = FeesEstimateRequest.from_dict(_fees_estimate_request)

        result = cls(
            id_type=id_type,
            id_value=id_value,
            fees_estimate_request=fees_estimate_request,
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
