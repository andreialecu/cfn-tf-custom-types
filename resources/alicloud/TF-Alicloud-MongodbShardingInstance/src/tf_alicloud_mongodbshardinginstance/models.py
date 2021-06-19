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
    AccountPassword: Optional[str]
    BackupPeriod: Optional[Sequence[str]]
    BackupTime: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContextDefinition"]]
    Name: Optional[str]
    Period: Optional[float]
    RetentionPeriod: Optional[float]
    SecurityGroupId: Optional[str]
    SecurityIpList: Optional[Sequence[str]]
    StorageEngine: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TdeStatus: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    MongoList: Optional[Sequence["_MongoListDefinition"]]
    ShardList: Optional[Sequence["_ShardListDefinition"]]

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
            AccountPassword=json_data.get("AccountPassword"),
            BackupPeriod=json_data.get("BackupPeriod"),
            BackupTime=json_data.get("BackupTime"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=deserialize_list(json_data.get("KmsEncryptionContext"), KmsEncryptionContextDefinition),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityIpList=json_data.get("SecurityIpList"),
            StorageEngine=json_data.get("StorageEngine"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TdeStatus=json_data.get("TdeStatus"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            MongoList=deserialize_list(json_data.get("MongoList"), MongoListDefinition),
            ShardList=deserialize_list(json_data.get("ShardList"), ShardListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KmsEncryptionContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionContextDefinition = KmsEncryptionContextDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class MongoListDefinition(BaseModel):
    NodeClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongoListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongoListDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeClass=json_data.get("NodeClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongoListDefinition = MongoListDefinition


@dataclass
class ShardListDefinition(BaseModel):
    NodeClass: Optional[str]
    NodeStorage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ShardListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShardListDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeClass=json_data.get("NodeClass"),
            NodeStorage=json_data.get("NodeStorage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShardListDefinition = ShardListDefinition


