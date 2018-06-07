"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page 350 in chapter 22

Discription of the algorithms:
DFS(G)
1   for each vertex u belong to G.V
2       u.color = WHITE  //which means the vertex u does not been traveled
3       u.pi = NULL
4   for each vertex u belong to G.V
5       if u.color == WHITE
6           DFS-VISIT(G, u)
DFS-VISIT(G, u) 
1   u.color = BLACK
2   for each v belong to G:Adj[u]
3       if v.color == WHITE
4           v.pi = u
5           DFS-VISIT(G, v)   
"""
from pygraph.classes.graph import graph

class DFSResults:
    def __init__(self):
        self.level = dict()
        self.parent = dict()
        self.time = dict()
        self.t = -1

def dfs(g):
    result = DFSResults()
    for vertex in g.nodes:
        if vertex not in g.parent:
            dfs_visit(g, vertex, result)
    return result

def dfs_visit(g, node, result, parent = None):
    result.parent[node] = parent
    for each in g.neighbors(node):
        if each not in result.parent:
            dfs_visit(g, each, result, node)
    result.t += 1
    result.time[node] = result.t

if __name__ == '__main__':
    pass


