# TF::OCI::AutoscalingAutoScalingConfiguration RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="actiondefinition.md">ActionDefinition</a>, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metricdefinition.md">MetricDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="actiondefinition.md">ActionDefinition</a></i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metricdefinition.md">MetricDefinition</a></i>
</pre>

## Properties

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="actiondefinition.md">ActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metricdefinition.md">MetricDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

