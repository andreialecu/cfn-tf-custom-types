# TF::AzureRM::CosmosdbSqlContainer SpatialIndexDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#path" title="Path">Path</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### Path

Path for which the indexing behaviour applies to. According to the service design, all spatial types including `LineString`, `MultiPolygon`, `Point`, and `Polygon` will be applied to the path.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

