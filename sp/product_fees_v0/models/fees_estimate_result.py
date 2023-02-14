from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fees_estimate import FeesEstimate
    from ..models.fees_estimate_error import FeesEstimateError
    from ..models.fees_estimate_identifier import FeesEstimateIdentifier


T = TypeVar("T", bound="FeesEstimateResult")


@attr.s(auto_attribs=True)
class FeesEstimateResult:
    r"""An item identifier and the estimated fees for the item.

    Attributes:
        status (Union[Unset, str]): The status of the fee request. Possible values: Success, ClientError, ServiceError.
        fees_estimate_identifier (Union[Unset, FeesEstimateIdentifier]): An item identifier, marketplace, time of
            request, and other details that identify an estimate.
        fees_estimate (Union[Unset, FeesEstimate]): The total estimated fees for an item and a list of details.
        error (Union[Unset, FeesEstimateError]): An unexpected error occurred during this operation.
    """

    status: Union[Unset, str] = UNSET
    fees_estimate_identifier: Union[Unset, "FeesEstimateIdentifier"] = UNSET
    fees_estimate: Union[Unset, "FeesEstimate"] = UNSET
    error: Union[Unset, "FeesEstimateError"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        fees_estimate_identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fees_estimate_identifier, Unset):
            fees_estimate_identifier = self.fees_estimate_identifier.to_dict()

        fees_estimate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fees_estimate, Unset):
            fees_estimate = self.fees_estimate.to_dict()

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["Status"] = status
        if fees_estimate_identifier is not UNSET:
            field_dict["FeesEstimateIdentifier"] = fees_estimate_identifier
        if fees_estimate is not UNSET:
            field_dict["FeesEstimate"] = fees_estimate
        if error is not UNSET:
            field_dict["Error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fees_estimate import FeesEstimate
        from ..models.fees_estimate_error import FeesEstimateError
        from ..models.fees_estimate_identifier import FeesEstimateIdentifier

        d = src_dict.copy()
        status = d.pop("Status", UNSET)

        _fees_estimate_identifier = d.pop("FeesEstimateIdentifier", UNSET)
        fees_estimate_identifier: Union[Unset, FeesEstimateIdentifier]
        if isinstance(_fees_estimate_identifier, Unset):
            fees_estimate_identifier = UNSET
        else:
            fees_estimate_identifier = FeesEstimateIdentifier.from_dict(_fees_estimate_identifier)

        _fees_estimate = d.pop("FeesEstimate", UNSET)
        fees_estimate: Union[Unset, FeesEstimate]
        if isinstance(_fees_estimate, Unset):
            fees_estimate = UNSET
        else:
            fees_estimate = FeesEstimate.from_dict(_fees_estimate)

        _error = d.pop("Error", UNSET)
        error: Union[Unset, FeesEstimateError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = FeesEstimateError.from_dict(_error)

        result = cls(
            status=status,
            fees_estimate_identifier=fees_estimate_identifier,
            fees_estimate=fees_estimate,
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
