from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.label_format import LabelFormat

if TYPE_CHECKING:
    from ..models.order_schedule_details import OrderScheduleDetails


T = TypeVar("T", bound="CreateScheduledPackagesRequest")


@attr.s(auto_attribs=True)
class CreateScheduledPackagesRequest:
    r"""The request body for the POST /easyShip/2022-03-23/packages/bulk API.

    Attributes:
        marketplace_id (str): A string of up to 255 characters.
        order_schedule_details_list (List['OrderScheduleDetails']): An array allowing users to specify orders to be
            scheduled.
        label_format (LabelFormat): The file format in which the shipping label will be created.
    """

    marketplace_id: str
    order_schedule_details_list: List["OrderScheduleDetails"]
    label_format: LabelFormat
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        order_schedule_details_list = []
        for order_schedule_details_list_item_data in self.order_schedule_details_list:
            order_schedule_details_list_item = order_schedule_details_list_item_data.to_dict()

            order_schedule_details_list.append(order_schedule_details_list_item)

        label_format = self.label_format.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "orderScheduleDetailsList": order_schedule_details_list,
                "labelFormat": label_format,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_schedule_details import OrderScheduleDetails

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        order_schedule_details_list = []
        _order_schedule_details_list = d.pop("orderScheduleDetailsList")
        for order_schedule_details_list_item_data in _order_schedule_details_list:
            order_schedule_details_list_item = OrderScheduleDetails.from_dict(order_schedule_details_list_item_data)

            order_schedule_details_list.append(order_schedule_details_list_item)

        label_format = LabelFormat(d.pop("labelFormat"))

        result = cls(
            marketplace_id=marketplace_id,
            order_schedule_details_list=order_schedule_details_list,
            label_format=label_format,
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
