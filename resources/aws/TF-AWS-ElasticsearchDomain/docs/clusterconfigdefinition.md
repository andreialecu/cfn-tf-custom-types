# TF::AWS::ElasticsearchDomain ClusterConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dedicatedmastercount" title="DedicatedMasterCount">DedicatedMasterCount</a>" : <i>Double</i>,
    "<a href="#dedicatedmasterenabled" title="DedicatedMasterEnabled">DedicatedMasterEnabled</a>" : <i>Boolean</i>,
    "<a href="#dedicatedmastertype" title="DedicatedMasterType">DedicatedMasterType</a>" : <i>String</i>,
    "<a href="#instancecount" title="InstanceCount">InstanceCount</a>" : <i>Double</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#warmcount" title="WarmCount">WarmCount</a>" : <i>Double</i>,
    "<a href="#warmenabled" title="WarmEnabled">WarmEnabled</a>" : <i>Boolean</i>,
    "<a href="#warmtype" title="WarmType">WarmType</a>" : <i>String</i>,
    "<a href="#zoneawarenessenabled" title="ZoneAwarenessEnabled">ZoneAwarenessEnabled</a>" : <i>Boolean</i>,
    "<a href="#zoneawarenessconfig" title="ZoneAwarenessConfig">ZoneAwarenessConfig</a>" : <i>[ <a href="zoneawarenessconfigdefinition.md">ZoneAwarenessConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dedicatedmastercount" title="DedicatedMasterCount">DedicatedMasterCount</a>: <i>Double</i>
<a href="#dedicatedmasterenabled" title="DedicatedMasterEnabled">DedicatedMasterEnabled</a>: <i>Boolean</i>
<a href="#dedicatedmastertype" title="DedicatedMasterType">DedicatedMasterType</a>: <i>String</i>
<a href="#instancecount" title="InstanceCount">InstanceCount</a>: <i>Double</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#warmcount" title="WarmCount">WarmCount</a>: <i>Double</i>
<a href="#warmenabled" title="WarmEnabled">WarmEnabled</a>: <i>Boolean</i>
<a href="#warmtype" title="WarmType">WarmType</a>: <i>String</i>
<a href="#zoneawarenessenabled" title="ZoneAwarenessEnabled">ZoneAwarenessEnabled</a>: <i>Boolean</i>
<a href="#zoneawarenessconfig" title="ZoneAwarenessConfig">ZoneAwarenessConfig</a>: <i>
      - <a href="zoneawarenessconfigdefinition.md">ZoneAwarenessConfigDefinition</a></i>
</pre>

## Properties

#### DedicatedMasterCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedMasterEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedMasterType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarmCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarmEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarmType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneAwarenessEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneAwarenessConfig

_Required_: No

_Type_: List of <a href="zoneawarenessconfigdefinition.md">ZoneAwarenessConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

