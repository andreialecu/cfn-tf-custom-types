# TF::Datadog::Dashboard GroupByDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#facet" title="Facet">Facet</a>" : <i>String</i>,
    "<a href="#limit" title="Limit">Limit</a>" : <i>Double</i>,
    "<a href="#sort" title="Sort">Sort</a>" : <i>[ <a href="sortdefinition.md">SortDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#facet" title="Facet">Facet</a>: <i>String</i>
<a href="#limit" title="Limit">Limit</a>: <i>Double</i>
<a href="#sort" title="Sort">Sort</a>: <i>
      - <a href="sortdefinition.md">SortDefinition</a></i>
</pre>

## Properties

#### Facet

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sort

_Required_: No

_Type_: List of <a href="sortdefinition.md">SortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

