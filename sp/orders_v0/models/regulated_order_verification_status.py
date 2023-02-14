from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.verification_status import VerificationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rejection_reason import RejectionReason


T = TypeVar("T", bound="RegulatedOrderVerificationStatus")


@attr.s(auto_attribs=True)
class RegulatedOrderVerificationStatus:
    r"""The verification status of the order along with associated approval or rejection metadata.

    Attributes:
        status (VerificationStatus): The verification status of the order.
        requires_merchant_action (bool): When true, the regulated information provided in the order requires a review by
            the merchant.
        valid_rejection_reasons (List['RejectionReason']): A list of valid rejection reasons that may be used to reject
            the order's regulated information.
        rejection_reason (Union[Unset, RejectionReason]): The reason for rejecting the order's regulated information.
            Not present if the order isn't rejected.
        review_date (Union[Unset, str]): The date the order was reviewed. In ISO 8601 date time format.
        external_reviewer_id (Union[Unset, str]): The identifier for the order's regulated information reviewer.
    """

    status: VerificationStatus
    requires_merchant_action: bool
    valid_rejection_reasons: List["RejectionReason"]
    rejection_reason: Union[Unset, "RejectionReason"] = UNSET
    review_date: Union[Unset, str] = UNSET
    external_reviewer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        requires_merchant_action = self.requires_merchant_action
        valid_rejection_reasons = []
        for valid_rejection_reasons_item_data in self.valid_rejection_reasons:
            valid_rejection_reasons_item = valid_rejection_reasons_item_data.to_dict()

            valid_rejection_reasons.append(valid_rejection_reasons_item)

        rejection_reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rejection_reason, Unset):
            rejection_reason = self.rejection_reason.to_dict()

        review_date = self.review_date
        external_reviewer_id = self.external_reviewer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Status": status,
                "RequiresMerchantAction": requires_merchant_action,
                "ValidRejectionReasons": valid_rejection_reasons,
            }
        )
        if rejection_reason is not UNSET:
            field_dict["RejectionReason"] = rejection_reason
        if review_date is not UNSET:
            field_dict["ReviewDate"] = review_date
        if external_reviewer_id is not UNSET:
            field_dict["ExternalReviewerId"] = external_reviewer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rejection_reason import RejectionReason

        d = src_dict.copy()
        status = VerificationStatus(d.pop("Status"))

        requires_merchant_action = d.pop("RequiresMerchantAction")

        valid_rejection_reasons = []
        _valid_rejection_reasons = d.pop("ValidRejectionReasons")
        for valid_rejection_reasons_item_data in _valid_rejection_reasons:
            valid_rejection_reasons_item = RejectionReason.from_dict(valid_rejection_reasons_item_data)

            valid_rejection_reasons.append(valid_rejection_reasons_item)

        _rejection_reason = d.pop("RejectionReason", UNSET)
        rejection_reason: Union[Unset, RejectionReason]
        if isinstance(_rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = RejectionReason.from_dict(_rejection_reason)

        review_date = d.pop("ReviewDate", UNSET)

        external_reviewer_id = d.pop("ExternalReviewerId", UNSET)

        result = cls(
            status=status,
            requires_merchant_action=requires_merchant_action,
            valid_rejection_reasons=valid_rejection_reasons,
            rejection_reason=rejection_reason,
            review_date=review_date,
            external_reviewer_id=external_reviewer_id,
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
