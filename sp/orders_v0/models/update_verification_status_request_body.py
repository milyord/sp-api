from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.verification_status import VerificationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateVerificationStatusRequestBody")


@attr.s(auto_attribs=True)
class UpdateVerificationStatusRequestBody:
    r"""The updated values of the VerificationStatus field.

    Attributes:
        status (VerificationStatus): The verification status of the order.
        external_reviewer_id (str): The identifier for the order's regulated information reviewer.
        rejection_reason_id (Union[Unset, str]): The unique identifier for the rejection reason used for rejecting the
            order's regulated information. Only required if the new status is rejected.
    """

    status: VerificationStatus
    external_reviewer_id: str
    rejection_reason_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        external_reviewer_id = self.external_reviewer_id
        rejection_reason_id = self.rejection_reason_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "externalReviewerId": external_reviewer_id,
            }
        )
        if rejection_reason_id is not UNSET:
            field_dict["rejectionReasonId"] = rejection_reason_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = VerificationStatus(d.pop("status"))

        external_reviewer_id = d.pop("externalReviewerId")

        rejection_reason_id = d.pop("rejectionReasonId", UNSET)

        result = cls(
            status=status,
            external_reviewer_id=external_reviewer_id,
            rejection_reason_id=rejection_reason_id,
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
