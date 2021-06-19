# TF::Google::StorageBucket

Creates a new bucket in Google cloud storage service (GCS).
Once a bucket has been created, its location can't be changed.

For more information see
[the official documentation](https://cloud.google.com/storage/docs/overview)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/buckets).

**Note**: If the project id is not set on the resource or in the provider block it will be dynamically
determined which will require enabling the compute api.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::StorageBucket",
    "Properties" : {
        "<a href="#bucketpolicyonly" title="BucketPolicyOnly">BucketPolicyOnly</a>" : <i>Boolean</i>,
        "<a href="#defaulteventbasedhold" title="DefaultEventBasedHold">DefaultEventBasedHold</a>" : <i>Boolean</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#requesterpays" title="RequesterPays">RequesterPays</a>" : <i>Boolean</i>,
        "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
        "<a href="#uniformbucketlevelaccess" title="UniformBucketLevelAccess">UniformBucketLevelAccess</a>" : <i>Boolean</i>,
        "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="corsdefinition.md">CorsDefinition</a>, ... ]</i>,
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>[ <a href="encryptiondefinition.md">EncryptionDefinition</a>, ... ]</i>,
        "<a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>" : <i>[ <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a>, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="loggingdefinition.md">LoggingDefinition</a>, ... ]</i>,
        "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ <a href="retentionpolicydefinition.md">RetentionPolicyDefinition</a>, ... ]</i>,
        "<a href="#versioning" title="Versioning">Versioning</a>" : <i>[ <a href="versioningdefinition.md">VersioningDefinition</a>, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ <a href="websitedefinition.md">WebsiteDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::StorageBucket
Properties:
    <a href="#bucketpolicyonly" title="BucketPolicyOnly">BucketPolicyOnly</a>: <i>Boolean</i>
    <a href="#defaulteventbasedhold" title="DefaultEventBasedHold">DefaultEventBasedHold</a>: <i>Boolean</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#requesterpays" title="RequesterPays">RequesterPays</a>: <i>Boolean</i>
    <a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
    <a href="#uniformbucketlevelaccess" title="UniformBucketLevelAccess">UniformBucketLevelAccess</a>: <i>Boolean</i>
    <a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="corsdefinition.md">CorsDefinition</a></i>
    <a href="#encryption" title="Encryption">Encryption</a>: <i>
      - <a href="encryptiondefinition.md">EncryptionDefinition</a></i>
    <a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>: <i>
      - <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a></i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="loggingdefinition.md">LoggingDefinition</a></i>
    <a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - <a href="retentionpolicydefinition.md">RetentionPolicyDefinition</a></i>
    <a href="#versioning" title="Versioning">Versioning</a>: <i>
      - <a href="versioningdefinition.md">VersioningDefinition</a></i>
    <a href="#website" title="Website">Website</a>: <i>
      - <a href="websitedefinition.md">WebsiteDefinition</a></i>
</pre>

## Properties

#### BucketPolicyOnly

Enables [Bucket Policy Only](https://cloud.google.com/storage/docs/bucket-policy-only) access to a bucket. This field will be removed in the next major release of the provider.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultEventBasedHold

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

When deleting a bucket, this
boolean option will delete all contained objects. If you try to delete a
bucket that contains objects, Terraform will fail that run.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

A map of key/value label pairs to assign to the bucket.

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The [GCS location](https://cloud.google.com/storage/docs/bucket-locations).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequesterPays

Enables [Requester Pays](https://cloud.google.com/storage/docs/requester-pays) on a storage bucket.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

The [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of the new bucket. Supported values include: `STANDARD`, `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UniformBucketLevelAccess

Enables [Uniform bucket-level access](https://cloud.google.com/storage/docs/uniform-bucket-level-access) access to a bucket.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="corsdefinition.md">CorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryption

_Required_: No

_Type_: List of <a href="encryptiondefinition.md">EncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRule

_Required_: No

_Type_: List of <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="loggingdefinition.md">LoggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicy

_Required_: No

_Type_: List of <a href="retentionpolicydefinition.md">RetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Versioning

_Required_: No

_Type_: List of <a href="versioningdefinition.md">VersioningDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

_Required_: No

_Type_: List of <a href="websitedefinition.md">WebsiteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### Url

Returns the <code>Url</code> value.

