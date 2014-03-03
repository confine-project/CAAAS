# CAAAS tutorial

## Supported input file
Currently the following input files describing the network are supported:
* GEXF

### GEXF

#### Structure

In this section we describe how the GEXF format describes the community network. A logical community node in the network consists of a number of routing boards and antenna devices, all located on the same site and interconnected with wires.  A logical node can thus be broken down in antenna devices and routing boards.  The antenna devices are used to let the interfaces of the routing boards on different logical nodes to communicate with each other and consist of a wired connection to the router board and a wireless connection to the antenna device of another logical node.  The routing boards them self are made up of multiple interfaces, combining multiple connections with other logical nodes on a single board.  Each interface has its own metrics such as transmitted packet count, link speed, ... . For this reason, the GEXF format is used as follows:

* Each routing board is an GEXF node.
* Each interface of the routing board is a GEXF node with the parent id equal to the id of its routing board.
* Each antenna device is a GEXF node.
* Each wired connection within the logical node, is a directed GEXF edge between the interface GEXF nodes.
* Each wireless connection between logical nodes, is a directed GEXF edge between the interface GEXF nodes.

Consider the following example.
![Example of two logical nodes](images/example.png)

This would result in the following GEXF file structure:

	<gexf>
		<graph>
			<nodes>
				<!-- logical node A -->
				<node id="11" label="Router board A"/>
				<node id="12" label="Interface A1" pid="11"/>
				<node id="13" label="Interface A2" pid="11"/>
				
				<node id="14" label="Antenna device A1"/>
				<node id="15" label="Antenna device A2"/>
				
				<!-- logical node B -->
				<node id="21" label="Router board B"/>
				<node id="22" label="Interface B1" pid="21"/>
				<node id="23" label="Interface B2" pid "21"/>
				
				<node id="24" label="Antenna device B1"/>
				<node id="25" label="Antenna device B2"/>
			</nodes>
			<edges>
				<!-- wired edges in logical node A -->
				<edge id="1" source="12" target="14"/>
				<edge id="2" source="13" target="15"/>
				
				<!-- wired edges in logical node B -->
				<edge id="3" source="22" target="24"/>
				<edge id="4" source="23" target="25"/>
				
				<!-- wireless edge between logical node A  and B -->
				<edge id="5" source="14" target="24"/>
			</edges>
		<graph>
	</gexf>

If the logical node graph is needed for certain metrics, first the nodes with the same PID should be joined together.  Also the edges should be rewritten to aim at the joined node for the routing boards. Then the wired edges can be merged into a single node. Also here the edges should be renamed.

#### Attributes

