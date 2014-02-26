#!/usr/bin/python
#title Connected components
#descr Provides the separate connected components of the device and node graph

import sys
import networkx
import group

if len(sys.argv) != 2:
    print 'Provide gexf file as argument'
    sys.exit(1)

def infoToFile(graph, file):
    cc = networkx.connected_components(graph.to_undirected())
    with open("connected_components_%s_size.txt" % file, 'w') as f:
        f.write("%i\n" % len(cc))

    with open("connected_components_%s.txt" % file, 'w') as f:
        for i,l in enumerate(cc):
            f.write("component %i\n" % i);
            for j,k in enumerate(l):
                f.write("    %s\n" % k);

G_orig = networkx.read_gexf(sys.argv[1],None,False)
G = group.deviceGraph(G_orig)
infoToFile(G_orig, "devicegraph")

G = group.nodeGraph(G_orig)
infoToFile(G_orig, "nodegraph")

