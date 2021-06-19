# TF::Kubernetes::PersistentVolume NodeSelectorTermDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ <a href="matchexpressionsdefinition.md">MatchExpressionsDefinition</a>, ... ]</i>,
    "<a href="#matchfields" title="MatchFields">MatchFields</a>" : <i>[ <a href="matchfieldsdefinition.md">MatchFieldsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - <a href="matchexpressionsdefinition.md">MatchExpressionsDefinition</a></i>
<a href="#matchfields" title="MatchFields">MatchFields</a>: <i>
      - <a href="matchfieldsdefinition.md">MatchFieldsDefinition</a></i>
</pre>

## Properties

#### MatchExpressions

_Required_: No

_Type_: List of <a href="matchexpressionsdefinition.md">MatchExpressionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchFields

_Required_: No

_Type_: List of <a href="matchfieldsdefinition.md">MatchFieldsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

