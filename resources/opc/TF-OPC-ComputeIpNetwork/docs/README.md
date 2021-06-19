# TF::OPC::ComputeIpNetwork

The ``opc_compute_ip_network`` resource creates and manages an IP Network in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OPC::ComputeIpNetwork",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ipaddressprefix" title="IpAddressPrefix">IpAddressPrefix</a>" : <i>String</i>,
        "<a href="#ipnetworkexchange" title="IpNetworkExchange">IpNetworkExchange</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#publicnaptenabled" title="PublicNaptEnabled">PublicNaptEnabled</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::OPC::ComputeIpNetwork
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ipaddressprefix" title="IpAddressPrefix">IpAddressPrefix</a>: <i>String</i>
    <a href="#ipnetworkexchange" title="IpNetworkExchange">IpNetworkExchange</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#publicnaptenabled" title="PublicNaptEnabled">PublicNaptEnabled</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### Description

The description of the IP Network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddressPrefix

The IPv4 address prefix, in CIDR format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNetworkExchange

Specify the IP Network exchange to which the IP Network belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the IP Network. Changing this name forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicNaptEnabled

If true, enable public internet access using NAPT for VNICs without any public IP Reservation. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

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

#### Uri

Returns the <code>Uri</code> value.

