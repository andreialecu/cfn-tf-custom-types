# TF::AWS::SagemakerModel ContainerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#containerhostname" title="ContainerHostname">ContainerHostname</a>" : <i>String</i>,
    "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="environmentdefinition.md">EnvironmentDefinition</a>, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#modeldataurl" title="ModelDataUrl">ModelDataUrl</a>" : <i>String</i>,
    "<a href="#imageconfig" title="ImageConfig">ImageConfig</a>" : <i>[ <a href="imageconfigdefinition.md">ImageConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#containerhostname" title="ContainerHostname">ContainerHostname</a>: <i>String</i>
<a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="environmentdefinition.md">EnvironmentDefinition</a></i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#modeldataurl" title="ModelDataUrl">ModelDataUrl</a>: <i>String</i>
<a href="#imageconfig" title="ImageConfig">ImageConfig</a>: <i>
      - <a href="imageconfigdefinition.md">ImageConfigDefinition</a></i>
</pre>

## Properties

#### ContainerHostname

The DNS host name for the container.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

Environment variables for the Docker container.
A list of key value pairs.

_Required_: No

_Type_: List of <a href="environmentdefinition.md">EnvironmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

The registry path where the inference code image is stored in Amazon ECR.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The container hosts value `SingleModel/MultiModel`. The default value is `SingleModel`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModelDataUrl

The URL for the S3 location where model artifacts are stored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageConfig

_Required_: No

_Type_: List of <a href="imageconfigdefinition.md">ImageConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

