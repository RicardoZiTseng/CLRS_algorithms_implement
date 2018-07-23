"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page 379 in chapter 24

BELLMAN-FOLD(G, w, s)
1   INITIALIZE-SINGLE-SOURCE(G, s)
2   for i = 1 to |G.V| - 1
3       for each edge(u, v) ∈ G.E
4           RELAX(u, v, w)
5   for each edge(u, v) ∈ G.E
6       if v.d > u.d + w(u, v)
7           return FALSE
8   return TRUE
"""
from pygraph.classes.digraph import digraph
from disjoint_set_data import tree_node

MAX_NUM = float('inf')

def initialize_single_source(g, s):
    """
    @param type: digraph, node_name
    @return type: dict
    """
    v2node = dict()
    for each in g.nodes():
        v = tree_node(each)
        v.d = MAX_NUM
        v.parent = None
        v2node[each] = v

    v2node[s].d = 0
    return v2node

def relax(g, u, v, v2node):
    """
    @param type: digraph, node_name, node_name, dict
    @return type: None
    """
    w_uv = g.edge_weight((u, v))
    u = v2node[u]
    v = v2node[v]
    if v.d > u.d + w_uv:
        v.d = u.d + w_uv
        v.parent = u.name

def bellman_fold(g, s):
    v2node = initialize_single_source(g, s)
    v_num = len(g.nodes())
    for i in range(1, v_num):
        for edge in g.edges():
            relax(g, edge[0], edge[1], v2node)
    for edge in g.edges():
        u = v2node[edge[0]]
        v = v2node[edge[1]]
        if v.d > u.d + g.edge_weight(edge):
            raise ValueError('no solution!')
    print("Complete")
    return v2node

def dag_shortest_paths(g, s):
    pass

def dijkstra(g, s):
    pass

if __name__ == '__main__':
    g = digraph()
    nodes = ['s', 't', 'x', 'y', 'z']
    g.add_nodes(nodes)
    g.add_edge(('s', 't'), 6)
    g.add_edge(('s', 'y'), 7)
    g.add_edge(('t', 'x'), 5)
    g.add_edge(('t', 'y'), 8)
    g.add_edge(('t', 'z'), -4)
    g.add_edge(('y', 'x'), -3)
    g.add_edge(('y', 'z'), 9)
    g.add_edge(('x', 't'), -2)
    g.add_edge(('z', 'x'), 7)
    g.add_edge(('z', 's'), 2)

    v2node = bellman_fold(g, 's')
    for each in v2node:
        print(each, v2node[each].parent)