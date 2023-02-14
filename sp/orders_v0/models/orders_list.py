from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order import Order


T = TypeVar("T", bound="OrdersList")


@attr.s(auto_attribs=True)
class OrdersList:
    r"""A list of orders along with additional information to make subsequent API calls.

    Attributes:
        orders (List['Order']): A list of orders.
        next_token (Union[Unset, str]): When present and not empty, pass this string token in the next request to return
            the next response page.
        last_updated_before (Union[Unset, str]): A date used for selecting orders that were last updated before (or at)
            a specified time. An update is defined as any change in order status, including the creation of a new order.
            Includes updates made by Amazon and by the seller. All dates must be in ISO 8601 format.
        created_before (Union[Unset, str]): A date used for selecting orders created before (or at) a specified time.
            Only orders placed before the specified time are returned. The date must be in ISO 8601 format.
    """

    orders: List["Order"]
    next_token: Union[Unset, str] = UNSET
    last_updated_before: Union[Unset, str] = UNSET
    created_before: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        orders = []
        for componentsschemas_order_list_item_data in self.orders:
            componentsschemas_order_list_item = componentsschemas_order_list_item_data.to_dict()

            orders.append(componentsschemas_order_list_item)

        next_token = self.next_token
        last_updated_before = self.last_updated_before
        created_before = self.created_before

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Orders": orders,
            }
        )
        if next_token is not UNSET:
            field_dict["NextToken"] = next_token
        if last_updated_before is not UNSET:
            field_dict["LastUpdatedBefore"] = last_updated_before
        if created_before is not UNSET:
            field_dict["CreatedBefore"] = created_before

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order import Order

        d = src_dict.copy()
        orders = []
        _orders = d.pop("Orders")
        for componentsschemas_order_list_item_data in _orders:
            componentsschemas_order_list_item = Order.from_dict(componentsschemas_order_list_item_data)

            orders.append(componentsschemas_order_list_item)

        next_token = d.pop("NextToken", UNSET)

        last_updated_before = d.pop("LastUpdatedBefore", UNSET)

        created_before = d.pop("CreatedBefore", UNSET)

        result = cls(
            orders=orders,
            next_token=next_token,
            last_updated_before=last_updated_before,
            created_before=created_before,
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
