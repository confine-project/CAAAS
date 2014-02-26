import networkx

def deviceGraph(G):
    F = networkx.Graph();
    for n,nd in G.nodes_iter(data=True):
        if not 'pid' in nd:
            F.add_node(n,nd)
    for u,v,ed in G.edges_iter(data=True):
        ud = G.node[u]
        vd = G.node[v]
        if 'pid' in ud or 'pid' in vd:
            F.add_edge(ud['pid'] if 'pid' in ud else u, vd['pid'] if 'pid' in vd else v, ed)
    return F
    
def nodeGraph(G):
    G = deviceGraph(G)
    F = networkx.Graph()
    
    merge = dict();
    for n in G.nodes_iter():
        if n in merge:
            continue
        seen = set([n])
        todo = set([n])
        while len(todo) > 0:
            m = todo.pop();
            neighs = wiredNeighbours(G,m)
            todo = todo.union(neighs.difference(seen))
            seen = seen.union(neighs)
        for m in seen:
            if len(m) > len(n):
                n = m
        for m in seen:
            if m != n:
                merge[m] = n
        F.add_node(n,G.node[n]);
    
    for u,v,ed in G.edges_iter(data=True):
        if 'type' in ed and ed['type'] != 'wired':
            F.add_edge(merge[u] if u in merge else u, merge[v] if v in merge else v, ed)
    return F

def wiredNeighbours(G, n):
    wired = set([]);
    for u,v,ed in G.edges_iter(nbunch=n, data=True):
        if 'type' in ed and ed['type'] == 'wired':
            wired.add(v)
    return wired
