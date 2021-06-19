# TF::Google::DatastoreIndex

Describes a composite index for Cloud Datastore.


To get more information about Index, see:

* [API documentation](https://cloud.google.com/datastore/docs/reference/admin/rest/v1/projects.indexes)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/datastore/docs/concepts/indexes)

~> **Warning:** This resource creates a Datastore Index on a project that has already
enabled a Datastore-compatible database. If you haven't already enabled
one, you can create a `google_app_engine_application` resource with
`database_type` set to `"CLOUD_DATASTORE_COMPATIBILITY"` to do so. Your
Datastore location will be the same as the App Engine location specified.

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=datastore_index&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_e...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::DatastoreIndex",
    "Properties" : {
        "<a href="#ancestor" title="Ancestor">Ancestor</a>" : <i>String</i>,
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="propertiesdefinition.md">PropertiesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::DatastoreIndex
Properties:
    <a href="#ancestor" title="Ancestor">Ancestor</a>: <i>String</i>
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="propertiesdefinition.md">PropertiesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Ancestor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kind

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of <a href="propertiesdefinition.md">PropertiesDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### IndexId

Returns the <code>IndexId</code> value.

