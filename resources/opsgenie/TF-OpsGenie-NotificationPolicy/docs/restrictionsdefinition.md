# TF::OpsGenie::NotificationPolicy RestrictionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endday" title="EndDay">EndDay</a>" : <i>String</i>,
    "<a href="#endhour" title="EndHour">EndHour</a>" : <i>Double</i>,
    "<a href="#endmin" title="EndMin">EndMin</a>" : <i>Double</i>,
    "<a href="#startday" title="StartDay">StartDay</a>" : <i>String</i>,
    "<a href="#starthour" title="StartHour">StartHour</a>" : <i>Double</i>,
    "<a href="#startmin" title="StartMin">StartMin</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#endday" title="EndDay">EndDay</a>: <i>String</i>
<a href="#endhour" title="EndHour">EndHour</a>: <i>Double</i>
<a href="#endmin" title="EndMin">EndMin</a>: <i>Double</i>
<a href="#startday" title="StartDay">StartDay</a>: <i>String</i>
<a href="#starthour" title="StartHour">StartHour</a>: <i>Double</i>
<a href="#startmin" title="StartMin">StartMin</a>: <i>Double</i>
</pre>

## Properties

#### EndDay

Ending day of restriction (eg. `wednesday`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndHour

Ending hour of restriction on defined `end_day`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndMin

Ending minute of restriction on defined `end_hour`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDay

Starting day of restriction (eg. `monday`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartHour

Starting hour of restriction on defined `start_day`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartMin

Staring minute of restriction on defined `start_hour`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

