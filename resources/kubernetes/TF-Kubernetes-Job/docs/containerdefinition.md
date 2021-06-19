# TF::Kubernetes::Job ContainerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#args" title="Args">Args</a>" : <i>[ String, ... ]</i>,
    "<a href="#command" title="Command">Command</a>" : <i>[ String, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#imagepullpolicy" title="ImagePullPolicy">ImagePullPolicy</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#stdin" title="Stdin">Stdin</a>" : <i>Boolean</i>,
    "<a href="#stdinonce" title="StdinOnce">StdinOnce</a>" : <i>Boolean</i>,
    "<a href="#terminationmessagepath" title="TerminationMessagePath">TerminationMessagePath</a>" : <i>String</i>,
    "<a href="#terminationmessagepolicy" title="TerminationMessagePolicy">TerminationMessagePolicy</a>" : <i>String</i>,
    "<a href="#tty" title="Tty">Tty</a>" : <i>Boolean</i>,
    "<a href="#workingdir" title="WorkingDir">WorkingDir</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ <a href="envdefinition.md">EnvDefinition</a>, ... ]</i>,
    "<a href="#envfrom" title="EnvFrom">EnvFrom</a>" : <i>[ <a href="envfromdefinition.md">EnvFromDefinition</a>, ... ]</i>,
    "<a href="#lifecycle" title="Lifecycle">Lifecycle</a>" : <i>[ <a href="lifecycledefinition.md">LifecycleDefinition</a>, ... ]</i>,
    "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ <a href="livenessprobedefinition.md">LivenessProbeDefinition</a>, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>[ <a href="portdefinition.md">PortDefinition</a>, ... ]</i>,
    "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ <a href="readinessprobedefinition.md">ReadinessProbeDefinition</a>, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resourcesdefinition.md">ResourcesDefinition</a>, ... ]</i>,
    "<a href="#securitycontext" title="SecurityContext">SecurityContext</a>" : <i>[ <a href="securitycontextdefinition.md">SecurityContextDefinition</a>, ... ]</i>,
    "<a href="#startupprobe" title="StartupProbe">StartupProbe</a>" : <i>[ <a href="startupprobedefinition.md">StartupProbeDefinition</a>, ... ]</i>,
    "<a href="#volumemount" title="VolumeMount">VolumeMount</a>" : <i>[ <a href="volumemountdefinition.md">VolumeMountDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#args" title="Args">Args</a>: <i>
      - String</i>
<a href="#command" title="Command">Command</a>: <i>
      - String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#imagepullpolicy" title="ImagePullPolicy">ImagePullPolicy</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#stdin" title="Stdin">Stdin</a>: <i>Boolean</i>
<a href="#stdinonce" title="StdinOnce">StdinOnce</a>: <i>Boolean</i>
<a href="#terminationmessagepath" title="TerminationMessagePath">TerminationMessagePath</a>: <i>String</i>
<a href="#terminationmessagepolicy" title="TerminationMessagePolicy">TerminationMessagePolicy</a>: <i>String</i>
<a href="#tty" title="Tty">Tty</a>: <i>Boolean</i>
<a href="#workingdir" title="WorkingDir">WorkingDir</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>
      - <a href="envdefinition.md">EnvDefinition</a></i>
<a href="#envfrom" title="EnvFrom">EnvFrom</a>: <i>
      - <a href="envfromdefinition.md">EnvFromDefinition</a></i>
<a href="#lifecycle" title="Lifecycle">Lifecycle</a>: <i>
      - <a href="lifecycledefinition.md">LifecycleDefinition</a></i>
<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - <a href="livenessprobedefinition.md">LivenessProbeDefinition</a></i>
<a href="#port" title="Port">Port</a>: <i>
      - <a href="portdefinition.md">PortDefinition</a></i>
<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - <a href="readinessprobedefinition.md">ReadinessProbeDefinition</a></i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resourcesdefinition.md">ResourcesDefinition</a></i>
<a href="#securitycontext" title="SecurityContext">SecurityContext</a>: <i>
      - <a href="securitycontextdefinition.md">SecurityContextDefinition</a></i>
<a href="#startupprobe" title="StartupProbe">StartupProbe</a>: <i>
      - <a href="startupprobedefinition.md">StartupProbeDefinition</a></i>
<a href="#volumemount" title="VolumeMount">VolumeMount</a>: <i>
      - <a href="volumemountdefinition.md">VolumeMountDefinition</a></i>
</pre>

## Properties

#### Args

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stdin

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StdinOnce

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationMessagePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationMessagePolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tty

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of <a href="envdefinition.md">EnvDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvFrom

_Required_: No

_Type_: List of <a href="envfromdefinition.md">EnvFromDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifecycle

_Required_: No

_Type_: List of <a href="lifecycledefinition.md">LifecycleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No

_Type_: List of <a href="livenessprobedefinition.md">LivenessProbeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="portdefinition.md">PortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No

_Type_: List of <a href="readinessprobedefinition.md">ReadinessProbeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resourcesdefinition.md">ResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityContext

_Required_: No

_Type_: List of <a href="securitycontextdefinition.md">SecurityContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartupProbe

_Required_: No

_Type_: List of <a href="startupprobedefinition.md">StartupProbeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMount

_Required_: No

_Type_: List of <a href="volumemountdefinition.md">VolumeMountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

