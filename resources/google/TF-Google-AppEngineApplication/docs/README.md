# TF::Google::AppEngineApplication

Allows creation and management of an App Engine application.

~> App Engine applications cannot be deleted once they're created; you have to delete the
   entire project to delete the application. Terraform will report the application has been
   successfully deleted; this is a limitation of Terraform, and will go away in the future.
   Terraform is not able to delete App Engine applications.

~> **Warning:** All arguments including `iap.oauth2_client_secret` will be stored in the raw
state as plain-text. [Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::AppEngineApplication",
    "Properties" : {
        "<a href="#authdomain" title="AuthDomain">AuthDomain</a>" : <i>String</i>,
        "<a href="#databasetype" title="DatabaseType">DatabaseType</a>" : <i>String</i>,
        "<a href="#locationid" title="LocationId">LocationId</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#servingstatus" title="ServingStatus">ServingStatus</a>" : <i>String</i>,
        "<a href="#featuresettings" title="FeatureSettings">FeatureSettings</a>" : <i>[ <a href="featuresettingsdefinition.md">FeatureSettingsDefinition</a>, ... ]</i>,
        "<a href="#iap" title="Iap">Iap</a>" : <i>[ <a href="iapdefinition.md">IapDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::AppEngineApplication
Properties:
    <a href="#authdomain" title="AuthDomain">AuthDomain</a>: <i>String</i>
    <a href="#databasetype" title="DatabaseType">DatabaseType</a>: <i>String</i>
    <a href="#locationid" title="LocationId">LocationId</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#servingstatus" title="ServingStatus">ServingStatus</a>: <i>String</i>
    <a href="#featuresettings" title="FeatureSettings">FeatureSettings</a>: <i>
      - <a href="featuresettingsdefinition.md">FeatureSettingsDefinition</a></i>
    <a href="#iap" title="Iap">Iap</a>: <i>
      - <a href="iapdefinition.md">IapDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AuthDomain

The domain to authenticate users with when using App Engine's User API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseType

The type of the Cloud Firestore or Cloud Datastore database associated with this application.
Can be `CLOUD_FIRESTORE` or `CLOUD_DATASTORE_COMPATIBILITY` for new
instances.  To support old instances, the value `CLOUD_DATASTORE` is accepted
by the provider, but will be rejected by the API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationId

The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The project ID to create the application under.
~>**NOTE:** GCP only accepts project ID, not project number. If you are using number,
you may get a "Permission denied" error.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServingStatus

The serving status of the app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureSettings

_Required_: No

_Type_: List of <a href="featuresettingsdefinition.md">FeatureSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iap

_Required_: No

_Type_: List of <a href="iapdefinition.md">IapDefinition</a>

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

#### AppId

Returns the <code>AppId</code> value.

#### CodeBucket

Returns the <code>CodeBucket</code> value.

#### DefaultBucket

Returns the <code>DefaultBucket</code> value.

#### DefaultHostname

Returns the <code>DefaultHostname</code> value.

#### GcrDomain

Returns the <code>GcrDomain</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### UrlDispatchRule

Returns the <code>UrlDispatchRule</code> value.

