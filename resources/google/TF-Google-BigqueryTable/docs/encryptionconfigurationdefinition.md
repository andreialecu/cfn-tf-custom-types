# TF::Google::BigqueryTable EncryptionConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kmskeyname" title="KmsKeyName">KmsKeyName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#kmskeyname" title="KmsKeyName">KmsKeyName</a>: <i>String</i>
</pre>

## Properties

#### KmsKeyName

The self link or full name of a key which should be used to
encrypt this table.  Note that the default bigquery service account will need to have
encrypt/decrypt permissions on this key - you may want to see the
`google_bigquery_default_service_account` datasource and the
`google_kms_crypto_key_iam_binding` resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

