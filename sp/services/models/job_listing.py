from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_job import ServiceJob


T = TypeVar("T", bound="JobListing")


@attr.s(auto_attribs=True)
class JobListing:
    r"""The payload for the `getServiceJobs` operation.

    Attributes:
        total_result_size (Union[Unset, int]): Total result size of the query result.
        next_page_token (Union[Unset, str]): A generated string used to pass information to your next request. If
            `nextPageToken` is returned, pass the value of `nextPageToken` to the `pageToken` to get next results.
        previous_page_token (Union[Unset, str]): A generated string used to pass information to your next request. If
            `previousPageToken` is returned, pass the value of `previousPageToken` to the `pageToken` to get previous page
            results.
        jobs (Union[Unset, List['ServiceJob']]): List of job details for the given input.
    """

    total_result_size: Union[Unset, int] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    previous_page_token: Union[Unset, str] = UNSET
    jobs: Union[Unset, List["ServiceJob"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_result_size = self.total_result_size
        next_page_token = self.next_page_token
        previous_page_token = self.previous_page_token
        jobs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()

                jobs.append(jobs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_result_size is not UNSET:
            field_dict["totalResultSize"] = total_result_size
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if previous_page_token is not UNSET:
            field_dict["previousPageToken"] = previous_page_token
        if jobs is not UNSET:
            field_dict["jobs"] = jobs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_job import ServiceJob

        d = src_dict.copy()
        total_result_size = d.pop("totalResultSize", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        previous_page_token = d.pop("previousPageToken", UNSET)

        jobs = []
        _jobs = d.pop("jobs", UNSET)
        for jobs_item_data in _jobs or []:
            jobs_item = ServiceJob.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        result = cls(
            total_result_size=total_result_size,
            next_page_token=next_page_token,
            previous_page_token=previous_page_token,
            jobs=jobs,
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
