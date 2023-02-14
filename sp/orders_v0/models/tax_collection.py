from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tax_collection_model import TaxCollectionModel
from ..models.tax_collection_responsible_party import TaxCollectionResponsibleParty
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxCollection")


@attr.s(auto_attribs=True)
class TaxCollection:
    r"""Information about withheld taxes.

    Attributes:
        model (Union[Unset, TaxCollectionModel]): The tax collection model applied to the item.
        responsible_party (Union[Unset, TaxCollectionResponsibleParty]): The party responsible for withholding the taxes
            and remitting them to the taxing authority.
    """

    model: Union[Unset, TaxCollectionModel] = UNSET
    responsible_party: Union[Unset, TaxCollectionResponsibleParty] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        responsible_party: Union[Unset, str] = UNSET
        if not isinstance(self.responsible_party, Unset):
            responsible_party = self.responsible_party.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["Model"] = model
        if responsible_party is not UNSET:
            field_dict["ResponsibleParty"] = responsible_party

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _model = d.pop("Model", UNSET)
        model: Union[Unset, TaxCollectionModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = TaxCollectionModel(_model)

        _responsible_party = d.pop("ResponsibleParty", UNSET)
        responsible_party: Union[Unset, TaxCollectionResponsibleParty]
        if isinstance(_responsible_party, Unset):
            responsible_party = UNSET
        else:
            responsible_party = TaxCollectionResponsibleParty(_responsible_party)

        result = cls(
            model=model,
            responsible_party=responsible_party,
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
