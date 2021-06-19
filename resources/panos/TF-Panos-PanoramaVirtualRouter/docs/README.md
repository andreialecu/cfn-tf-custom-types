# TF::Panos::PanoramaVirtualRouter

This resource allows you to add/update/delete Panorama virtual routers
for templates.

**Note** - The `default` virtual router may be configured with this resource,
however it will not be deleted from Panorama.  It will only be unexported
from the vsys that it is currently imported in, and any interfaces imported
into the virtual router will be removed.

This resource has some overlap with the `panos_panorama_virtual_router_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_virtual_router` spec does not define the
`interfaces` field.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaVirtualRouter",
    "Properties" : {
        "<a href="#ebgpdist" title="EbgpDist">EbgpDist</a>" : <i>Double</i>,
        "<a href="#ecmphashseed" title="EcmpHashSeed">EcmpHashSeed</a>" : <i>Double</i>,
        "<a href="#ecmphashsourceonly" title="EcmpHashSourceOnly">EcmpHashSourceOnly</a>" : <i>Boolean</i>,
        "<a href="#ecmphashuseport" title="EcmpHashUsePort">EcmpHashUsePort</a>" : <i>Boolean</i>,
        "<a href="#ecmploadbalancemethod" title="EcmpLoadBalanceMethod">EcmpLoadBalanceMethod</a>" : <i>String</i>,
        "<a href="#ecmpmaxpath" title="EcmpMaxPath">EcmpMaxPath</a>" : <i>Double</i>,
        "<a href="#ecmpstrictsourcepath" title="EcmpStrictSourcePath">EcmpStrictSourcePath</a>" : <i>Boolean</i>,
        "<a href="#ecmpsymmetricreturn" title="EcmpSymmetricReturn">EcmpSymmetricReturn</a>" : <i>Boolean</i>,
        "<a href="#ecmpweightedroundrobininterfaces" title="EcmpWeightedRoundRobinInterfaces">EcmpWeightedRoundRobinInterfaces</a>" : <i>[ <a href="ecmpweightedroundrobininterfacesdefinition.md">EcmpWeightedRoundRobinInterfacesDefinition</a>, ... ]</i>,
        "<a href="#enableecmp" title="EnableEcmp">EnableEcmp</a>" : <i>Boolean</i>,
        "<a href="#ibgpdist" title="IbgpDist">IbgpDist</a>" : <i>Double</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ospfextdist" title="OspfExtDist">OspfExtDist</a>" : <i>Double</i>,
        "<a href="#ospfintdist" title="OspfIntDist">OspfIntDist</a>" : <i>Double</i>,
        "<a href="#ospfv3extdist" title="Ospfv3ExtDist">Ospfv3ExtDist</a>" : <i>Double</i>,
        "<a href="#ospfv3intdist" title="Ospfv3IntDist">Ospfv3IntDist</a>" : <i>Double</i>,
        "<a href="#ripdist" title="RipDist">RipDist</a>" : <i>Double</i>,
        "<a href="#staticdist" title="StaticDist">StaticDist</a>" : <i>Double</i>,
        "<a href="#staticipv6dist" title="StaticIpv6Dist">StaticIpv6Dist</a>" : <i>Double</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::PanoramaVirtualRouter
Properties:
    <a href="#ebgpdist" title="EbgpDist">EbgpDist</a>: <i>Double</i>
    <a href="#ecmphashseed" title="EcmpHashSeed">EcmpHashSeed</a>: <i>Double</i>
    <a href="#ecmphashsourceonly" title="EcmpHashSourceOnly">EcmpHashSourceOnly</a>: <i>Boolean</i>
    <a href="#ecmphashuseport" title="EcmpHashUsePort">EcmpHashUsePort</a>: <i>Boolean</i>
    <a href="#ecmploadbalancemethod" title="EcmpLoadBalanceMethod">EcmpLoadBalanceMethod</a>: <i>String</i>
    <a href="#ecmpmaxpath" title="EcmpMaxPath">EcmpMaxPath</a>: <i>Double</i>
    <a href="#ecmpstrictsourcepath" title="EcmpStrictSourcePath">EcmpStrictSourcePath</a>: <i>Boolean</i>
    <a href="#ecmpsymmetricreturn" title="EcmpSymmetricReturn">EcmpSymmetricReturn</a>: <i>Boolean</i>
    <a href="#ecmpweightedroundrobininterfaces" title="EcmpWeightedRoundRobinInterfaces">EcmpWeightedRoundRobinInterfaces</a>: <i>
      - <a href="ecmpweightedroundrobininterfacesdefinition.md">EcmpWeightedRoundRobinInterfacesDefinition</a></i>
    <a href="#enableecmp" title="EnableEcmp">EnableEcmp</a>: <i>Boolean</i>
    <a href="#ibgpdist" title="IbgpDist">IbgpDist</a>: <i>Double</i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ospfextdist" title="OspfExtDist">OspfExtDist</a>: <i>Double</i>
    <a href="#ospfintdist" title="OspfIntDist">OspfIntDist</a>: <i>Double</i>
    <a href="#ospfv3extdist" title="Ospfv3ExtDist">Ospfv3ExtDist</a>: <i>Double</i>
    <a href="#ospfv3intdist" title="Ospfv3IntDist">Ospfv3IntDist</a>: <i>Double</i>
    <a href="#ripdist" title="RipDist">RipDist</a>: <i>Double</i>
    <a href="#staticdist" title="StaticDist">StaticDist</a>: <i>Double</i>
    <a href="#staticipv6dist" title="StaticIpv6Dist">StaticIpv6Dist</a>: <i>Double</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
</pre>

## Properties

#### EbgpDist

Admin distance - EBGP (default: `20`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpHashSeed

For `ecmp_load_balance_method` = `ip-hash`:
User-specified hash seed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpHashSourceOnly

For `ecmp_load_balance_method` = `ip-hash`:
Only use source address for hash.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpHashUsePort

For `ecmp_load_balance_method` = `ip-hash`:
Use source/destination port for hash.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpLoadBalanceMethod

Load balancing algorithm.  Valid
values are `ip-modulo`, `ip-hash`, `weighted-round-robin`, or
`balanced-round-robin`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpMaxPath

Maximum number of ECMP paths supported.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpStrictSourcePath

Force VPN traffic to exit interface
that the source-ip belongs to.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpSymmetricReturn

Allows return packets to egress out
of the ingress interface of the flow.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpWeightedRoundRobinInterfaces

For `ecmp_load_balance_method` =
`weighted-round-robin`: Interface weight used in weighted ECMP load balancing.

_Required_: No

_Type_: List of <a href="ecmpweightedroundrobininterfacesdefinition.md">EcmpWeightedRoundRobinInterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEcmp

Enable ECMP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IbgpDist

Admin distance - IBGP (default: `200`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

List of interfaces that should use this virtual
router.  If you intend to use the `panos_panorama_virtual_router_entry`
resource, then you should leave this param unspecified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The virtual router's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfExtDist

Admin distance - OSPF Ext (default: `110`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfIntDist

Admin distance - OSPF Int (default: `30`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospfv3ExtDist

Admin distance - OSPFv3 Ext (default:
`110`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospfv3IntDist

Admin distance - OSPFv3 Int (default:
`30`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RipDist

Admin distance - RIP (default: `120`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticDist

Admin distance - Static (default: `10`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpv6Dist

Admin distance - Static IPv6 (default: `10`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys that will use this virtual router.  This should
be something like `vsys1` or `vsys3`.

_Required_: No

_Type_: String

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

