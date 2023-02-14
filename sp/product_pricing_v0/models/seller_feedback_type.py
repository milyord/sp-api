from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SellerFeedbackType")


@attr.s(auto_attribs=True)
class SellerFeedbackType:
    r"""Information about the seller's feedback, including the percentage of positive feedback, and the total number of
    ratings received.

        Attributes:
            feedback_count (int): The number of ratings received about the seller.
            seller_positive_feedback_rating (Union[Unset, float]): The percentage of positive feedback for the seller in the
                past 365 days.
    """

    feedback_count: int
    seller_positive_feedback_rating: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feedback_count = self.feedback_count
        seller_positive_feedback_rating = self.seller_positive_feedback_rating

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FeedbackCount": feedback_count,
            }
        )
        if seller_positive_feedback_rating is not UNSET:
            field_dict["SellerPositiveFeedbackRating"] = seller_positive_feedback_rating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feedback_count = d.pop("FeedbackCount")

        seller_positive_feedback_rating = d.pop("SellerPositiveFeedbackRating", UNSET)

        result = cls(
            feedback_count=feedback_count,
            seller_positive_feedback_rating=seller_positive_feedback_rating,
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
