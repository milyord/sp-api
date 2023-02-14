from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.listings_item_submission_response_status import ListingsItemSubmissionResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue import Issue


T = TypeVar("T", bound="ListingsItemSubmissionResponse")


@attr.s(auto_attribs=True)
class ListingsItemSubmissionResponse:
    r"""Response containing the results of a submission to the Selling Partner API for Listings Items.

    Attributes:
        sku (str): A selling partner provided identifier for an Amazon listing.
        status (ListingsItemSubmissionResponseStatus): The status of the listings item submission.
        submission_id (str): The unique identifier of the listings item submission.
        issues (Union[Unset, List['Issue']]): Listings item issues related to the listings item submission.
    """

    sku: str
    status: ListingsItemSubmissionResponseStatus
    submission_id: str
    issues: Union[Unset, List["Issue"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku = self.sku
        status = self.status.value

        submission_id = self.submission_id
        issues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()

                issues.append(issues_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sku": sku,
                "status": status,
                "submissionId": submission_id,
            }
        )
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue import Issue

        d = src_dict.copy()
        sku = d.pop("sku")

        status = ListingsItemSubmissionResponseStatus(d.pop("status"))

        submission_id = d.pop("submissionId")

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = Issue.from_dict(issues_item_data)

            issues.append(issues_item)

        result = cls(
            sku=sku,
            status=status,
            submission_id=submission_id,
            issues=issues,
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
