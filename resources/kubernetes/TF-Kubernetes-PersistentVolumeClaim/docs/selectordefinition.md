# TF::Kubernetes::PersistentVolumeClaim SelectorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchlabels" title="MatchLabels">MatchLabels</a>" : <i>[ <a href="matchlabelsdefinition.md">MatchLabelsDefinition</a>, ... ]</i>,
    "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ <a href="matchexpressionsdefinition.md">MatchExpressionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchlabels" title="MatchLabels">MatchLabels</a>: <i>
      - <a href="matchlabelsdefinition.md">MatchLabelsDefinition</a></i>
<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - <a href="matchexpressionsdefinition.md">MatchExpressionsDefinition</a></i>
</pre>

## Properties

#### MatchLabels

_Required_: No

_Type_: List of <a href="matchlabelsdefinition.md">MatchLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of <a href="matchexpressionsdefinition.md">MatchExpressionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

