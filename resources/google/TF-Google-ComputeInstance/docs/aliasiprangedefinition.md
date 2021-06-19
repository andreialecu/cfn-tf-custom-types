# TF::Google::ComputeInstance AliasIpRangeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipcidrrange" title="IpCidrRange">IpCidrRange</a>" : <i>String</i>,
    "<a href="#subnetworkrangename" title="SubnetworkRangeName">SubnetworkRangeName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ipcidrrange" title="IpCidrRange">IpCidrRange</a>: <i>String</i>
<a href="#subnetworkrangename" title="SubnetworkRangeName">SubnetworkRangeName</a>: <i>String</i>
</pre>

## Properties

#### IpCidrRange

The IP CIDR range represented by this alias IP range. This IP CIDR range
must belong to the specified subnetwork and cannot contain IP addresses reserved by
system or used by other network interfaces. This range may be a single IP address
(e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetworkRangeName

The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range. If left unspecified, the primary range of the subnetwork will be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

