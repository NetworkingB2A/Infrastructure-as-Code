What is VxLan?
- it it helps reducing the need for Spanning tree, trucking
- It allows you to put a Layer 2 network overlay with a layer 3 underlay
- Standard based - RFC XXX

Vlan 
- id is 12 bits long
- which allows for 4095 vlans
- Concept if you have customers in your data center
  - if you gave each customer 8 vlans, you only have room for 511 customers

VxLan
- VNI = VxLAN Network Identifier
- A VNI is a bridge domain
- Traffic is encapsulated with UDP and IP 
- VNI work just like Vlans. if you want to go between VNIs you will need a router.
- Changes to the Underlay does not impact the Overlay. as long as there is ip connectivity.
- id is 24 bits long
- 16,777,216 segments

VTEPs
- Is a special kind of interface  
- VTEPs connects the overlay to the underlay
- VTEP has a ip address in the underlay and 1 or more VNIs
- traffic between a source and destination VTEP create a stateless tunnel. the tunnel is formed long enough to pass the VxLan frame in the tunnel
- When traffic comes to a VTEP, the VTEP will encapsulate the traffic and sent that traffic to the remote VTEP to be decapsulated.
- The VTEPS are on the leaf switches.
- VxLAN tunnels are created on leaf switches.
- If you use BGP Spine switches can become Route-Reflectors.

Encapsulation of a data using VxLAN
Ethernet|IP|UDP|VxLAN|frame

VxLAN header -  Total of 64 Bits
reserved - 8-bits
VNI - 24-bits: The VxLAN ID
Reserved - 24-Bits
Flags - 8-bit; Bit-3 shows VNI is valid

Things to know
- UDP destination port is 4789 
- Know that you will need to have Jumbo frames enabled for best results
- ECMP (Equal-cost Multipath) routing will help significantly with this strategy. 
- if your fabric starts to grow too large, you can break up the design into more spine/leaves. At this point you would add a Super-spine. (Not used very often)

What about Routers/Firewalls/Load Balancers/ETC?
- This functionality is added to the Leaf layer.
- When routers/Firewalls are added to a leaf, the leaf becomes a boarder leaf.
- Boarder leaf switches represent connectivity to and from the fabric.


Thoughts to help me understand
- it seems like frame that is already constructed goes to the VTEP. The VTEP encapsulated the frame adds VxLAN tag( for lack of a better word). once the frame has the new VxLAN header, the frame brought back up to layer 4, and starts again.