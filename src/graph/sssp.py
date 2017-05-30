import sys

class SingleSourceShortestPath(object):

    @classmethod
    def dijkstra(cls, graph, source): # O(E+VlogV) time, if store the vertices in a Fibonacci heap
        """
        :param graph: an adjacent matrix
        :param source: the starting vertex
        """

        # n indicates the number of vertices in the graph
        n = len(graph)

        # initialize the dist and sptSet arrays
        # dist[i] indicates the distance from source node to node i.
        dist = [sys.maxint] * n

        # sptSet[i] indicates if node i is in the shortest path tree or not.
        sptSet = [False] * n

        # set the distance value of the source vertex as 0
        dist[source] = 0

        # the shortest path has only (n-1) edges
        for _ in xrange(n-1):
            # pick the minimum distance vertex from the set of vertices not yet visited
            u = cls.minDistance(dist, sptSet)
            sptSet[u] = True

            # update the distance value of the vertices adjacent to u
            for v in xrange(n):
                if sptSet[v]==False and graph[u][v]!=0 and graph[u][v]!=sys.maxint:
                    dist[v] = min(dist[v], dist[u]+graph[u][v])

        cls.printSolution(dist, source)

    @classmethod
    def minDistance(cls, dist, sptSet):
        """
        If use min heap, the time complexity is in O(logV)
        """
        min_value = sys.maxint
        min_idx = -1
        for x in xrange(len(dist)):
            if dist[x] < min_value and sptSet[x] == False:
                min_value = dist[x]
                min_idx = x
        return min_idx

    @classmethod
    def shimbel_dp(cls, graph, source): # O(VE) time, O(V) space
        """
        :param graph: an adjacent matrix
        :param source: the starting vertex
        """

        n = len(graph)

        # dist[u] denotes the distance from source to u
        dist = [sys.maxint] * n
        dist[source] = 0

        for _ in range(n-1):
            for u in range(n):
                for v in range(n):
                    if graph[u][v]!=0 and graph[u][v]!=sys.maxint:
                        dist[v] = min(dist[v], dist[u] + graph[u][v])

        # check negative cycle
        for u in range(n):
            for v in range(n):
                if graph[u][v]!=0 and graph[u][v]!=sys.maxint and dist[v] > dist[u] + graph[u][v]:
                    print "Negative Cycle!"
                    break

        cls.printSolution(dist, source)

    @classmethod
    def printSolution(cls, dist, source):

        n = len(dist)
        res = []
        for u in xrange(n):
            res.append((source, u, dist[u]))

        print res