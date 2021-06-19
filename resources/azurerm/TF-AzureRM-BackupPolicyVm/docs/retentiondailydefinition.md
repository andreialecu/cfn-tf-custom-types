# TF::AzureRM::BackupPolicyVm RetentionDailyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
</pre>

## Properties

#### Count

The number of daily backups to keep. Must be between `7` and `9999`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

