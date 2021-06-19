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
    AutoReleaseTime: Optional[str]
    DeploymentSetId: Optional[str]
    Description: Optional[str]
    EnableVmOsConfig: Optional[bool]
    HostName: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    ImageOwnerAlias: Optional[str]
    InstanceChargeType: Optional[str]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthIn: Optional[float]
    InternetMaxBandwidthOut: Optional[float]
    IoOptimized: Optional[str]
    KeyPairName: Optional[str]
    LaunchTemplateName: Optional[str]
    Name: Optional[str]
    NetworkType: Optional[str]
    PasswordInherit: Optional[bool]
    Period: Optional[float]
    PrivateIpAddress: Optional[str]
    RamRoleName: Optional[str]
    ResourceGroupId: Optional[str]
    SecurityEnhancementStrategy: Optional[str]
    SecurityGroupId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SpotDuration: Optional[str]
    SpotPriceLimit: Optional[float]
    SpotStrategy: Optional[str]
    SystemDiskCategory: Optional[str]
    SystemDiskDescription: Optional[str]
    SystemDiskName: Optional[str]
    SystemDiskSize: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TemplateResourceGroupId: Optional[str]
    TemplateTags: Optional[Sequence["_TemplateTagsDefinition"]]
    UserData: Optional[str]
    Userdata: Optional[str]
    VersionDescription: Optional[str]
    VpcId: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    DataDisks: Optional[Sequence["_DataDisksDefinition"]]
    NetworkInterfaces: Optional[Sequence["_NetworkInterfacesDefinition"]]
    SystemDisk: Optional[Sequence["_SystemDiskDefinition"]]

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
            AutoReleaseTime=json_data.get("AutoReleaseTime"),
            DeploymentSetId=json_data.get("DeploymentSetId"),
            Description=json_data.get("Description"),
            EnableVmOsConfig=json_data.get("EnableVmOsConfig"),
            HostName=json_data.get("HostName"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            ImageOwnerAlias=json_data.get("ImageOwnerAlias"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthIn=json_data.get("InternetMaxBandwidthIn"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            IoOptimized=json_data.get("IoOptimized"),
            KeyPairName=json_data.get("KeyPairName"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Name=json_data.get("Name"),
            NetworkType=json_data.get("NetworkType"),
            PasswordInherit=json_data.get("PasswordInherit"),
            Period=json_data.get("Period"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            RamRoleName=json_data.get("RamRoleName"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SecurityEnhancementStrategy=json_data.get("SecurityEnhancementStrategy"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SpotDuration=json_data.get("SpotDuration"),
            SpotPriceLimit=json_data.get("SpotPriceLimit"),
            SpotStrategy=json_data.get("SpotStrategy"),
            SystemDiskCategory=json_data.get("SystemDiskCategory"),
            SystemDiskDescription=json_data.get("SystemDiskDescription"),
            SystemDiskName=json_data.get("SystemDiskName"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TemplateResourceGroupId=json_data.get("TemplateResourceGroupId"),
            TemplateTags=deserialize_list(json_data.get("TemplateTags"), TemplateTagsDefinition),
            UserData=json_data.get("UserData"),
            Userdata=json_data.get("Userdata"),
            VersionDescription=json_data.get("VersionDescription"),
            VpcId=json_data.get("VpcId"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            DataDisks=deserialize_list(json_data.get("DataDisks"), DataDisksDefinition),
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), NetworkInterfacesDefinition),
            SystemDisk=deserialize_list(json_data.get("SystemDisk"), SystemDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class TemplateTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateTagsDefinition = TemplateTagsDefinition


@dataclass
class DataDisksDefinition(BaseModel):
    Category: Optional[str]
    DeleteWithInstance: Optional[bool]
    Description: Optional[str]
    Encrypted: Optional[bool]
    Name: Optional[str]
    PerformanceLevel: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisksDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Description=json_data.get("Description"),
            Encrypted=json_data.get("Encrypted"),
            Name=json_data.get("Name"),
            PerformanceLevel=json_data.get("PerformanceLevel"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisksDefinition = DataDisksDefinition


@dataclass
class NetworkInterfacesDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    PrimaryIp: Optional[str]
    SecurityGroupId: Optional[str]
    VswitchId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            PrimaryIp=json_data.get("PrimaryIp"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            VswitchId=json_data.get("VswitchId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfacesDefinition = NetworkInterfacesDefinition


@dataclass
class SystemDiskDefinition(BaseModel):
    Category: Optional[str]
    DeleteWithInstance: Optional[bool]
    Description: Optional[str]
    Iops: Optional[str]
    Name: Optional[str]
    PerformanceLevel: Optional[str]
    Size: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SystemDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Description=json_data.get("Description"),
            Iops=json_data.get("Iops"),
            Name=json_data.get("Name"),
            PerformanceLevel=json_data.get("PerformanceLevel"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemDiskDefinition = SystemDiskDefinition


