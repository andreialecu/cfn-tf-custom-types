# TF::PagerDuty::Service ScheduledActionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tourgency" title="ToUrgency">ToUrgency</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#at" title="At">At</a>" : <i>[ <a href="atdefinition.md">AtDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tourgency" title="ToUrgency">ToUrgency</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#at" title="At">At</a>: <i>
      - <a href="atdefinition.md">AtDefinition</a></i>
</pre>

## Properties

#### ToUrgency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### At

_Required_: No

_Type_: List of <a href="atdefinition.md">AtDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

