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
    Arn: Optional[str]
    CompatibleRuntimes: Optional[Sequence[str]]
    CreatedDate: Optional[str]
    Description: Optional[str]
    Filename: Optional[str]
    Id: Optional[str]
    LayerArn: Optional[str]
    LayerName: Optional[str]
    LicenseInfo: Optional[str]
    S3Bucket: Optional[str]
    S3Key: Optional[str]
    S3ObjectVersion: Optional[str]
    SigningJobArn: Optional[str]
    SigningProfileVersionArn: Optional[str]
    SourceCodeHash: Optional[str]
    SourceCodeSize: Optional[float]
    Version: Optional[str]

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
            Arn=json_data.get("Arn"),
            CompatibleRuntimes=json_data.get("CompatibleRuntimes"),
            CreatedDate=json_data.get("CreatedDate"),
            Description=json_data.get("Description"),
            Filename=json_data.get("Filename"),
            Id=json_data.get("Id"),
            LayerArn=json_data.get("LayerArn"),
            LayerName=json_data.get("LayerName"),
            LicenseInfo=json_data.get("LicenseInfo"),
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
            S3ObjectVersion=json_data.get("S3ObjectVersion"),
            SigningJobArn=json_data.get("SigningJobArn"),
            SigningProfileVersionArn=json_data.get("SigningProfileVersionArn"),
            SourceCodeHash=json_data.get("SourceCodeHash"),
            SourceCodeSize=json_data.get("SourceCodeSize"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


