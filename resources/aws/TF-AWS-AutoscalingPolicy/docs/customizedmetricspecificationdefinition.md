# TF::AWS::AutoscalingPolicy CustomizedMetricSpecificationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#statistic" title="Statistic">Statistic</a>" : <i>String</i>,
    "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
    "<a href="#metricdimension" title="MetricDimension">MetricDimension</a>" : <i>[ <a href="metricdimensiondefinition.md">MetricDimensionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#statistic" title="Statistic">Statistic</a>: <i>String</i>
<a href="#unit" title="Unit">Unit</a>: <i>String</i>
<a href="#metricdimension" title="MetricDimension">MetricDimension</a>: <i>
      - <a href="metricdimensiondefinition.md">MetricDimensionDefinition</a></i>
</pre>

## Properties

#### MetricName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statistic

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricDimension

_Required_: No

_Type_: List of <a href="metricdimensiondefinition.md">MetricDimensionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

