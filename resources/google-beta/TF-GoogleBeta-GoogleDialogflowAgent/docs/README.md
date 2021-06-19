# TF::GoogleBeta::GoogleDialogflowAgent

CloudFormation equivalent of google_dialogflow_agent

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleDialogflowAgent",
    "Properties" : {
        "<a href="#apiversion" title="ApiVersion">ApiVersion</a>" : <i>String</i>,
        "<a href="#avataruri" title="AvatarUri">AvatarUri</a>" : <i>String</i>,
        "<a href="#classificationthreshold" title="ClassificationThreshold">ClassificationThreshold</a>" : <i>Double</i>,
        "<a href="#defaultlanguagecode" title="DefaultLanguageCode">DefaultLanguageCode</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enablelogging" title="EnableLogging">EnableLogging</a>" : <i>Boolean</i>,
        "<a href="#matchmode" title="MatchMode">MatchMode</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#supportedlanguagecodes" title="SupportedLanguageCodes">SupportedLanguageCodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleDialogflowAgent
Properties:
    <a href="#apiversion" title="ApiVersion">ApiVersion</a>: <i>String</i>
    <a href="#avataruri" title="AvatarUri">AvatarUri</a>: <i>String</i>
    <a href="#classificationthreshold" title="ClassificationThreshold">ClassificationThreshold</a>: <i>Double</i>
    <a href="#defaultlanguagecode" title="DefaultLanguageCode">DefaultLanguageCode</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enablelogging" title="EnableLogging">EnableLogging</a>: <i>Boolean</i>
    <a href="#matchmode" title="MatchMode">MatchMode</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#supportedlanguagecodes" title="SupportedLanguageCodes">SupportedLanguageCodes</a>: <i>
      - String</i>
    <a href="#tier" title="Tier">Tier</a>: <i>String</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ApiVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvatarUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassificationThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLanguageCode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportedLanguageCodes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvatarUriBackend

Returns the <code>AvatarUriBackend</code> value.

#### Id

Returns the <code>Id</code> value.

