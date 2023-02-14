import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.currency_amount import CurrencyAmount
    from ..models.length import Length
    from ..models.weight import Weight


T = TypeVar("T", bound="AdditionalSellerInput")


@attr.s(auto_attribs=True)
class AdditionalSellerInput:
    r"""Additional information required to purchase shipping.

    Attributes:
        data_type (Union[Unset, str]): The data type of the additional information.
        value_as_string (Union[Unset, str]): The value when the data type is string.
        value_as_boolean (Union[Unset, bool]): The value when the data type is boolean.
        value_as_integer (Union[Unset, int]): The value when the data type is integer.
        value_as_timestamp (Union[Unset, datetime.datetime]):
        value_as_address (Union[Unset, Address]): The postal address information.
        value_as_weight (Union[Unset, Weight]): The weight.
        value_as_dimension (Union[Unset, Length]): The length.
        value_as_currency (Union[Unset, CurrencyAmount]): Currency type and amount.
    """

    data_type: Union[Unset, str] = UNSET
    value_as_string: Union[Unset, str] = UNSET
    value_as_boolean: Union[Unset, bool] = UNSET
    value_as_integer: Union[Unset, int] = UNSET
    value_as_timestamp: Union[Unset, datetime.datetime] = UNSET
    value_as_address: Union[Unset, "Address"] = UNSET
    value_as_weight: Union[Unset, "Weight"] = UNSET
    value_as_dimension: Union[Unset, "Length"] = UNSET
    value_as_currency: Union[Unset, "CurrencyAmount"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_type = self.data_type
        value_as_string = self.value_as_string
        value_as_boolean = self.value_as_boolean
        value_as_integer = self.value_as_integer
        value_as_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.value_as_timestamp, Unset):
            value_as_timestamp = self.value_as_timestamp.isoformat()

        value_as_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_as_address, Unset):
            value_as_address = self.value_as_address.to_dict()

        value_as_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_as_weight, Unset):
            value_as_weight = self.value_as_weight.to_dict()

        value_as_dimension: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_as_dimension, Unset):
            value_as_dimension = self.value_as_dimension.to_dict()

        value_as_currency: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_as_currency, Unset):
            value_as_currency = self.value_as_currency.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_type is not UNSET:
            field_dict["DataType"] = data_type
        if value_as_string is not UNSET:
            field_dict["ValueAsString"] = value_as_string
        if value_as_boolean is not UNSET:
            field_dict["ValueAsBoolean"] = value_as_boolean
        if value_as_integer is not UNSET:
            field_dict["ValueAsInteger"] = value_as_integer
        if value_as_timestamp is not UNSET:
            field_dict["ValueAsTimestamp"] = value_as_timestamp
        if value_as_address is not UNSET:
            field_dict["ValueAsAddress"] = value_as_address
        if value_as_weight is not UNSET:
            field_dict["ValueAsWeight"] = value_as_weight
        if value_as_dimension is not UNSET:
            field_dict["ValueAsDimension"] = value_as_dimension
        if value_as_currency is not UNSET:
            field_dict["ValueAsCurrency"] = value_as_currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.currency_amount import CurrencyAmount
        from ..models.length import Length
        from ..models.weight import Weight

        d = src_dict.copy()
        data_type = d.pop("DataType", UNSET)

        value_as_string = d.pop("ValueAsString", UNSET)

        value_as_boolean = d.pop("ValueAsBoolean", UNSET)

        value_as_integer = d.pop("ValueAsInteger", UNSET)

        _value_as_timestamp = d.pop("ValueAsTimestamp", UNSET)
        value_as_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_value_as_timestamp, Unset):
            value_as_timestamp = UNSET
        else:
            value_as_timestamp = isoparse(_value_as_timestamp)

        _value_as_address = d.pop("ValueAsAddress", UNSET)
        value_as_address: Union[Unset, Address]
        if isinstance(_value_as_address, Unset):
            value_as_address = UNSET
        else:
            value_as_address = Address.from_dict(_value_as_address)

        _value_as_weight = d.pop("ValueAsWeight", UNSET)
        value_as_weight: Union[Unset, Weight]
        if isinstance(_value_as_weight, Unset):
            value_as_weight = UNSET
        else:
            value_as_weight = Weight.from_dict(_value_as_weight)

        _value_as_dimension = d.pop("ValueAsDimension", UNSET)
        value_as_dimension: Union[Unset, Length]
        if isinstance(_value_as_dimension, Unset):
            value_as_dimension = UNSET
        else:
            value_as_dimension = Length.from_dict(_value_as_dimension)

        _value_as_currency = d.pop("ValueAsCurrency", UNSET)
        value_as_currency: Union[Unset, CurrencyAmount]
        if isinstance(_value_as_currency, Unset):
            value_as_currency = UNSET
        else:
            value_as_currency = CurrencyAmount.from_dict(_value_as_currency)

        result = cls(
            data_type=data_type,
            value_as_string=value_as_string,
            value_as_boolean=value_as_boolean,
            value_as_integer=value_as_integer,
            value_as_timestamp=value_as_timestamp,
            value_as_address=value_as_address,
            value_as_weight=value_as_weight,
            value_as_dimension=value_as_dimension,
            value_as_currency=value_as_currency,
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
