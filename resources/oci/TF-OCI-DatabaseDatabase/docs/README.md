# TF::OCI::DatabaseDatabase

This resource provides the Database resource in Oracle Cloud Infrastructure Database service.

Creates a new database in the specified Database Home. If the database version is provided, it must match the version of the Database Home. Applies only to Exadata systems.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseDatabase",
    "Properties" : {
        "<a href="#dbhomeid" title="DbHomeId">DbHomeId</a>" : <i>String</i>,
        "<a href="#dbversion" title="DbVersion">DbVersion</a>" : <i>String</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#kmskeymigration" title="KmsKeyMigration">KmsKeyMigration</a>" : <i>Boolean</i>,
        "<a href="#kmskeyrotation" title="KmsKeyRotation">KmsKeyRotation</a>" : <i>Double</i>,
        "<a href="#kmskeyversionid" title="KmsKeyVersionId">KmsKeyVersionId</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ <a href="databasedefinition.md">DatabaseDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseDatabase
Properties:
    <a href="#dbhomeid" title="DbHomeId">DbHomeId</a>: <i>String</i>
    <a href="#dbversion" title="DbVersion">DbVersion</a>: <i>String</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#kmskeymigration" title="KmsKeyMigration">KmsKeyMigration</a>: <i>Boolean</i>
    <a href="#kmskeyrotation" title="KmsKeyRotation">KmsKeyRotation</a>: <i>Double</i>
    <a href="#kmskeyversionid" title="KmsKeyVersionId">KmsKeyVersionId</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#database" title="Database">Database</a>: <i>
      - <a href="databasedefinition.md">DatabaseDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DbHomeId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyMigration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyRotation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyVersionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of <a href="databasedefinition.md">DatabaseDefinition</a>

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

#### CharacterSet

The character set for the database.  The default is AL32UTF8. Allowed values are:.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### ConnectionStrings

Returns the <code>ConnectionStrings</code> value.

#### DatabaseSoftwareImageId

Returns the <code>DatabaseSoftwareImageId</code> value.

#### DbBackupConfig

Returns the <code>DbBackupConfig</code> value.

#### DbName

Returns the <code>DbName</code> value.

#### DbSystemId

Returns the <code>DbSystemId</code> value.

#### DbUniqueName

Returns the <code>DbUniqueName</code> value.

#### DbWorkload

Returns the <code>DbWorkload</code> value.

#### DefinedTags

Returns the <code>DefinedTags</code> value.

#### FreeformTags

Returns the <code>FreeformTags</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastBackupTimestamp

Returns the <code>LastBackupTimestamp</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### NcharacterSet

Returns the <code>NcharacterSet</code> value.

#### PdbName

Returns the <code>PdbName</code> value.

#### SourceDatabasePointInTimeRecoveryTimestamp

Returns the <code>SourceDatabasePointInTimeRecoveryTimestamp</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VmClusterId

Returns the <code>VmClusterId</code> value.

