"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page 324 in chapter 21

Discription of the algorithms:
CONNECTED-COMPONENT(G): calculate the component of a undirected graph
1   for each vertex v ∈ G.V
2       MAKE-SET(v)
3   for each edge(u, v) ∈ G.E
4       if FIND-SET(u) ≠ FIND-SET(v)
5           UNION(u, v)

SAME-COMPONENT(u, v): judge if the node u and v are in the component
1   if FIND-SET(u) == FIND-SET(v)
2       return TRUE
3   else
4       return FALSE
"""
from pygraph.classes.graph import graph

class tree_node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.rank = None
        self.key = None #which defined for the mst_prim algorithm in page 369
        self.d = None # which defined for the graph shortest path in chapter 24

def make_set(x):
    """
    @param type: tree_node
    @return type: tree_node
    """
    x.parent = x
    x.rank = 0
    return x

def link(x, y):
    """
    @param type: tree_node, tree_node
    @return type: None
    """
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank = y.rank + 1

def find_set(x):
    """
    @param type: tree_node
    @return type: None
    """
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent

def union(x, y):
    """
    @param type: tree_node, tree_node
    @return type: None
    """
    link(find_set(x), find_set(y))

def connected_components(g):
    v2node = dict()
    # sets = list()
    component = dict()
    for vertex in g.nodes():
        v = tree_node(vertex)
        v = make_set(v)
        v2node[vertex] = v

    for edge in g.edges():
        u, v = v2node[edge[0]], v2node[edge[1]]
        if find_set(u) != find_set(v):
            union(u, v)

    for vertex in g.nodes():
        node = v2node[vertex]
        node_parent = node.parent.name
        if node_parent not in component:
            component[node_parent] = [vertex]
        else:
            component[node_parent].append(vertex)
    
    return component, v2node
        
def same_component(u, v, v2node):
    u = v2node[u]
    v = v2node[v]
    if find_set(u) == find_set(v):
        return True
    else:
        return False

if __name__ == '__main__':
    g = graph()
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    g.add_nodes(nodes)
    g.add_edge(('a', 'c'))
    g.add_edge(('a', 'b'))
    g.add_edge(('c', 'b'))
    g.add_edge(('b', 'd'))
    g.add_edge(('e', 'g'))
    g.add_edge(('e', 'f'))
    g.add_edge(('h', 'i'))

    component, v2node = connected_components(g)
    print(component)
    print(same_component('a', 'e', v2node))