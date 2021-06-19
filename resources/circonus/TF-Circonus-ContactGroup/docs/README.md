# TF::Circonus::ContactGroup

The ``circonus_contact_group`` resource creates and manages a
[Circonus Contact Group](https://login.circonus.com/user/docs/Alerting/ContactGroups).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Circonus::ContactGroup",
    "Properties" : {
        "<a href="#aggregationwindow" title="AggregationWindow">AggregationWindow</a>" : <i>String</i>,
        "<a href="#alwayssendclear" title="AlwaysSendClear">AlwaysSendClear</a>" : <i>Boolean</i>,
        "<a href="#grouptype" title="GroupType">GroupType</a>" : <i>String</i>,
        "<a href="#longmessage" title="LongMessage">LongMessage</a>" : <i>String</i>,
        "<a href="#longsubject" title="LongSubject">LongSubject</a>" : <i>String</i>,
        "<a href="#longsummary" title="LongSummary">LongSummary</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#shortmessage" title="ShortMessage">ShortMessage</a>" : <i>String</i>,
        "<a href="#shortsummary" title="ShortSummary">ShortSummary</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#alertoption" title="AlertOption">AlertOption</a>" : <i>[ <a href="alertoptiondefinition.md">AlertOptionDefinition</a>, ... ]</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ <a href="emaildefinition.md">EmailDefinition</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="httpdefinition.md">HttpDefinition</a>, ... ]</i>,
        "<a href="#pagerduty" title="PagerDuty">PagerDuty</a>" : <i>[ <a href="pagerdutydefinition.md">PagerDutyDefinition</a>, ... ]</i>,
        "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slackdefinition.md">SlackDefinition</a>, ... ]</i>,
        "<a href="#sms" title="Sms">Sms</a>" : <i>[ <a href="smsdefinition.md">SmsDefinition</a>, ... ]</i>,
        "<a href="#victorops" title="Victorops">Victorops</a>" : <i>[ <a href="victoropsdefinition.md">VictoropsDefinition</a>, ... ]</i>,
        "<a href="#xmpp" title="Xmpp">Xmpp</a>" : <i>[ <a href="xmppdefinition.md">XmppDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Circonus::ContactGroup
Properties:
    <a href="#aggregationwindow" title="AggregationWindow">AggregationWindow</a>: <i>String</i>
    <a href="#alwayssendclear" title="AlwaysSendClear">AlwaysSendClear</a>: <i>Boolean</i>
    <a href="#grouptype" title="GroupType">GroupType</a>: <i>String</i>
    <a href="#longmessage" title="LongMessage">LongMessage</a>: <i>String</i>
    <a href="#longsubject" title="LongSubject">LongSubject</a>: <i>String</i>
    <a href="#longsummary" title="LongSummary">LongSummary</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#shortmessage" title="ShortMessage">ShortMessage</a>: <i>String</i>
    <a href="#shortsummary" title="ShortSummary">ShortSummary</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#alertoption" title="AlertOption">AlertOption</a>: <i>
      - <a href="alertoptiondefinition.md">AlertOptionDefinition</a></i>
    <a href="#email" title="Email">Email</a>: <i>
      - <a href="emaildefinition.md">EmailDefinition</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="httpdefinition.md">HttpDefinition</a></i>
    <a href="#pagerduty" title="PagerDuty">PagerDuty</a>: <i>
      - <a href="pagerdutydefinition.md">PagerDutyDefinition</a></i>
    <a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slackdefinition.md">SlackDefinition</a></i>
    <a href="#sms" title="Sms">Sms</a>: <i>
      - <a href="smsdefinition.md">SmsDefinition</a></i>
    <a href="#victorops" title="Victorops">Victorops</a>: <i>
      - <a href="victoropsdefinition.md">VictoropsDefinition</a></i>
    <a href="#xmpp" title="Xmpp">Xmpp</a>: <i>
      - <a href="xmppdefinition.md">XmppDefinition</a></i>
</pre>

## Properties

#### AggregationWindow

The aggregation window for batching up alert
notifications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlwaysSendClear

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongMessage

The bulk of the message used in long form alert
messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongSubject

The subject used in long form alert messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongSummary

The brief summary used in long form alert messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the contact group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortMessage

The subject used in short form alert messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortSummary

The brief summary used in short form alert
messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags attached to the Contact Group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertOption

_Required_: No

_Type_: List of <a href="alertoptiondefinition.md">AlertOptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of <a href="emaildefinition.md">EmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="httpdefinition.md">HttpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PagerDuty

_Required_: No

_Type_: List of <a href="pagerdutydefinition.md">PagerDutyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slack

_Required_: No

_Type_: List of <a href="slackdefinition.md">SlackDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sms

_Required_: No

_Type_: List of <a href="smsdefinition.md">SmsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Victorops

_Required_: No

_Type_: List of <a href="victoropsdefinition.md">VictoropsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Xmpp

_Required_: No

_Type_: List of <a href="xmppdefinition.md">XmppDefinition</a>

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

#### LastModified

Returns the <code>LastModified</code> value.

#### LastModifiedBy

Returns the <code>LastModifiedBy</code> value.

