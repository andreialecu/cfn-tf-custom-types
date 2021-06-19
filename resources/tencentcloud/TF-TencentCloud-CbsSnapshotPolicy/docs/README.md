# TF::TencentCloud::CbsSnapshotPolicy

Provides a snapshot policy resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::CbsSnapshotPolicy",
    "Properties" : {
        "<a href="#repeathours" title="RepeatHours">RepeatHours</a>" : <i>[ Double, ... ]</i>,
        "<a href="#repeatweekdays" title="RepeatWeekdays">RepeatWeekdays</a>" : <i>[ Double, ... ]</i>,
        "<a href="#retentiondays" title="RetentionDays">RetentionDays</a>" : <i>Double</i>,
        "<a href="#snapshotpolicyname" title="SnapshotPolicyName">SnapshotPolicyName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::CbsSnapshotPolicy
Properties:
    <a href="#repeathours" title="RepeatHours">RepeatHours</a>: <i>
      - Double</i>
    <a href="#repeatweekdays" title="RepeatWeekdays">RepeatWeekdays</a>: <i>
      - Double</i>
    <a href="#retentiondays" title="RetentionDays">RetentionDays</a>: <i>Double</i>
    <a href="#snapshotpolicyname" title="SnapshotPolicyName">SnapshotPolicyName</a>: <i>String</i>
</pre>

## Properties

#### RepeatHours

Trigger times of periodic snapshot. Valid value ranges: (0~23). The 0 means 00:00, and so on.

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepeatWeekdays

Periodic snapshot is enabled. Valid values: [0, 1, 2, 3, 4, 5, 6]. 0 means Sunday, 1-6 means Monday to Saturday.

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDays

Retention days of the snapshot, and the default value is 7.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotPolicyName

Name of snapshot policy. The maximum length can not exceed 60 bytes.

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

