# TF::AWS::CloudwatchQueryDefinition

Provides a CloudWatch Logs query definition resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudwatchQueryDefinition",
    "Properties" : {
        "<a href="#loggroupnames" title="LogGroupNames">LogGroupNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#querystring" title="QueryString">QueryString</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudwatchQueryDefinition
Properties:
    <a href="#loggroupnames" title="LogGroupNames">LogGroupNames</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#querystring" title="QueryString">QueryString</a>: <i>String</i>
</pre>

## Properties

#### LogGroupNames

Specific log groups to use with the query.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the query.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

The query to save. You can read more about CloudWatch Logs Query Syntax in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### QueryDefinitionId

Returns the <code>QueryDefinitionId</code> value.

