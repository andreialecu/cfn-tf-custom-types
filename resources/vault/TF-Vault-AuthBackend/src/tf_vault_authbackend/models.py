# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Accessor: Optional[str]
    DefaultLeaseTtlSeconds: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    ListingVisibility: Optional[str]
    Local: Optional[bool]
    MaxLeaseTtlSeconds: Optional[float]
    Path: Optional[str]
    Tune: Optional[Sequence["_TuneDefinition"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Accessor=json_data.get("Accessor"),
            DefaultLeaseTtlSeconds=json_data.get("DefaultLeaseTtlSeconds"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ListingVisibility=json_data.get("ListingVisibility"),
            Local=json_data.get("Local"),
            MaxLeaseTtlSeconds=json_data.get("MaxLeaseTtlSeconds"),
            Path=json_data.get("Path"),
            Tune=deserialize_list(json_data.get("Tune"), TuneDefinition),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TuneDefinition(BaseModel):
    AllowedResponseHeaders: Optional[Sequence[str]]
    AuditNonHmacRequestKeys: Optional[Sequence[str]]
    AuditNonHmacResponseKeys: Optional[Sequence[str]]
    DefaultLeaseTtl: Optional[str]
    ListingVisibility: Optional[str]
    MaxLeaseTtl: Optional[str]
    PassthroughRequestHeaders: Optional[Sequence[str]]
    TokenType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TuneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TuneDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedResponseHeaders=json_data.get("AllowedResponseHeaders"),
            AuditNonHmacRequestKeys=json_data.get("AuditNonHmacRequestKeys"),
            AuditNonHmacResponseKeys=json_data.get("AuditNonHmacResponseKeys"),
            DefaultLeaseTtl=json_data.get("DefaultLeaseTtl"),
            ListingVisibility=json_data.get("ListingVisibility"),
            MaxLeaseTtl=json_data.get("MaxLeaseTtl"),
            PassthroughRequestHeaders=json_data.get("PassthroughRequestHeaders"),
            TokenType=json_data.get("TokenType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TuneDefinition = TuneDefinition


