# TF::AWS::LoadBalancerListenerPolicy

Attaches a load balancer policy to an ELB Listener.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LoadBalancerListenerPolicy",
    "Properties" : {
        "<a href="#loadbalancername" title="LoadBalancerName">LoadBalancerName</a>" : <i>String</i>,
        "<a href="#loadbalancerport" title="LoadBalancerPort">LoadBalancerPort</a>" : <i>Double</i>,
        "<a href="#policynames" title="PolicyNames">PolicyNames</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LoadBalancerListenerPolicy
Properties:
    <a href="#loadbalancername" title="LoadBalancerName">LoadBalancerName</a>: <i>String</i>
    <a href="#loadbalancerport" title="LoadBalancerPort">LoadBalancerPort</a>: <i>Double</i>
    <a href="#policynames" title="PolicyNames">PolicyNames</a>: <i>
      - String</i>
</pre>

## Properties

#### LoadBalancerName

The load balancer to attach the policy to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerPort

The load balancer listener port to apply the policy to.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyNames

List of Policy Names to apply to the backend server.

_Required_: No

_Type_: List of String

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

