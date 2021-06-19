# TF::Google::DataprocCluster PreemptibleWorkerConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#numinstances" title="NumInstances">NumInstances</a>" : <i>Double</i>,
    "<a href="#diskconfig" title="DiskConfig">DiskConfig</a>" : <i>[ <a href="diskconfigdefinition.md">DiskConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#numinstances" title="NumInstances">NumInstances</a>: <i>Double</i>
<a href="#diskconfig" title="DiskConfig">DiskConfig</a>: <i>
      - <a href="diskconfigdefinition.md">DiskConfigDefinition</a></i>
</pre>

## Properties

#### NumInstances

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskConfig

_Required_: No

_Type_: List of <a href="diskconfigdefinition.md">DiskConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

