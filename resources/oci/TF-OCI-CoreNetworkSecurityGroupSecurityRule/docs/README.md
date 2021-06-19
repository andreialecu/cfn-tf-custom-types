# TF::OCI::CoreNetworkSecurityGroupSecurityRule

This resource provides the Network Security Group Security Rule resource in Oracle Cloud Infrastructure Core service.

Adds a security rule to the specified network security group.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CoreNetworkSecurityGroupSecurityRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#destinationtype" title="DestinationType">DestinationType</a>" : <i>String</i>,
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
        "<a href="#stateless" title="Stateless">Stateless</a>" : <i>Boolean</i>,
        "<a href="#icmpoptions" title="IcmpOptions">IcmpOptions</a>" : <i>[ <a href="icmpoptionsdefinition.md">IcmpOptionsDefinition</a>, ... ]</i>,
        "<a href="#tcpoptions" title="TcpOptions">TcpOptions</a>" : <i>[ <a href="tcpoptionsdefinition.md">TcpOptionsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#udpoptions" title="UdpOptions">UdpOptions</a>" : <i>[ <a href="udpoptionsdefinition.md">UdpOptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CoreNetworkSecurityGroupSecurityRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#destinationtype" title="DestinationType">DestinationType</a>: <i>String</i>
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
    <a href="#stateless" title="Stateless">Stateless</a>: <i>Boolean</i>
    <a href="#icmpoptions" title="IcmpOptions">IcmpOptions</a>: <i>
      - <a href="icmpoptionsdefinition.md">IcmpOptionsDefinition</a></i>
    <a href="#tcpoptions" title="TcpOptions">TcpOptions</a>: <i>
      - <a href="tcpoptionsdefinition.md">TcpOptionsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#udpoptions" title="UdpOptions">UdpOptions</a>: <i>
      - <a href="udpoptionsdefinition.md">UdpOptionsDefinition</a></i>
</pre>

## Properties

#### Description

An optional description of your choice for the rule. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

Conceptually, this is the range of IP addresses that a packet originating from the instance can go to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationType

Type of destination for the rule. Required if `direction` = `EGRESS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The transport protocol. Specify either `all` or an IPv4 protocol number as defined in [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). Options are supported only for ICMP ("1"), TCP ("6"), UDP ("17"), and ICMPv6 ("58").

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Conceptually, this is the range of IP addresses that a packet coming into the instance can come from.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

Type of source for the rule. Required if `direction` = `INGRESS`.
* `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.
* `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a [Service](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic coming from a particular `Service` through a service gateway).
* `NETWORK_SECURITY_GROUP`: If the rule's `source` is the OCID of a [NetworkSecurityGroup](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateless

A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpOptions

_Required_: No

_Type_: List of <a href="icmpoptionsdefinition.md">IcmpOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpOptions

_Required_: No

_Type_: List of <a href="tcpoptionsdefinition.md">TcpOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpOptions

_Required_: No

_Type_: List of <a href="udpoptionsdefinition.md">UdpOptionsDefinition</a>

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

#### IsValid

Returns the <code>IsValid</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

