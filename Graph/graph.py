"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
The implement of graph data structure.
"""
class graph(object):
    def __init__(self):
        """
        Initialize a graph.
        """
        self.node_neighbors = {}    #Paring: Node -> Neighbors
        self.edge_weight = {}   #Key value pairs: (Edge -> Attributes)

    def nodes(self):
        """
        Return all the nodes in graph.

        @return type:   list
        """
        return list(self.node_neighbors.keys())

    def neighbors(self, node):
        """
        Return all the nodes that are directly access from the given node
        @param type: Node identifier
        @return type: List of nodes directly accessible from given node.
        """
        return list(self.node_neighbors[node])
    
    def edges(self):
        pass

    def has_node(self, node):
        """
        Return whether the requested node exists.
        
        @param node type: Node identifier
        @return type: boolean
        @return: True-value for node existence
        """
        return node in self.node_neighbors

    def has_edge(self, edge):
        """
        Return whether the requested edge exists.

        @param edge type: tuple
        @return type: boolean
        @return: True-value for edge existence
        """
        return edge in self.edge_weight

    def add_node(self, node, attrs = None):
        """
        Add given node to the graph
        @note: node can be any type
        @param type: Node identifier
        """
        if attrs is None:
            attrs = []
        if (not node in self.node_neighbors):
            self.node_neighbors[node] = set()
            # self.node_attr[node] = attr
        else:
            raise RuntimeError("Node %s already in graph" % node)

    def add_nodes(self, nodelist):
        """
        Add all the node from nodelist to the graph
        """
        for each in nodelist:
            self.add_node(each)
        
    def add_edge(self, edge, wt = 1):
        """
        Add an edge to the graph connecting two nodes.
        An edge is a pair of nodes like (u, v)
        @type edge: tuple
        @param edge: Edge
        
        @type wt:   real number
        @param wt:  the weight from node u to node v of edge (p, q)
        """
        u, v = edge
        if (v not in self.node_neighbors[u] and u not in self.node_neighbors[v]):
            self.node_neighbors[u].add(v)
            if (u != v):
                self.node_neighbors[v].add(u)
            if (edge not in self.edge_weight):
                self.edge_weight[edge] = wt
        else:
            raise RuntimeError("Edge (%s, %s) already in graph" % (u, v))    

    def del_node(self, node):
        """
        Remove a node from the graph.
        @type node: Node identifier
        """
        pass

    def del_edge(self, edge):
        """
        Remove the given edge from the graph.
        @type edge: tuple
        @param edge: Edge
        """
        u, v = edge
        self.node_neighbors[u].remove(v)
        if u != v:
            self.node_neighbors[v].remove(u)


def test():
    g = graph()
    g.add_nodes(["A", "B", "C", "D", "E"])

    g.add_edge(("A", "C"))  #A→C
    g.add_edge(("A", "D"))  #A→D
    g.add_edge(("B", "D"))
    g.add_edge(("C", "E"))
    g.add_edge(("D", "E"))
    g.add_edge(("B", "E"))  #B→E
    g.add_edge(("E", "A"))
        
