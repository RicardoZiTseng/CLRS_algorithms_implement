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


DIJKSTRA(G, w, s)
1   INITIALIZE-SINGLE-SOURCE(G, s)
2   S = φ
3   Q = G.V
4   while Q ≠ φ
5       u = EXTRACT-MIN(Q)
6       S = S ∪ u
7       for each vertex v ∈ G.Adj[u]
8           RELAX(u, v, w)
"""
from pygraph.classes.digraph import digraph
from disjoint_set_data import tree_node
import heapq

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

def bellman_fold_notCLRS(graph, source):
    """
    Another complication of bellman-fold algorithm
    @param type: digraph/graph, node_name
    @return type: dict, dict
    """
    distance = {source: 0}
    predecessor = {source: None}

    for i in range(1, graph.order()-1):
        for src, dst in graph.edges():
            if(src in distance) and (dst not in distance):
                distance[dst] = distance[src] + graph.edge_weight((src, dst))
                predecessor[dst] = src
            elif (src in distance) and (dst in distance) and \
            (distance[dst] > distance[src] + graph.edge_weight((src, dst))):
                distance[dst] = distance[src] + graph.edge_weight((src, dst))
    
    for u,v in graph.edges():
        if distance[v] > distance[u] + graph.edge_weight((u, v)):
            raise ValueError("Detected a negative weight cycle on edge (%s, %s)" % (u, v))
    
    return predecessor, distance

def dag_shortest_paths(g, s):
    pass

def dijkstra(graph, source):
    """
    Return the shortest path distance between source and all other nodes using Dijkstra's
    algorithm
    @param type: digraph/graph, node_name
    @return type: dict, dict   
    """
    dist = {source: 0}
    previous = {source: None}

    q = [(0, source)]

    while len(q) > 0:
        du, u = heapq.heappop(q)

        if dist[u] < du:
            continue
        
        for v in graph[u]:
            alt = du + graph.edge_weight((u, v))
            if(v not in dist) or (alt < dist[v]):
                dist[v] = alt
                previous[v] = u
                heapq.heappush(q, (alt, v))
    return previous, dist

def test_bellman_fold():
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

def test_dijkstra():
    g = digraph()
    nodes = ['s', 't', 'x', 'y', 'z']
    g.add_nodes(nodes)
    g.add_edge(('s', 't'), 10)
    g.add_edge(('s', 'y'), 5)
    g.add_edge(('t', 'x'), 1)
    g.add_edge(('t', 'y'), 2)
    g.add_edge(('y', 't'), 3)
    g.add_edge(('y', 'x'), 9)
    g.add_edge(('y', 'z'), 2)
    g.add_edge(('x', 'z'), 4)
    g.add_edge(('z', 'x'), 6)
    g.add_edge(('z', 's'), 7)

    previous, dist = dijkstra(g, 's')
    print(previous, dist)

def system_of_different_constraints():
    """
    x1 - x2 <= 0
    x1 - x5 <= -1
    x2 - x5 <= 1
    x3 - x1 <= 5
    x4 - x1 <= 4
    x4 - x3 <= -1
    x5 - x3 <= -3
    x5 - x4 <= -3
    """
    m = int(input("Enter the number of limited conditions ->"))
    n = int(input("Enter the number of variables ->"))
    g = digraph()
    for i in range(0, n+1):
        node = 'x' + str(i)
        g.add_node(node)
        if i > 0:
            g.add_edge(('x0', node), 0)
    print(g.nodes())
    print(g.edges())

    print("Enter the conditions: ")
    for i in range(m):
        print("The %d-th condition:" % (i+1))
        v1 = input("First variable: ")
        v2 = input("Second variable: ")
        b = int(input("Biase: "))
        g.add_edge((v2, v1), b)
    print(g.edges())
    previous, dist = bellman_fold_notCLRS(g, 'x0')
    print(previous, dist)
    """
    If there is no solutions to the system, the function should
    tell the users "no solution", we do not complete this part here.
    """

if __name__ == '__main__':
    system_of_different_constraints()