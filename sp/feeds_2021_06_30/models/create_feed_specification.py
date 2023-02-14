from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feed_options import FeedOptions


T = TypeVar("T", bound="CreateFeedSpecification")


@attr.s(auto_attribs=True)
class CreateFeedSpecification:
    r"""Information required to create the feed.

    Attributes:
        feed_type (str): The feed type.
        marketplace_ids (List[str]): A list of identifiers for marketplaces that you want the feed to be applied to.
        input_feed_document_id (str): The document identifier returned by the createFeedDocument operation. Upload the
            feed document contents before calling the createFeed operation.
        feed_options (Union[Unset, FeedOptions]): Additional options to control the feed. These vary by feed type.
    """

    feed_type: str
    marketplace_ids: List[str]
    input_feed_document_id: str
    feed_options: Union[Unset, "FeedOptions"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feed_type = self.feed_type
        marketplace_ids = self.marketplace_ids

        input_feed_document_id = self.input_feed_document_id
        feed_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_options, Unset):
            feed_options = self.feed_options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feedType": feed_type,
                "marketplaceIds": marketplace_ids,
                "inputFeedDocumentId": input_feed_document_id,
            }
        )
        if feed_options is not UNSET:
            field_dict["feedOptions"] = feed_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feed_options import FeedOptions

        d = src_dict.copy()
        feed_type = d.pop("feedType")

        marketplace_ids = cast(List[str], d.pop("marketplaceIds"))

        input_feed_document_id = d.pop("inputFeedDocumentId")

        _feed_options = d.pop("feedOptions", UNSET)
        feed_options: Union[Unset, FeedOptions]
        if isinstance(_feed_options, Unset):
            feed_options = UNSET
        else:
            feed_options = FeedOptions.from_dict(_feed_options)

        result = cls(
            feed_type=feed_type,
            marketplace_ids=marketplace_ids,
            input_feed_document_id=input_feed_document_id,
            feed_options=feed_options,
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
