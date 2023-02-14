import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="Expiry")


@attr.s(auto_attribs=True)
class Expiry:
    r"""
    Attributes:
        manufacturer_date (Union[Unset, datetime.datetime]): Production, packaging or assembly date determined by the
            manufacturer. Its meaning is determined based on the trade item context.
        expiry_date (Union[Unset, datetime.datetime]): The date that determines the limit of consumption or use of a
            product. Its meaning is determined based on the trade item context.
        expiry_after_duration (Union[Unset, Duration]):
    """

    manufacturer_date: Union[Unset, datetime.datetime] = UNSET
    expiry_date: Union[Unset, datetime.datetime] = UNSET
    expiry_after_duration: Union[Unset, "Duration"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        manufacturer_date: Union[Unset, str] = UNSET
        if not isinstance(self.manufacturer_date, Unset):
            manufacturer_date = self.manufacturer_date.isoformat()

        expiry_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat()

        expiry_after_duration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expiry_after_duration, Unset):
            expiry_after_duration = self.expiry_after_duration.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if manufacturer_date is not UNSET:
            field_dict["manufacturerDate"] = manufacturer_date
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if expiry_after_duration is not UNSET:
            field_dict["expiryAfterDuration"] = expiry_after_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        _manufacturer_date = d.pop("manufacturerDate", UNSET)
        manufacturer_date: Union[Unset, datetime.datetime]
        if isinstance(_manufacturer_date, Unset):
            manufacturer_date = UNSET
        else:
            manufacturer_date = isoparse(_manufacturer_date)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, datetime.datetime]
        if isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        _expiry_after_duration = d.pop("expiryAfterDuration", UNSET)
        expiry_after_duration: Union[Unset, Duration]
        if isinstance(_expiry_after_duration, Unset):
            expiry_after_duration = UNSET
        else:
            expiry_after_duration = Duration.from_dict(_expiry_after_duration)

        result = cls(
            manufacturer_date=manufacturer_date,
            expiry_date=expiry_date,
            expiry_after_duration=expiry_after_duration,
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
