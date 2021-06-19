# TF::Kubernetes::ApiService SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cabundle" title="CaBundle">CaBundle</a>" : <i>String</i>,
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#grouppriorityminimum" title="GroupPriorityMinimum">GroupPriorityMinimum</a>" : <i>Double</i>,
    "<a href="#insecureskiptlsverify" title="InsecureSkipTlsVerify">InsecureSkipTlsVerify</a>" : <i>Boolean</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#versionpriority" title="VersionPriority">VersionPriority</a>" : <i>Double</i>,
    "<a href="#service" title="Service">Service</a>" : <i>[ <a href="servicedefinition.md">ServiceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cabundle" title="CaBundle">CaBundle</a>: <i>String</i>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#grouppriorityminimum" title="GroupPriorityMinimum">GroupPriorityMinimum</a>: <i>Double</i>
<a href="#insecureskiptlsverify" title="InsecureSkipTlsVerify">InsecureSkipTlsVerify</a>: <i>Boolean</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#versionpriority" title="VersionPriority">VersionPriority</a>: <i>Double</i>
<a href="#service" title="Service">Service</a>: <i>
      - <a href="servicedefinition.md">ServiceDefinition</a></i>
</pre>

## Properties

#### CaBundle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupPriorityMinimum

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsecureSkipTlsVerify

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionPriority

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="servicedefinition.md">ServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

