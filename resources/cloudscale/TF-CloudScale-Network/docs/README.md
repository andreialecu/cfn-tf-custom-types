# TF::CloudScale::Network

Provides a cloudscale.ch Private Network resource. This can be used to create, modify, and delete networks.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudScale::Network",
    "Properties" : {
        "<a href="#autocreateipv4subnet" title="AutoCreateIpv4Subnet">AutoCreateIpv4Subnet</a>" : <i>Boolean</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#zoneslug" title="ZoneSlug">ZoneSlug</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudScale::Network
Properties:
    <a href="#autocreateipv4subnet" title="AutoCreateIpv4Subnet">AutoCreateIpv4Subnet</a>: <i>Boolean</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#zoneslug" title="ZoneSlug">ZoneSlug</a>: <i>String</i>
</pre>

## Properties

#### AutoCreateIpv4Subnet

Automatically create an IPv4 Subnet on the network. Can be `true` (default) or `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

You can specify the MTU size for the network, defaults to 9000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneSlug

You can specify a zone slug. Options include `lpg1` and `rma1`.

_Required_: No

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

#### Href

Returns the <code>Href</code> value.

#### Id

Returns the <code>Id</code> value.

#### Subnets

Returns the <code>Subnets</code> value.

