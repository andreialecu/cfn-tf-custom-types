# TF::OCI::FileStorageFileSystem

This resource provides the File System resource in Oracle Cloud Infrastructure File Storage service.

Creates a new file system in the specified compartment and
availability domain. Instances can mount file systems in
another availability domain, but doing so might increase
latency when compared to mounting instances in the same
availability domain.

After you create a file system, you can associate it with a mount
target. Instances can then mount the file system by connecting to the
mount target's IP address. You can associate a file system with
more than one mount target at a time.

For information about access control and compartments, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

For information about Network Security Groups access control, see
[Network Security Groups](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).

For information about availability domains, see [Regions and
Availability Domains...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::FileStorageFileSystem",
    "Properties" : {
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#sourcesnapshotid" title="SourceSnapshotId">SourceSnapshotId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::FileStorageFileSystem
Properties:
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#sourcesnapshotid" title="SourceSnapshotId">SourceSnapshotId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailabilityDomain

The availability domain to create the file system in.  Example: `Uocm:PHX-AD-1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to create the file system in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My file system`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

(Updatable) The OCID of KMS key used to encrypt the encryption keys associated with this file system. May be unset as a blank or deleted from the configuration to remove the KMS key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSnapshotId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the snapshot used to create a cloned file system. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningafilesystem.htm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### IsCloneParent

Returns the <code>IsCloneParent</code> value.

#### IsHydrated

Returns the <code>IsHydrated</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### MeteredBytes

Returns the <code>MeteredBytes</code> value.

#### SourceDetails

Returns the <code>SourceDetails</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

