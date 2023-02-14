from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scenario import Scenario


T = TypeVar("T", bound="TestCaseData")


@attr.s(auto_attribs=True)
class TestCaseData:
    r"""The set of test case data returned in response to the test data request.

    Attributes:
        scenarios (Union[Unset, List['Scenario']]): Set of use cases that describes the possible test scenarios.
    """

    scenarios: Union[Unset, List["Scenario"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scenarios: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scenarios, Unset):
            scenarios = []
            for scenarios_item_data in self.scenarios:
                scenarios_item = scenarios_item_data.to_dict()

                scenarios.append(scenarios_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scenarios is not UNSET:
            field_dict["scenarios"] = scenarios

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scenario import Scenario

        d = src_dict.copy()
        scenarios = []
        _scenarios = d.pop("scenarios", UNSET)
        for scenarios_item_data in _scenarios or []:
            scenarios_item = Scenario.from_dict(scenarios_item_data)

            scenarios.append(scenarios_item)

        result = cls(
            scenarios=scenarios,
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
