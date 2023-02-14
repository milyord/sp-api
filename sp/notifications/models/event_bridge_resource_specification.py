from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="EventBridgeResourceSpecification")


@attr.s(auto_attribs=True)
class EventBridgeResourceSpecification:
    r"""The information required to create an Amazon EventBridge destination.

    Attributes:
        region (str): The AWS region in which you will be receiving the notifications.
        account_id (str): The identifier for the AWS account that is responsible for charges related to receiving
            notifications.
    """

    region: str
    account_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region = self.region
        account_id = self.account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "accountId": account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region = d.pop("region")

        account_id = d.pop("accountId")

        result = cls(
            region=region,
            account_id=account_id,
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
