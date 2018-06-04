"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
pages of CLRS: chinese page 344 in chapter 22

Discription of the algorithms:
BFS(G,s)
1   Q = null
2   ENQUEUE(Q, s)
3   while Q != null
4       u = DEQUEUE(Q)
5       for each v belong to G.Adj[u]
6           if v do not been traveled
7               v.travel = has been traveled
8               v.parent = u
9               ENQUEUE(Q, v)
"""
from pygraph.classes.graph import graph
from collections import deque

class BFSResults:
    def __init__(self):
        self.level = dict()
        self.parent = dict()

def bfs(g, s):
    r = BFSResults()
    q = deque()
    q.append(s)
    r.parent[s] = None
    r.level[s] = 0

    while(len(q)):
        v = q.popleft()
        for each in g.neighbors(v):
            if each not in r.parent:
                r.parent[each] = v
                r.level[each] = r.level[v] + 1
                q.append(each)
    return r

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
    nodes = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    g.add_nodes(nodes)
    g.add_edge(('s','r'))
    g.add_edge(('s','w'))
    g.add_edge(('r','v'))
    g.add_edge(('w','t'))
    g.add_edge(('w','x'))
    g.add_edge(('t','x'))
    g.add_edge(('t','u'))
    g.add_edge(('u','x'))
    g.add_edge(('u','y'))
    g.add_edge(('x','y'))

    r = bfs(g, 's')
    print('level : %s' % str(r.level))
    print('parent: %s' % str(r.parent))
    print_path(r, 's', 'y')