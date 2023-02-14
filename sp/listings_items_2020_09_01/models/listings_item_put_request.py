from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.listings_item_put_request_requirements import ListingsItemPutRequestRequirements
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_item_put_request_attributes import ListingsItemPutRequestAttributes


T = TypeVar("T", bound="ListingsItemPutRequest")


@attr.s(auto_attribs=True)
class ListingsItemPutRequest:
    r"""The request body schema for the putListingsItem operation.

    Attributes:
        product_type (str): The Amazon product type of the listings item.
        attributes (ListingsItemPutRequestAttributes): JSON object containing structured listings item attribute data
            keyed by attribute name.
        requirements (Union[Unset, ListingsItemPutRequestRequirements]): The name of the requirements set for the
            provided data.
    """

    product_type: str
    attributes: "ListingsItemPutRequestAttributes"
    requirements: Union[Unset, ListingsItemPutRequestRequirements] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_type = self.product_type
        attributes = self.attributes.to_dict()

        requirements: Union[Unset, str] = UNSET
        if not isinstance(self.requirements, Unset):
            requirements = self.requirements.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productType": product_type,
                "attributes": attributes,
            }
        )
        if requirements is not UNSET:
            field_dict["requirements"] = requirements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listings_item_put_request_attributes import ListingsItemPutRequestAttributes

        d = src_dict.copy()
        product_type = d.pop("productType")

        attributes = ListingsItemPutRequestAttributes.from_dict(d.pop("attributes"))

        _requirements = d.pop("requirements", UNSET)
        requirements: Union[Unset, ListingsItemPutRequestRequirements]
        if isinstance(_requirements, Unset):
            requirements = UNSET
        else:
            requirements = ListingsItemPutRequestRequirements(_requirements)

        result = cls(
            product_type=product_type,
            attributes=attributes,
            requirements=requirements,
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
