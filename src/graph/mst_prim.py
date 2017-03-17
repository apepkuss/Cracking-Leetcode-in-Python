
import sys

class MST(object):
    """
    Minimum Spanning Tree problem in a connected, undirected, weighted graph. When all edge weights are distinct, the
    minimum spanning tree is unique.
    """

    @classmethod
    def prim_mst(cls, graph, source):  # O(V^2) time
        """
        The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST,
        the other set contains the vertices not yet included. At every step, it considers all the edges that connect
        the two sets, and picks the minimum weight edge from these edges. After picking the edge, it moves the other
        endpoint of the edge to the set containing MST.

        1. Create a set mstSet that keeps track of vertices already included in MST.
        2. Assign a key value to all vertices in the input graph. Initialize all key values as 0 for the first vertex
           so that it is picked first.
        3. while mstSet doesn't include all vertices:
            3.1 Pick a vertex u which is not there in mstSet and has minimum key value.
            3.2 Include u to mstSet.
            3.3 Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent
                vertices. For every adjacent vertex v, if weight of edge u-v is less than the previous key value of v,
                update the key value as weight of u-v.

        :param graph: an adjacent matrix
        :param source:
        """

        n = len(graph)

        # 1. create a set to keep track of vertices already included in MST
        mstSet = [False] * n

        # 2. key used to pick minimum weight edge in cut
        key = [sys.maxint] * n
        key[source] = 0

        # store mst
        parent = [0] * n
        parent[source] = -1

        # 3. MST has n-1 edges
        for _ in xrange(n-1):
            # get the node with minimum weight
            min_weight = sys.maxint
            u = -1

            # find next node to be added into MST, which has the minimum weight
            for i in xrange(n):
                if mstSet[i] == False and key[i] < min_weight:
                    min_weight = key[i]
                    u = i

            # add the node into MST
            mstSet[u] = True

            # update the weights of all nodes incident to u
            for v in xrange(n):
                if mstSet[v] == False and graph[u][v] != 0 and graph[u][v] < key[v]:
                    # set the weight on edge u->v to the vertex v
                    key[v] = graph[u][v]
                    parent[v] = u

        # print the mst, which has n-1 edges
        for i in xrange(n):
            print str(parent[i]) + "->" + str(i) + ": " + str(graph[i][parent[i]])


if __name__ == "__main__":
    graph = [[0,2,0,6,0],
             [2,0,3,8,5],
             [0,3,0,0,7],
             [6,8,0,0,9],
             [0,5,7,9,0]]
    MST.prim_mst(graph, 0)

            
