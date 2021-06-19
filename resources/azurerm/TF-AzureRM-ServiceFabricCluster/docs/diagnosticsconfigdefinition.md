# TF::AzureRM::ServiceFabricCluster DiagnosticsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blobendpoint" title="BlobEndpoint">BlobEndpoint</a>" : <i>String</i>,
    "<a href="#protectedaccountkeyname" title="ProtectedAccountKeyName">ProtectedAccountKeyName</a>" : <i>String</i>,
    "<a href="#queueendpoint" title="QueueEndpoint">QueueEndpoint</a>" : <i>String</i>,
    "<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>" : <i>String</i>,
    "<a href="#tableendpoint" title="TableEndpoint">TableEndpoint</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#blobendpoint" title="BlobEndpoint">BlobEndpoint</a>: <i>String</i>
<a href="#protectedaccountkeyname" title="ProtectedAccountKeyName">ProtectedAccountKeyName</a>: <i>String</i>
<a href="#queueendpoint" title="QueueEndpoint">QueueEndpoint</a>: <i>String</i>
<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>: <i>String</i>
<a href="#tableendpoint" title="TableEndpoint">TableEndpoint</a>: <i>String</i>
</pre>

## Properties

#### BlobEndpoint

The Blob Endpoint of the Storage Account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectedAccountKeyName

The protected diagnostics storage key name, such as `StorageAccountKey1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueEndpoint

The Queue Endpoint of the Storage Account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountName

The name of the Storage Account where the Diagnostics should be sent to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableEndpoint

The Table Endpoint of the Storage Account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

