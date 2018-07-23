"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page 369 in chapter 23

Discription of the algorithms:
MST-PRIM(G, w, r)
1   for each u ∈ G.V
2       u:key = ∞
3       u:π = NIL
4   r:key = 0
5   Q = G.V
6   while Q ≠ φ
7       u = EXTRACT-MIN(Q)
8       for each v ∈ G.Adj[u]
9           if v ∈ Q and w(u, v) < v.key
10              v.π = u
11              v.key = w(u, v)
"""

from pygraph.classes.digraph import digraph
from disjoint_set_data import *

MAX_NUM = float('inf')

def mst_prim(g, r):
    """
    @param type: graph, tree_node
    @return type: None
    """
    pass