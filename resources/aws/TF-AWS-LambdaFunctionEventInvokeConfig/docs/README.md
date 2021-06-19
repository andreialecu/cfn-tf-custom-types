# TF::AWS::LambdaFunctionEventInvokeConfig

Manages an asynchronous invocation configuration for a Lambda Function or Alias. More information about asynchronous invocations and the configurable values can be found in the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LambdaFunctionEventInvokeConfig",
    "Properties" : {
        "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
        "<a href="#maximumeventageinseconds" title="MaximumEventAgeInSeconds">MaximumEventAgeInSeconds</a>" : <i>Double</i>,
        "<a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>" : <i>Double</i>,
        "<a href="#qualifier" title="Qualifier">Qualifier</a>" : <i>String</i>,
        "<a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>" : <i>[ <a href="destinationconfigdefinition.md">DestinationConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LambdaFunctionEventInvokeConfig
Properties:
    <a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
    <a href="#maximumeventageinseconds" title="MaximumEventAgeInSeconds">MaximumEventAgeInSeconds</a>: <i>Double</i>
    <a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>: <i>Double</i>
    <a href="#qualifier" title="Qualifier">Qualifier</a>: <i>String</i>
    <a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>: <i>
      - <a href="destinationconfigdefinition.md">DestinationConfigDefinition</a></i>
</pre>

## Properties

#### FunctionName

Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumEventAgeInSeconds

Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumRetryAttempts

Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Qualifier

Lambda Function published version, `$LATEST`, or Lambda Alias name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationConfig

_Required_: No

_Type_: List of <a href="destinationconfigdefinition.md">DestinationConfigDefinition</a>

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

