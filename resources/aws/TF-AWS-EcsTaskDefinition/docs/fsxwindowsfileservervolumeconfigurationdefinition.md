# TF::AWS::EcsTaskDefinition FsxWindowsFileServerVolumeConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filesystemid" title="FileSystemId">FileSystemId</a>" : <i>String</i>,
    "<a href="#rootdirectory" title="RootDirectory">RootDirectory</a>" : <i>String</i>,
    "<a href="#authorizationconfig" title="AuthorizationConfig">AuthorizationConfig</a>" : <i>[ <a href="authorizationconfigdefinition.md">AuthorizationConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#filesystemid" title="FileSystemId">FileSystemId</a>: <i>String</i>
<a href="#rootdirectory" title="RootDirectory">RootDirectory</a>: <i>String</i>
<a href="#authorizationconfig" title="AuthorizationConfig">AuthorizationConfig</a>: <i>
      - <a href="authorizationconfigdefinition.md">AuthorizationConfigDefinition</a></i>
</pre>

## Properties

#### FileSystemId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootDirectory

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationConfig

_Required_: No

_Type_: List of <a href="authorizationconfigdefinition.md">AuthorizationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

