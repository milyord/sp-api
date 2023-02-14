import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_detail import FeeDetail
    from ..models.money_type import MoneyType


T = TypeVar("T", bound="FeesEstimate")


@attr.s(auto_attribs=True)
class FeesEstimate:
    r"""The total estimated fees for an item and a list of details.

    Attributes:
        time_of_fees_estimation (datetime.datetime): The time at which the fees were estimated. This defaults to the
            time the request is made.
        total_fees_estimate (Union[Unset, MoneyType]):
        fee_detail_list (Union[Unset, List['FeeDetail']]): A list of other fees that contribute to a given fee.
    """

    time_of_fees_estimation: datetime.datetime
    total_fees_estimate: Union[Unset, "MoneyType"] = UNSET
    fee_detail_list: Union[Unset, List["FeeDetail"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_of_fees_estimation = self.time_of_fees_estimation.isoformat()

        total_fees_estimate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_fees_estimate, Unset):
            total_fees_estimate = self.total_fees_estimate.to_dict()

        fee_detail_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fee_detail_list, Unset):
            fee_detail_list = []
            for componentsschemas_fee_detail_list_item_data in self.fee_detail_list:
                componentsschemas_fee_detail_list_item = componentsschemas_fee_detail_list_item_data.to_dict()

                fee_detail_list.append(componentsschemas_fee_detail_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TimeOfFeesEstimation": time_of_fees_estimation,
            }
        )
        if total_fees_estimate is not UNSET:
            field_dict["TotalFeesEstimate"] = total_fees_estimate
        if fee_detail_list is not UNSET:
            field_dict["FeeDetailList"] = fee_detail_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fee_detail import FeeDetail
        from ..models.money_type import MoneyType

        d = src_dict.copy()
        time_of_fees_estimation = isoparse(d.pop("TimeOfFeesEstimation"))

        _total_fees_estimate = d.pop("TotalFeesEstimate", UNSET)
        total_fees_estimate: Union[Unset, MoneyType]
        if isinstance(_total_fees_estimate, Unset):
            total_fees_estimate = UNSET
        else:
            total_fees_estimate = MoneyType.from_dict(_total_fees_estimate)

        fee_detail_list = []
        _fee_detail_list = d.pop("FeeDetailList", UNSET)
        for componentsschemas_fee_detail_list_item_data in _fee_detail_list or []:
            componentsschemas_fee_detail_list_item = FeeDetail.from_dict(componentsschemas_fee_detail_list_item_data)

            fee_detail_list.append(componentsschemas_fee_detail_list_item)

        result = cls(
            time_of_fees_estimation=time_of_fees_estimation,
            total_fees_estimate=total_fees_estimate,
            fee_detail_list=fee_detail_list,
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
