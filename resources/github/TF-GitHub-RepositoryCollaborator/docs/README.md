# TF::GitHub::RepositoryCollaborator

Provides a GitHub repository collaborator resource.

This resource allows you to add/remove collaborators from repositories in your
organization or personal account. For organization repositories, collaborators can
have explicit (and differing levels of) read, write, or administrator access to 
specific repositories, without giving the user full organization membership. 
For personal repositories, collaborators can only be granted write
(implictly includes read) permission. 

When applied, an invitation will be sent to the user to become a collaborator
on a repository. When destroyed, either the invitation will be cancelled or the
collaborator will be removed from the repository.

Further documentation on GitHub collaborators:

- [Adding outside collaborators to your personal repositories](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-access-to-your-personal-repositories)
- [Adding outside collaborators to repositories in your organization](https://help.github...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::RepositoryCollaborator",
    "Properties" : {
        "<a href="#permission" title="Permission">Permission</a>" : <i>String</i>,
        "<a href="#permissiondiffsuppression" title="PermissionDiffSuppression">PermissionDiffSuppression</a>" : <i>Boolean</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::RepositoryCollaborator
Properties:
    <a href="#permission" title="Permission">Permission</a>: <i>String</i>
    <a href="#permissiondiffsuppression" title="PermissionDiffSuppression">PermissionDiffSuppression</a>: <i>Boolean</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### Permission

The permission of the outside collaborator for the repository.
Must be one of `pull`, `push`, `maintain`, `triage` or `admin` for organization-owned repositories.
Must be `push` for personal repositories. Defaults to `push`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionDiffSuppression

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

The GitHub repository.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The user to add to the repository as a collaborator.

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

#### InvitationId

Returns the <code>InvitationId</code> value.

