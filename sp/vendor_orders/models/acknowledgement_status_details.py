import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_quantity import ItemQuantity


T = TypeVar("T", bound="AcknowledgementStatusDetails")


@attr.s(auto_attribs=True)
class AcknowledgementStatusDetails:
    r"""Details of item quantity ordered

    Attributes:
        acknowledgement_date (Union[Unset, datetime.datetime]): The date when the line item was confirmed by vendor.
            Must be in ISO-8601 date/time format.
        accepted_quantity (Union[Unset, ItemQuantity]): Details of quantity ordered.
        rejected_quantity (Union[Unset, ItemQuantity]): Details of quantity ordered.
    """

    acknowledgement_date: Union[Unset, datetime.datetime] = UNSET
    accepted_quantity: Union[Unset, "ItemQuantity"] = UNSET
    rejected_quantity: Union[Unset, "ItemQuantity"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acknowledgement_date: Union[Unset, str] = UNSET
        if not isinstance(self.acknowledgement_date, Unset):
            acknowledgement_date = self.acknowledgement_date.isoformat()

        accepted_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accepted_quantity, Unset):
            accepted_quantity = self.accepted_quantity.to_dict()

        rejected_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rejected_quantity, Unset):
            rejected_quantity = self.rejected_quantity.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledgement_date is not UNSET:
            field_dict["acknowledgementDate"] = acknowledgement_date
        if accepted_quantity is not UNSET:
            field_dict["acceptedQuantity"] = accepted_quantity
        if rejected_quantity is not UNSET:
            field_dict["rejectedQuantity"] = rejected_quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_quantity import ItemQuantity

        d = src_dict.copy()
        _acknowledgement_date = d.pop("acknowledgementDate", UNSET)
        acknowledgement_date: Union[Unset, datetime.datetime]
        if isinstance(_acknowledgement_date, Unset):
            acknowledgement_date = UNSET
        else:
            acknowledgement_date = isoparse(_acknowledgement_date)

        _accepted_quantity = d.pop("acceptedQuantity", UNSET)
        accepted_quantity: Union[Unset, ItemQuantity]
        if isinstance(_accepted_quantity, Unset):
            accepted_quantity = UNSET
        else:
            accepted_quantity = ItemQuantity.from_dict(_accepted_quantity)

        _rejected_quantity = d.pop("rejectedQuantity", UNSET)
        rejected_quantity: Union[Unset, ItemQuantity]
        if isinstance(_rejected_quantity, Unset):
            rejected_quantity = UNSET
        else:
            rejected_quantity = ItemQuantity.from_dict(_rejected_quantity)

        result = cls(
            acknowledgement_date=acknowledgement_date,
            accepted_quantity=accepted_quantity,
            rejected_quantity=rejected_quantity,
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
