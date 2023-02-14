from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_component import ChargeComponent


T = TypeVar("T", bound="TaxWithheldComponent")


@attr.s(auto_attribs=True)
class TaxWithheldComponent:
    r"""Information about the taxes withheld.

    Attributes:
        tax_collection_model (Union[Unset, str]): The tax collection model applied to the item.

            Possible values:

            * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the
            seller.

            * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.
        taxes_withheld (Union[Unset, List['ChargeComponent']]): A list of charge information on the seller's account.
    """

    tax_collection_model: Union[Unset, str] = UNSET
    taxes_withheld: Union[Unset, List["ChargeComponent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_collection_model = self.tax_collection_model
        taxes_withheld: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.taxes_withheld, Unset):
            taxes_withheld = []
            for componentsschemas_charge_component_list_item_data in self.taxes_withheld:
                componentsschemas_charge_component_list_item = (
                    componentsschemas_charge_component_list_item_data.to_dict()
                )

                taxes_withheld.append(componentsschemas_charge_component_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tax_collection_model is not UNSET:
            field_dict["TaxCollectionModel"] = tax_collection_model
        if taxes_withheld is not UNSET:
            field_dict["TaxesWithheld"] = taxes_withheld

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_component import ChargeComponent

        d = src_dict.copy()
        tax_collection_model = d.pop("TaxCollectionModel", UNSET)

        taxes_withheld = []
        _taxes_withheld = d.pop("TaxesWithheld", UNSET)
        for componentsschemas_charge_component_list_item_data in _taxes_withheld or []:
            componentsschemas_charge_component_list_item = ChargeComponent.from_dict(
                componentsschemas_charge_component_list_item_data
            )

            taxes_withheld.append(componentsschemas_charge_component_list_item)

        result = cls(
            tax_collection_model=tax_collection_model,
            taxes_withheld=taxes_withheld,
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
