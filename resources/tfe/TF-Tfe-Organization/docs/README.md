# TF::Tfe::Organization

Manages organizations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Tfe::Organization",
    "Properties" : {
        "<a href="#collaboratorauthpolicy" title="CollaboratorAuthPolicy">CollaboratorAuthPolicy</a>" : <i>String</i>,
        "<a href="#costestimationenabled" title="CostEstimationEnabled">CostEstimationEnabled</a>" : <i>Boolean</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ownersteamsamlroleid" title="OwnersTeamSamlRoleId">OwnersTeamSamlRoleId</a>" : <i>String</i>,
        "<a href="#sessionrememberminutes" title="SessionRememberMinutes">SessionRememberMinutes</a>" : <i>Double</i>,
        "<a href="#sessiontimeoutminutes" title="SessionTimeoutMinutes">SessionTimeoutMinutes</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Tfe::Organization
Properties:
    <a href="#collaboratorauthpolicy" title="CollaboratorAuthPolicy">CollaboratorAuthPolicy</a>: <i>String</i>
    <a href="#costestimationenabled" title="CostEstimationEnabled">CostEstimationEnabled</a>: <i>Boolean</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ownersteamsamlroleid" title="OwnersTeamSamlRoleId">OwnersTeamSamlRoleId</a>: <i>String</i>
    <a href="#sessionrememberminutes" title="SessionRememberMinutes">SessionRememberMinutes</a>: <i>Double</i>
    <a href="#sessiontimeoutminutes" title="SessionTimeoutMinutes">SessionTimeoutMinutes</a>: <i>Double</i>
</pre>

## Properties

#### CollaboratorAuthPolicy

Authentication policy (`password`
or `two_factor_mandatory`). Defaults to `password`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CostEstimationEnabled

Whether or not the cost estimation feature is enabled for all workspaces in the organization. Defaults to true. In a Terraform Cloud organization which does not have Teams & Governance features, this value is always false and cannot be changed. In Terraform Enterprise, Cost Estimation must also be enabled in Site Administration.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

Admin email address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the organization.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnersTeamSamlRoleId

The name of the "owners" team.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionRememberMinutes

Session expiration. Defaults to
`20160`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTimeoutMinutes

Session timeout after inactivity.
Defaults to `20160`.

_Required_: No

_Type_: Double

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

