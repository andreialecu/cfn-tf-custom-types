# TF::SumoLogic::KinesisMetricsSource PathDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#tagfilters" title="TagFilters">TagFilters</a>" : <i>[ <a href="tagfiltersdefinition.md">TagFiltersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#tagfilters" title="TagFilters">TagFilters</a>: <i>
      - <a href="tagfiltersdefinition.md">TagFiltersDefinition</a></i>
</pre>

## Properties

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagFilters

_Required_: No

_Type_: List of <a href="tagfiltersdefinition.md">TagFiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

