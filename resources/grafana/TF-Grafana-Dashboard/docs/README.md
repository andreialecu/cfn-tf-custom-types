# TF::Grafana::Dashboard

CloudFormation equivalent of grafana_dashboard

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Grafana::Dashboard",
    "Properties" : {
        "<a href="#configjson" title="ConfigJson">ConfigJson</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Grafana::Dashboard
Properties:
    <a href="#configjson" title="ConfigJson">ConfigJson</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>Double</i>
</pre>

## Properties

#### ConfigJson

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DashboardId

Returns the <code>DashboardId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Slug

Returns the <code>Slug</code> value.

