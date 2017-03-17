

class Edge(object):
    def __init__(self, u, v, w):
        """
        :param u: source node
        :param v: destination node
        :param w: weight on edge
        """
        self.u, self.v, self.w = u, v, w

class Solution(object):
    """
    Kruskal's union-find implementation for minimum spanning tree.

    The core idea is to use union-find array to check if adding an edge could form a cycle. If no cycle is formed,
    the new edge is added; otherwise, discard the edge.

    1. The union-find implementation with path compression will only require O(k*log(n)) time.
    2. The union-find implementation with union-by-rank and no path compression will also guarantee a running time
       of O(k*log(n)) for k operations.

    where k is the number of edges.
    """

    def kruskal(self, n, edges):  # O(ElogE + ElogV) time
        """
        Find MST in an undirected graph using Kruskal's algorithm

        1. Sort all the edges in non-decreasing order of their weight.
        2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is
           not formed, include this edge. Else, discard it.
        3. Repeat step#2 until there are (V-1) edges in the spanning tree

        :param n: the number of nodes in the graph
        :param edges: the edges of the graph
        :return: the total sum of the weights in minimum spanning tree
        """
        # 1. sort edges by their weights in non-decreasing order in O(ElogE)
        edges.sort(key=lambda e: e.w)

        # initialize the union-find array
        parent = [i for i in range(n)]
        # store the rank of each node, which is used by Union-By-Rank technique in union function
        rank = [0 for i in range(n)]

        # each tree represents a node
        trees = n
        # the total sum of the weights of edges in mst
        res = 0
        # the set of edges of final minimum spanning tree
        mst = []

        # 2. Pick the smallest edge in O(ElogV) time
        for edge in edges:
            u, v = edge.u, edge.v
            if self.union(u, v, parent, rank):  # O(logV) time
                # reduce components by 1
                trees -= 1
                # add u-v edge in current spanning tree
                mst.append(edge)
                # the weight of current spanning tree
                res += edge.w
        return res

    def union(self, u, v, parent, rank):  # O(logV) time
        """
        Check if the edge(u,v) forms a cycle with the spanning tree formed so far.
        Optimization: use rank array to track the depth of each tree; and when doing union, choose the shallower
        tree and point it at the deeper one. This will prevent any tree from becoming deeper than log(n)
        :param parent: the union-find array
        :return: True if u and v have different roots; otherwise, false.
        """
        uu = self.find_parent(u, parent)
        vv = self.find_parent(v, parent)

        if uu == vv: return False

        # union u and v with Union-By-Rank technique
        if rank[uu] > rank[vv]:
            parent[vv] = parent[uu]
        elif rank[uu] < rank[vv]:
            parent[uu] = parent[vv]
        else:
            parent[vv] = uu
            rank[uu] += 1
        return True

    def find_parent(self, u, parent): # O(logV) time
        """
        Find the root of u with path compression idea (reset u and u's all superiors to be the same root)
        :param parent: the union-find array
        :return: return the root of u
        """
        if parent[u] != parent[parent[u]]:
            # path compression
            parent[u] = self.find_parent(parent[u], parent)
        return parent[u]

