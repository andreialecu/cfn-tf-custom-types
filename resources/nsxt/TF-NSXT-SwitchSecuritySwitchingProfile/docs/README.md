# TF::NSXT::SwitchSecuritySwitchingProfile

Provides a resource to configure switch security switching profile on NSX-T manager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::SwitchSecuritySwitchingProfile",
    "Properties" : {
        "<a href="#blockclientdhcp" title="BlockClientDhcp">BlockClientDhcp</a>" : <i>Boolean</i>,
        "<a href="#blocknonip" title="BlockNonIp">BlockNonIp</a>" : <i>Boolean</i>,
        "<a href="#blockserverdhcp" title="BlockServerDhcp">BlockServerDhcp</a>" : <i>Boolean</i>,
        "<a href="#bpdufilterenabled" title="BpduFilterEnabled">BpduFilterEnabled</a>" : <i>Boolean</i>,
        "<a href="#bpdufilterwhitelist" title="BpduFilterWhitelist">BpduFilterWhitelist</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#ratelimits" title="RateLimits">RateLimits</a>" : <i>[ <a href="ratelimitsdefinition.md">RateLimitsDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::SwitchSecuritySwitchingProfile
Properties:
    <a href="#blockclientdhcp" title="BlockClientDhcp">BlockClientDhcp</a>: <i>Boolean</i>
    <a href="#blocknonip" title="BlockNonIp">BlockNonIp</a>: <i>Boolean</i>
    <a href="#blockserverdhcp" title="BlockServerDhcp">BlockServerDhcp</a>: <i>Boolean</i>
    <a href="#bpdufilterenabled" title="BpduFilterEnabled">BpduFilterEnabled</a>: <i>Boolean</i>
    <a href="#bpdufilterwhitelist" title="BpduFilterWhitelist">BpduFilterWhitelist</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#ratelimits" title="RateLimits">RateLimits</a>: <i>
      - <a href="ratelimitsdefinition.md">RateLimitsDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### BlockClientDhcp

Indicates whether DHCP client blocking is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockNonIp

Indicates whether blocking of all traffic except IP/(G)ARP/BPDU is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockServerDhcp

Indicates whether DHCP server blocking is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BpduFilterEnabled

Indicates whether BPDU filter is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BpduFilterWhitelist

Set of allowed MAC addresses to be excluded from BPDU filtering, if enabled.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. Defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimits

_Required_: No

_Type_: List of <a href="ratelimitsdefinition.md">RateLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Revision

Returns the <code>Revision</code> value.

