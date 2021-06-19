# TF::AzureRM::KeyVault

Manages a Key Vault.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::KeyVault",
    "Properties" : {
        "<a href="#accesspolicy" title="AccessPolicy">AccessPolicy</a>" : <i>[ <a href="accesspolicydefinition.md">AccessPolicyDefinition</a>, ... ]</i>,
        "<a href="#enablerbacauthorization" title="EnableRbacAuthorization">EnableRbacAuthorization</a>" : <i>Boolean</i>,
        "<a href="#enabledfordeployment" title="EnabledForDeployment">EnabledForDeployment</a>" : <i>Boolean</i>,
        "<a href="#enabledfordiskencryption" title="EnabledForDiskEncryption">EnabledForDiskEncryption</a>" : <i>Boolean</i>,
        "<a href="#enabledfortemplatedeployment" title="EnabledForTemplateDeployment">EnabledForTemplateDeployment</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#purgeprotectionenabled" title="PurgeProtectionEnabled">PurgeProtectionEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#skuname" title="SkuName">SkuName</a>" : <i>String</i>,
        "<a href="#softdeleteenabled" title="SoftDeleteEnabled">SoftDeleteEnabled</a>" : <i>Boolean</i>,
        "<a href="#softdeleteretentiondays" title="SoftDeleteRetentionDays">SoftDeleteRetentionDays</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#contact" title="Contact">Contact</a>" : <i>[ <a href="contactdefinition.md">ContactDefinition</a>, ... ]</i>,
        "<a href="#networkacls" title="NetworkAcls">NetworkAcls</a>" : <i>[ <a href="networkaclsdefinition.md">NetworkAclsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::KeyVault
Properties:
    <a href="#accesspolicy" title="AccessPolicy">AccessPolicy</a>: <i>
      - <a href="accesspolicydefinition.md">AccessPolicyDefinition</a></i>
    <a href="#enablerbacauthorization" title="EnableRbacAuthorization">EnableRbacAuthorization</a>: <i>Boolean</i>
    <a href="#enabledfordeployment" title="EnabledForDeployment">EnabledForDeployment</a>: <i>Boolean</i>
    <a href="#enabledfordiskencryption" title="EnabledForDiskEncryption">EnabledForDiskEncryption</a>: <i>Boolean</i>
    <a href="#enabledfortemplatedeployment" title="EnabledForTemplateDeployment">EnabledForTemplateDeployment</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#purgeprotectionenabled" title="PurgeProtectionEnabled">PurgeProtectionEnabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#skuname" title="SkuName">SkuName</a>: <i>String</i>
    <a href="#softdeleteenabled" title="SoftDeleteEnabled">SoftDeleteEnabled</a>: <i>Boolean</i>
    <a href="#softdeleteretentiondays" title="SoftDeleteRetentionDays">SoftDeleteRetentionDays</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#contact" title="Contact">Contact</a>: <i>
      - <a href="contactdefinition.md">ContactDefinition</a></i>
    <a href="#networkacls" title="NetworkAcls">NetworkAcls</a>: <i>
      - <a href="networkaclsdefinition.md">NetworkAclsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessPolicy

[A list](/docs/configuration/attr-as-blocks.html) of up to 16 objects describing access policies, as described below.

_Required_: No

_Type_: List of <a href="accesspolicydefinition.md">AccessPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRbacAuthorization

Boolean flag to specify whether Azure Key Vault uses Role Based Access Control (RBAC) for authorization of data actions. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnabledForDeployment

Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnabledForDiskEncryption

Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnabledForTemplateDeployment

Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Key Vault. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PurgeProtectionEnabled

Is Purge Protection enabled for this Key Vault? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkuName

The Name of the SKU used for this Key Vault. Possible values are `standard` and `premium`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftDeleteEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftDeleteRetentionDays

The number of days that items should be retained for once soft-deleted. This value can be between `7` and `90` (the default) days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contact

_Required_: No

_Type_: List of <a href="contactdefinition.md">ContactDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkAcls

_Required_: No

_Type_: List of <a href="networkaclsdefinition.md">NetworkAclsDefinition</a>

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

#### VaultUri

Returns the <code>VaultUri</code> value.

