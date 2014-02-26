#!/usr/bin/python
#title Closeness centrality
#descr Calculates the closeness centrality for each node

import sys
import networkx
import group

if len(sys.argv) != 2:
    print 'Provide gexf file as argument'
    sys.exit(1)

def infoToFile(graph, file):
    cc = networkx.closeness_centrality(graph.to_undirected())
    with open("closeness_centrality_%s.txt" % file, 'w') as f:
        for i in sorted(cc, key=cc.get, reverse=True):
            f.write("%s %f\n" % (i, cc[i]));

G_orig = networkx.read_gexf(sys.argv[1],None,False)
G = group.nodeGraph(G_orig)
infoToFile(G, "nodegraph")
