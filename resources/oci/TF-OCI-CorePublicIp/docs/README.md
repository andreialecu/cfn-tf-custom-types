# TF::OCI::CorePublicIp

This resource provides the Public Ip resource in Oracle Cloud Infrastructure Core service.

Creates a public IP. Use the `lifetime` property to specify whether it's an ephemeral or
reserved public IP. For information about limits on how many you can create, see
[Public IP Addresses](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

* **For an ephemeral public IP assigned to a private IP:** You must also specify a `privateIpId`
with the OCID of the primary private IP you want to assign the public IP to. The public IP is
created in the same availability domain as the private IP. An ephemeral public IP must always be
assigned to a private IP, and only to the *primary* private IP on a VNIC, not a secondary
private IP. Exception: If you create a [NatGateway](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/), Oracle
automatically assigns the NAT gateway a regional ephemeral public IP that you cannot remove.

* **For a reserved public IP:** You may also optional...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CorePublicIp",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#lifetime" title="Lifetime">Lifetime</a>" : <i>String</i>,
        "<a href="#privateipid" title="PrivateIpId">PrivateIpId</a>" : <i>String</i>,
        "<a href="#publicippoolid" title="PublicIpPoolId">PublicIpPoolId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CorePublicIp
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#lifetime" title="Lifetime">Lifetime</a>: <i>String</i>
    <a href="#privateipid" title="PrivateIpId">PrivateIpId</a>: <i>String</i>
    <a href="#publicippoolid" title="PublicIpPoolId">PublicIpPoolId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The OCID of the compartment to contain the public IP. For ephemeral public IPs, you must set this to the private IP's compartment OCID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifetime

Defines when the public IP is deleted and released back to the Oracle Cloud Infrastructure public IP pool. For more information, see [Public IP Addresses](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpId

(Updatable) The OCID of the private IP to assign the public IP to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpPoolId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.

_Required_: No

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

#### AssignedEntityId

Returns the <code>AssignedEntityId</code> value.

#### AssignedEntityType

Returns the <code>AssignedEntityType</code> value.

#### AvailabilityDomain

Returns the <code>AvailabilityDomain</code> value.

#### Id

Returns the <code>Id</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### Scope

Returns the <code>Scope</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

