# TF::GitHub::Team

Provides a GitHub team resource.

This resource allows you to add/remove teams from your organization. When applied,
a new team will be created. When destroyed, that team will be removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::Team",
    "Properties" : {
        "<a href="#createdefaultmaintainer" title="CreateDefaultMaintainer">CreateDefaultMaintainer</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ldapdn" title="LdapDn">LdapDn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentteamid" title="ParentTeamId">ParentTeamId</a>" : <i>Double</i>,
        "<a href="#privacy" title="Privacy">Privacy</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::Team
Properties:
    <a href="#createdefaultmaintainer" title="CreateDefaultMaintainer">CreateDefaultMaintainer</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ldapdn" title="LdapDn">LdapDn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentteamid" title="ParentTeamId">ParentTeamId</a>: <i>Double</i>
    <a href="#privacy" title="Privacy">Privacy</a>: <i>String</i>
</pre>

## Properties

#### CreateDefaultMaintainer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the team.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapDn

The LDAP Distinguished Name of the group where membership will be synchronized. Only available in GitHub Enterprise Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the team.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentTeamId

The ID of the parent team, if this is a nested team.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privacy

The level of privacy for the team. Must be one of `secret` or `closed`.
Defaults to `secret`.

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

#### Etag

Returns the <code>Etag</code> value.

#### Id

Returns the <code>Id</code> value.

#### MembersCount

Returns the <code>MembersCount</code> value.

#### NodeId

Returns the <code>NodeId</code> value.

#### Slug

Returns the <code>Slug</code> value.

