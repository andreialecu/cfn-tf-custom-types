# TF::OCI::LoadBalancerBackendSet

CloudFormation equivalent of oci_load_balancer_backendset

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::LoadBalancerBackendSet",
    "Properties" : {
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#healthchecker" title="HealthChecker">HealthChecker</a>" : <i>[ <a href="healthcheckerdefinition.md">HealthCheckerDefinition</a>, ... ]</i>,
        "<a href="#lbcookiesessionpersistenceconfiguration" title="LbCookieSessionPersistenceConfiguration">LbCookieSessionPersistenceConfiguration</a>" : <i>[ <a href="lbcookiesessionpersistenceconfigurationdefinition.md">LbCookieSessionPersistenceConfigurationDefinition</a>, ... ]</i>,
        "<a href="#sessionpersistenceconfiguration" title="SessionPersistenceConfiguration">SessionPersistenceConfiguration</a>" : <i>[ <a href="sessionpersistenceconfigurationdefinition.md">SessionPersistenceConfigurationDefinition</a>, ... ]</i>,
        "<a href="#sslconfiguration" title="SslConfiguration">SslConfiguration</a>" : <i>[ <a href="sslconfigurationdefinition.md">SslConfigurationDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::LoadBalancerBackendSet
Properties:
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#healthchecker" title="HealthChecker">HealthChecker</a>: <i>
      - <a href="healthcheckerdefinition.md">HealthCheckerDefinition</a></i>
    <a href="#lbcookiesessionpersistenceconfiguration" title="LbCookieSessionPersistenceConfiguration">LbCookieSessionPersistenceConfiguration</a>: <i>
      - <a href="lbcookiesessionpersistenceconfigurationdefinition.md">LbCookieSessionPersistenceConfigurationDefinition</a></i>
    <a href="#sessionpersistenceconfiguration" title="SessionPersistenceConfiguration">SessionPersistenceConfiguration</a>: <i>
      - <a href="sessionpersistenceconfigurationdefinition.md">SessionPersistenceConfigurationDefinition</a></i>
    <a href="#sslconfiguration" title="SslConfiguration">SslConfiguration</a>: <i>
      - <a href="sslconfigurationdefinition.md">SslConfigurationDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### LoadBalancerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthChecker

_Required_: No

_Type_: List of <a href="healthcheckerdefinition.md">HealthCheckerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbCookieSessionPersistenceConfiguration

_Required_: No

_Type_: List of <a href="lbcookiesessionpersistenceconfigurationdefinition.md">LbCookieSessionPersistenceConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionPersistenceConfiguration

_Required_: No

_Type_: List of <a href="sessionpersistenceconfigurationdefinition.md">SessionPersistenceConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslConfiguration

_Required_: No

_Type_: List of <a href="sslconfigurationdefinition.md">SslConfigurationDefinition</a>

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

#### Backend

Returns the <code>Backend</code> value.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

