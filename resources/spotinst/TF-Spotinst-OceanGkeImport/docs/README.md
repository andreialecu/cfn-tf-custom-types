# TF::Spotinst::OceanGkeImport

Manages a Spotinst Ocean GKE resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Spotinst::OceanGkeImport",
    "Properties" : {
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#controllerclusterid" title="ControllerClusterId">ControllerClusterId</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#whitelist" title="Whitelist">Whitelist</a>" : <i>[ String, ... ]</i>,
        "<a href="#autoscaler" title="Autoscaler">Autoscaler</a>" : <i>[ <a href="autoscalerdefinition.md">AutoscalerDefinition</a>, ... ]</i>,
        "<a href="#backendservices" title="BackendServices">BackendServices</a>" : <i>[ <a href="backendservicesdefinition.md">BackendServicesDefinition</a>, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ <a href="scheduledtaskdefinition.md">ScheduledTaskDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Spotinst::OceanGkeImport
Properties:
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#controllerclusterid" title="ControllerClusterId">ControllerClusterId</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#whitelist" title="Whitelist">Whitelist</a>: <i>
      - String</i>
    <a href="#autoscaler" title="Autoscaler">Autoscaler</a>: <i>
      - <a href="autoscalerdefinition.md">AutoscalerDefinition</a></i>
    <a href="#backendservices" title="BackendServices">BackendServices</a>: <i>
      - <a href="backendservicesdefinition.md">BackendServicesDefinition</a></i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - <a href="scheduledtaskdefinition.md">ScheduledTaskDefinition</a></i>
</pre>

## Properties

#### ClusterName

The GKE cluster name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

The number of instances to launch and maintain in the cluster.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The zone the master cluster is located in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

The upper limit of instances the cluster can scale up to.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

The lower limit of instances the cluster can scale down to.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelist

Instance types allowed in the Ocean cluster.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaler

_Required_: No

_Type_: List of <a href="autoscalerdefinition.md">AutoscalerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendServices

_Required_: No

_Type_: List of <a href="backendservicesdefinition.md">BackendServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTask

_Required_: No

_Type_: List of <a href="scheduledtaskdefinition.md">ScheduledTaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClusterControllerId

Returns the <code>ClusterControllerId</code> value.

#### Id

Returns the <code>Id</code> value.

