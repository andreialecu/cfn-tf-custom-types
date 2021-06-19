# TF::AWS::AlbTargetGroup

CloudFormation equivalent of aws_alb_target_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AlbTargetGroup",
    "Properties" : {
        "<a href="#deregistrationdelay" title="DeregistrationDelay">DeregistrationDelay</a>" : <i>Double</i>,
        "<a href="#lambdamultivalueheadersenabled" title="LambdaMultiValueHeadersEnabled">LambdaMultiValueHeadersEnabled</a>" : <i>Boolean</i>,
        "<a href="#loadbalancingalgorithmtype" title="LoadBalancingAlgorithmType">LoadBalancingAlgorithmType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#preserveclientip" title="PreserveClientIp">PreserveClientIp</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#protocolversion" title="ProtocolVersion">ProtocolVersion</a>" : <i>String</i>,
        "<a href="#proxyprotocolv2" title="ProxyProtocolV2">ProxyProtocolV2</a>" : <i>Boolean</i>,
        "<a href="#slowstart" title="SlowStart">SlowStart</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthCheckDefinition</a>, ... ]</i>,
        "<a href="#stickiness" title="Stickiness">Stickiness</a>" : <i>[ <a href="stickinessdefinition.md">StickinessDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AlbTargetGroup
Properties:
    <a href="#deregistrationdelay" title="DeregistrationDelay">DeregistrationDelay</a>: <i>Double</i>
    <a href="#lambdamultivalueheadersenabled" title="LambdaMultiValueHeadersEnabled">LambdaMultiValueHeadersEnabled</a>: <i>Boolean</i>
    <a href="#loadbalancingalgorithmtype" title="LoadBalancingAlgorithmType">LoadBalancingAlgorithmType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#preserveclientip" title="PreserveClientIp">PreserveClientIp</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#protocolversion" title="ProtocolVersion">ProtocolVersion</a>: <i>String</i>
    <a href="#proxyprotocolv2" title="ProxyProtocolV2">ProxyProtocolV2</a>: <i>Boolean</i>
    <a href="#slowstart" title="SlowStart">SlowStart</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthCheckDefinition</a></i>
    <a href="#stickiness" title="Stickiness">Stickiness</a>: <i>
      - <a href="stickinessdefinition.md">StickinessDefinition</a></i>
</pre>

## Properties

#### DeregistrationDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaMultiValueHeadersEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingAlgorithmType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveClientIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyProtocolV2

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlowStart

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stickiness

_Required_: No

_Type_: List of <a href="stickinessdefinition.md">StickinessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### ArnSuffix

Returns the <code>ArnSuffix</code> value.

#### Id

Returns the <code>Id</code> value.

