# TF::NSXT::LbHttpRequestRewriteRule UriArgumentsConditionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#casesensitive" title="CaseSensitive">CaseSensitive</a>" : <i>Boolean</i>,
    "<a href="#inverse" title="Inverse">Inverse</a>" : <i>Boolean</i>,
    "<a href="#matchtype" title="MatchType">MatchType</a>" : <i>String</i>,
    "<a href="#uriarguments" title="UriArguments">UriArguments</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#casesensitive" title="CaseSensitive">CaseSensitive</a>: <i>Boolean</i>
<a href="#inverse" title="Inverse">Inverse</a>: <i>Boolean</i>
<a href="#matchtype" title="MatchType">MatchType</a>: <i>String</i>
<a href="#uriarguments" title="UriArguments">UriArguments</a>: <i>String</i>
</pre>

## Properties

#### CaseSensitive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inverse

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriArguments

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

