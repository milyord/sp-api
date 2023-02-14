from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.packing_slip import PackingSlip
    from ..models.pagination import Pagination


T = TypeVar("T", bound="PackingSlipList")


@attr.s(auto_attribs=True)
class PackingSlipList:
    r"""A list of packing slips.

    Attributes:
        pagination (Union[Unset, Pagination]):
        packing_slips (Union[Unset, List['PackingSlip']]):
    """

    pagination: Union[Unset, "Pagination"] = UNSET
    packing_slips: Union[Unset, List["PackingSlip"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        packing_slips: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.packing_slips, Unset):
            packing_slips = []
            for packing_slips_item_data in self.packing_slips:
                packing_slips_item = packing_slips_item_data.to_dict()

                packing_slips.append(packing_slips_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if packing_slips is not UNSET:
            field_dict["packingSlips"] = packing_slips

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.packing_slip import PackingSlip
        from ..models.pagination import Pagination

        d = src_dict.copy()
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        packing_slips = []
        _packing_slips = d.pop("packingSlips", UNSET)
        for packing_slips_item_data in _packing_slips or []:
            packing_slips_item = PackingSlip.from_dict(packing_slips_item_data)

            packing_slips.append(packing_slips_item)

        result = cls(
            pagination=pagination,
            packing_slips=packing_slips,
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
