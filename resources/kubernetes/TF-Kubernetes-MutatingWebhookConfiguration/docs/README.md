# TF::Kubernetes::MutatingWebhookConfiguration

CloudFormation equivalent of kubernetes_mutating_webhook_configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Kubernetes::MutatingWebhookConfiguration",
    "Properties" : {
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#webhook" title="Webhook">Webhook</a>" : <i>[ <a href="webhookdefinition.md">WebhookDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Kubernetes::MutatingWebhookConfiguration
Properties:
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#webhook" title="Webhook">Webhook</a>: <i>
      - <a href="webhookdefinition.md">WebhookDefinition</a></i>
</pre>

## Properties

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

_Required_: No

_Type_: List of <a href="webhookdefinition.md">WebhookDefinition</a>

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

