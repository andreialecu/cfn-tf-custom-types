# TF::ECL::NetworkSubnetV2 HostRoutesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationcidr" title="DestinationCidr">DestinationCidr</a>" : <i>String</i>,
    "<a href="#nexthop" title="NextHop">NextHop</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#destinationcidr" title="DestinationCidr">DestinationCidr</a>: <i>String</i>
<a href="#nexthop" title="NextHop">NextHop</a>: <i>String</i>
</pre>

## Properties

#### DestinationCidr

The destination CIDR.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHop

The next hop in the route.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

