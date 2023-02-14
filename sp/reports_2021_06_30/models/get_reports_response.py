from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report import Report


T = TypeVar("T", bound="GetReportsResponse")


@attr.s(auto_attribs=True)
class GetReportsResponse:
    r"""The response for the getReports operation.

    Attributes:
        reports (List['Report']): A list of reports.
        next_token (Union[Unset, str]): Returned when the number of results exceeds pageSize. To get the next page of
            results, call getReports with this token as the only parameter.
    """

    reports: List["Report"]
    next_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reports = []
        for componentsschemas_report_list_item_data in self.reports:
            componentsschemas_report_list_item = componentsschemas_report_list_item_data.to_dict()

            reports.append(componentsschemas_report_list_item)

        next_token = self.next_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reports": reports,
            }
        )
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report import Report

        d = src_dict.copy()
        reports = []
        _reports = d.pop("reports")
        for componentsschemas_report_list_item_data in _reports:
            componentsschemas_report_list_item = Report.from_dict(componentsschemas_report_list_item_data)

            reports.append(componentsschemas_report_list_item)

        next_token = d.pop("nextToken", UNSET)

        result = cls(
            reports=reports,
            next_token=next_token,
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
