# TF::BIGIP::SysIapp

`bigip_sys_iapp` resource helps you to deploy Application Services template that can be used to automate and orchestrate Layer 4-7 applications service deployments using F5 Network.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::SysIapp",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="Devicegroup">Devicegroup</a>" : <i>String</i>,
        "<a href="#executeaction" title="ExecuteAction">ExecuteAction</a>" : <i>String</i>,
        "<a href="#inheriteddevicegroup" title="InheritedDevicegroup">InheritedDevicegroup</a>" : <i>String</i>,
        "<a href="#inheritedtrafficgroup" title="InheritedTrafficGroup">InheritedTrafficGroup</a>" : <i>String</i>,
        "<a href="#jsonfile" title="Jsonfile">Jsonfile</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partition" title="Partition">Partition</a>" : <i>String</i>,
        "<a href="#strictupdates" title="StrictUpdates">StrictUpdates</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatemodified" title="TemplateModified">TemplateModified</a>" : <i>String</i>,
        "<a href="#templateprerequisiteerrors" title="TemplatePrerequisiteErrors">TemplatePrerequisiteErrors</a>" : <i>String</i>,
        "<a href="#trafficgroup" title="TrafficGroup">TrafficGroup</a>" : <i>String</i>,
        "<a href="#lists" title="Lists">Lists</a>" : <i>[ <a href="listsdefinition.md">ListsDefinition</a>, ... ]</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#tables" title="Tables">Tables</a>" : <i>[ <a href="tablesdefinition.md">TablesDefinition</a>, ... ]</i>,
        "<a href="#variables" title="Variables">Variables</a>" : <i>[ <a href="variablesdefinition.md">VariablesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::SysIapp
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="Devicegroup">Devicegroup</a>: <i>String</i>
    <a href="#executeaction" title="ExecuteAction">ExecuteAction</a>: <i>String</i>
    <a href="#inheriteddevicegroup" title="InheritedDevicegroup">InheritedDevicegroup</a>: <i>String</i>
    <a href="#inheritedtrafficgroup" title="InheritedTrafficGroup">InheritedTrafficGroup</a>: <i>String</i>
    <a href="#jsonfile" title="Jsonfile">Jsonfile</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partition" title="Partition">Partition</a>: <i>String</i>
    <a href="#strictupdates" title="StrictUpdates">StrictUpdates</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatemodified" title="TemplateModified">TemplateModified</a>: <i>String</i>
    <a href="#templateprerequisiteerrors" title="TemplatePrerequisiteErrors">TemplatePrerequisiteErrors</a>: <i>String</i>
    <a href="#trafficgroup" title="TrafficGroup">TrafficGroup</a>: <i>String</i>
    <a href="#lists" title="Lists">Lists</a>: <i>
      - <a href="listsdefinition.md">ListsDefinition</a></i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#tables" title="Tables">Tables</a>: <i>
      - <a href="tablesdefinition.md">TablesDefinition</a></i>
    <a href="#variables" title="Variables">Variables</a>: <i>
      - <a href="variablesdefinition.md">VariablesDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devicegroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecuteAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InheritedDevicegroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InheritedTrafficGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jsonfile

Refer to the Json file which will be deployed on F5 BIG-IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the iApp.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Partition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictUpdates

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateModified

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePrerequisiteErrors

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lists

_Required_: No

_Type_: List of <a href="listsdefinition.md">ListsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tables

_Required_: No

_Type_: List of <a href="tablesdefinition.md">TablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variables

_Required_: No

_Type_: List of <a href="variablesdefinition.md">VariablesDefinition</a>

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

