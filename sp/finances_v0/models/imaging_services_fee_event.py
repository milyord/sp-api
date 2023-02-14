import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_component import FeeComponent


T = TypeVar("T", bound="ImagingServicesFeeEvent")


@attr.s(auto_attribs=True)
class ImagingServicesFeeEvent:
    r"""A fee event related to Amazon Imaging services.

    Attributes:
        imaging_request_billing_item_id (Union[Unset, str]): The identifier for the imaging services request.
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item for which the imaging
            service was requested.
        posted_date (Union[Unset, datetime.datetime]):
        fee_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
    """

    imaging_request_billing_item_id: Union[Unset, str] = UNSET
    asin: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    fee_list: Union[Unset, List["FeeComponent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        imaging_request_billing_item_id = self.imaging_request_billing_item_id
        asin = self.asin
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        fee_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fee_list, Unset):
            fee_list = []
            for componentsschemas_fee_component_list_item_data in self.fee_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                fee_list.append(componentsschemas_fee_component_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if imaging_request_billing_item_id is not UNSET:
            field_dict["ImagingRequestBillingItemID"] = imaging_request_billing_item_id
        if asin is not UNSET:
            field_dict["ASIN"] = asin
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if fee_list is not UNSET:
            field_dict["FeeList"] = fee_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fee_component import FeeComponent

        d = src_dict.copy()
        imaging_request_billing_item_id = d.pop("ImagingRequestBillingItemID", UNSET)

        asin = d.pop("ASIN", UNSET)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        fee_list = []
        _fee_list = d.pop("FeeList", UNSET)
        for componentsschemas_fee_component_list_item_data in _fee_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            fee_list.append(componentsschemas_fee_component_list_item)

        result = cls(
            imaging_request_billing_item_id=imaging_request_billing_item_id,
            asin=asin,
            posted_date=posted_date,
            fee_list=fee_list,
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
