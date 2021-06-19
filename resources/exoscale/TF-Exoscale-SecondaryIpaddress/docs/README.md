# TF::Exoscale::SecondaryIpaddress

Provides a resource for assigning an existing Exoscale [Elastic IP][r-ipaddress] to a [Compute instance][r-compute].

~> **NOTE:** The network interfaces of the Compute instance itself still have to be configured accordingly (unless using a *managed* Elastic IP).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Exoscale::SecondaryIpaddress",
    "Properties" : {
        "<a href="#computeid" title="ComputeId">ComputeId</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Exoscale::SecondaryIpaddress
Properties:
    <a href="#computeid" title="ComputeId">ComputeId</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ComputeId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### NetworkId

Returns the <code>NetworkId</code> value.

#### NicId

Returns the <code>NicId</code> value.

