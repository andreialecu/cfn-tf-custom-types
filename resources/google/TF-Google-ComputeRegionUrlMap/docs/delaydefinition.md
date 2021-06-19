# TF::Google::ComputeRegionUrlMap DelayDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#percentage" title="Percentage">Percentage</a>" : <i>Double</i>,
    "<a href="#fixeddelay" title="FixedDelay">FixedDelay</a>" : <i>[ <a href="fixeddelaydefinition.md">FixedDelayDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#percentage" title="Percentage">Percentage</a>: <i>Double</i>
<a href="#fixeddelay" title="FixedDelay">FixedDelay</a>: <i>
      - <a href="fixeddelaydefinition.md">FixedDelayDefinition</a></i>
</pre>

## Properties

#### Percentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedDelay

_Required_: No

_Type_: List of <a href="fixeddelaydefinition.md">FixedDelayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

