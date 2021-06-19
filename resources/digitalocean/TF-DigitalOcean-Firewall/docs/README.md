# TF::DigitalOcean::Firewall

Provides a DigitalOcean Cloud Firewall resource. This can be used to create,
modify, and delete Firewalls.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::Firewall",
    "Properties" : {
        "<a href="#dropletids" title="DropletIds">DropletIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#inboundrule" title="InboundRule">InboundRule</a>" : <i>[ <a href="inboundruledefinition.md">InboundRuleDefinition</a>, ... ]</i>,
        "<a href="#outboundrule" title="OutboundRule">OutboundRule</a>" : <i>[ <a href="outboundruledefinition.md">OutboundRuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::Firewall
Properties:
    <a href="#dropletids" title="DropletIds">DropletIds</a>: <i>
      - Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#inboundrule" title="InboundRule">InboundRule</a>: <i>
      - <a href="inboundruledefinition.md">InboundRuleDefinition</a></i>
    <a href="#outboundrule" title="OutboundRule">OutboundRule</a>: <i>
      - <a href="outboundruledefinition.md">OutboundRuleDefinition</a></i>
</pre>

## Properties

#### DropletIds

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Firewall name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundRule

_Required_: No

_Type_: List of <a href="inboundruledefinition.md">InboundRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundRule

_Required_: No

_Type_: List of <a href="outboundruledefinition.md">OutboundRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### PendingChanges

Returns the <code>PendingChanges</code> value.

#### Status

Returns the <code>Status</code> value.

