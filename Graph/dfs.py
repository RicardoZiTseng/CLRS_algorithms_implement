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
# you need to add the library of pygraph, the github address is here: https://github.com/Shoobx/python-graph

class DFSResults:
    def __init__(self):
        self.level = dict()
        self.parent = dict()


def dfs(g):
    results = DFSResults()
    for each in g.nodes():
        if each not in results.parent:
            dfs_visit(g, each, results)
    return results

def dfs_visit(g, v, results, parent = None):
    results.parent[v] = parent

    for each in g.neighbors(v):
        if each not in results.parent:
            print(each)
            # results.parent[each] = v
            # results.level[each] = results.level[v] + 1
            dfs_visit(g, each, results, v)
    
def print_path(r, s, v):    # in page 344
    if v == s:
        print("path: " + str(s))
    elif r.parent[v] == None:
        print("No path from %s to %s" % (str(s), str(v)))
    else:
        print_path(r, s, r.parent[v])
        print("->" + str(v))

if __name__ == '__main__':
    g = graph()
    nodes = ['u', 'v', 'w', 'x', 'y', 'z']
    g.add_nodes(nodes)
    g.add_edge(('u', 'v'))
    g.add_edge(('u', 'x'))
    g.add_edge(('x', 'v'))
    g.add_edge(('v', 'y'))
    g.add_edge(('y', 'x'))
    g.add_edge(('w', 'y'))
    g.add_edge(('w', 'z'))
    # for each in g.nodes():
    #     print(each)

    r = dfs(g)
    print('level : %s' % str(r.level))
    print('parent: %s' % str(r.parent))