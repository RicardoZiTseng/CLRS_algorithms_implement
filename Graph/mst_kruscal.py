"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page 366 in chapter 23

Discription of the algorithms:
MST-KRUSKAL(G, w)
1   A = φ
2   for each vertex v ∈ G.V
3       MAKE-SET(v)
4   sort the edges of G.E in nonincreasing order by weight w
5   for each edge(u, v) ∈ G.E, taken in nondecreasing order by weight
6       if FIND-SET(u) ≠ FIND-SET(v)
7           A = A ∪ {(u, v)}
8           UNION(u, v)
9   return A
"""
from pygraph.classes.digraph import digraph
from disjoint_set_data import *

def mst_kruskal(g):
    """
    @param type: graph
    @return type: list
    """
    # edges = list()
    v2node = dict()
    A = list()
    
    for vertex in g.nodes():
        v = tree_node(vertex)
        v = make_set(v)
        v2node[vertex] = v

    edges = sorted(g.edges(), key = g.edge_weight)
    # print(edges)

    for edge in edges:
        u, v = v2node[edge[0]], v2node[edge[1]]
        if find_set(u) != find_set(v):
            A.append(edge)
            union(u, v)
    
    return A

if __name__ == '__main__':
    g = digraph()
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    g.add_nodes(nodes)
    g.add_edge(('a', 'b'), 4)
    g.add_edge(('b', 'c'), 8)
    g.add_edge(('a', 'h'), 8)
    g.add_edge(('b', 'h'), 11)
    g.add_edge(('h', 'i'), 7)
    g.add_edge(('h', 'g'), 1)
    g.add_edge(('i', 'g'), 6)
    g.add_edge(('i', 'c'), 2)
    g.add_edge(('c', 'd'), 7)
    g.add_edge(('c', 'f'), 4)
    g.add_edge(('g', 'f'), 2)
    g.add_edge(('d', 'e'), 9)
    g.add_edge(('d', 'f'), 14)
    g.add_edge(('e', 'f'), 10)
    
    A = mst_kruskal(g)
    print(A)