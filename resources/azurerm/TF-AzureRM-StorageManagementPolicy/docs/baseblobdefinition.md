# TF::AzureRM::StorageManagementPolicy BaseBlobDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deleteafterdayssincemodificationgreaterthan" title="DeleteAfterDaysSinceModificationGreaterThan">DeleteAfterDaysSinceModificationGreaterThan</a>" : <i>Double</i>,
    "<a href="#tiertoarchiveafterdayssincemodificationgreaterthan" title="TierToArchiveAfterDaysSinceModificationGreaterThan">TierToArchiveAfterDaysSinceModificationGreaterThan</a>" : <i>Double</i>,
    "<a href="#tiertocoolafterdayssincemodificationgreaterthan" title="TierToCoolAfterDaysSinceModificationGreaterThan">TierToCoolAfterDaysSinceModificationGreaterThan</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#deleteafterdayssincemodificationgreaterthan" title="DeleteAfterDaysSinceModificationGreaterThan">DeleteAfterDaysSinceModificationGreaterThan</a>: <i>Double</i>
<a href="#tiertoarchiveafterdayssincemodificationgreaterthan" title="TierToArchiveAfterDaysSinceModificationGreaterThan">TierToArchiveAfterDaysSinceModificationGreaterThan</a>: <i>Double</i>
<a href="#tiertocoolafterdayssincemodificationgreaterthan" title="TierToCoolAfterDaysSinceModificationGreaterThan">TierToCoolAfterDaysSinceModificationGreaterThan</a>: <i>Double</i>
</pre>

## Properties

#### DeleteAfterDaysSinceModificationGreaterThan

The age in days after last modification to delete the blob. Must be between 0 and 99999.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TierToArchiveAfterDaysSinceModificationGreaterThan

The age in days after last modification to tier blobs to archive storage. Supports blob currently at Hot or Cool tier. Must be between 0 and 99999.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TierToCoolAfterDaysSinceModificationGreaterThan

The age in days after last modification to tier blobs to cool storage. Supports blob currently at Hot tier. Must be between 0 and 99999.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

