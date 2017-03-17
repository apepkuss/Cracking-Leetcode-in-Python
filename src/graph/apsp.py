

class AllPairShortestPath(object):

    @classmethod
    def floydwarshall(cls, graph): # O(V^3) time, O(V^2) space
        """
        Floyd-Warshall APSP algorithm

        For every pair (u,v) of source and destination vertices respectively, there are two possible cases:
        1. If k is not an intermediate vertex on the shortest path from u to v, we keep the value of dist[u][v] as it is;
        2. If k is an intermediate vertex on the shortest path from u to v, then we update dist[u][v] with min(dist[u][v],
           dist[u][k]+dist[k][v]).

        :param graph: the target graph represented by adjacency matrix
        """

        # initialize the dist matrix with the values in graph matrix
        # dist[u][v] indicates the shortest path from u to v
        dist = map(lambda v: map(lambda u: u,v), graph)

        n = len(dist)
        # r denotes the possible intermediate vertices from u to v
        for r in xrange(n):

            # one-by-one pick all vertices as source
            for u in xrange(n):

                # pick all vertices as destination for the picked source
                for v in xrange(n):
                    # if k is the intermediate vertex on the path from u to v,
                    # then update dist[u][v]
                    dist[u][v] = min(dist[u][v], dist[u][r] + dist[r][v])

        cls.printSolution(dist)

    @classmethod
    def printSolution(cls, dist):
        res = []

        # source vertices
        for u in xrange(len(dist)):
            # destination vertices
            for v in xrange(len(dist)):
                if u != v:
                    res.append((u,v,dist[u][v]))

        print res
