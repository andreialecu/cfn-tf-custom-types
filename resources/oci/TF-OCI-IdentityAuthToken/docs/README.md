# TF::OCI::IdentityAuthToken

This resource provides the Auth Token resource in Oracle Cloud Infrastructure Identity service.

Creates a new auth token for the specified user. For information about what auth tokens are for, see
[Managing User Credentials](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm).

You must specify a *description* for the auth token (although it can be an empty string). It does not
have to be unique, and you can change it anytime with
[UpdateAuthToken](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/AuthToken/UpdateAuthToken).

Every user has permission to create an auth token for *their own user ID*. An administrator in your organization
does not need to write a policy to give users this ability. To compare, administrators who have permission to the
tenancy can use this operation to create an auth token for any user, including themselves.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::IdentityAuthToken",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::IdentityAuthToken
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

(Updatable) The description you assign to the auth token during creation. Does not have to be unique, and it's changeable.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

The OCID of the user.

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

#### InactiveState

Returns the <code>InactiveState</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeExpires

Returns the <code>TimeExpires</code> value.

#### Token

Returns the <code>Token</code> value.

