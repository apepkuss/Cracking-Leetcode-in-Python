import unittest
import math
import sys


class Graph(object):
    def __init__(self, n):
        self.table = [[1]*n for _ in xrange(n)]

    def add_edge(self, from_node, to_node, weight):
        self.table[from_node][to_node] = weight
        self.table[to_node][from_node] = 1.0/weight


class Elements(object):
    """
    elements 19.12

    Design an algorithm to determine whether there exists an arbitrage - a way to start with a single unit of some
    commodity C and convert it back to more time one unit of C through a sequence of exchanges.

    Solution: Observe that an arbitrage exists if and only if there exists a cycle in G whose edge weights multiply
    out to more than 1. Create a new graph G' with a new weight function w'(e) = -log(w(e)). Since log(a*b)=log(a)+
    log(b), there exists a cycle in G if and only if there exists a negative cycle in G'. In addition, for the
    arbitrage problem, the graph is complete. Hence, we can start from any single vertex. Therefore, we can use
    Shimbel's SSSP algorithm to solve this problem.
    """

    @classmethod
    def is_arbitrage_existed(cls, graph, source_node):

        def Shimbel_SSSP(graph, source_node):  # O(VE)<=O(V^3) time, O(V) space
            n = len(graph.table)
            dp = [sys.float_info.max for _ in xrange(n)]
            dp[source_node] = 0

            # a path has at most n-1 edges in a graph with n vertices
            for num_edge in xrange(1, n):
                updated = False
                for i in xrange(n):
                    for j in xrange(n):
                        if dp[i] != sys.float_info.max and dp[j] > dp[i] + graph.table[i][j]:
                            dp[j] = dp[i] + graph.table[i][j]
                            updated = True
                # no update means no negative cycle exists
                if not updated:
                    return False

            # check negative cycle
            for i in xrange(n):
                for j in xrange(n):
                    if dp[i] != sys.float_info.max and dp[j] > dp[i] + graph.table[i][j]:
                        return True
            return False

        n = len(graph.table)
        # transform each edge in graph
        for i in xrange(n):
            for j in xrange(n):
                graph.table[i][j] = -math.log(100 * graph.table[i][j])

        return Shimbel_SSSP(graph, source_node)


class TestRun(unittest.TestCase):

    def test_case1(self):
        graph = Graph(6)
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 3, 9)
        graph.add_edge(0, 4, 2)
        graph.add_edge(1, 2, 2)
        graph.add_edge(1, 4, 3)
        graph.add_edge(2, 0, 4)
        graph.add_edge(2, 3, 3)
        graph.add_edge(2, 5, 2)
        graph.add_edge(3, 1, 5)
        graph.add_edge(3, 4, 2)
        graph.add_edge(3, 5, 2)
        graph.add_edge(4, 2, 4)
        graph.add_edge(4, 5, 3)
        graph.add_edge(5, 0, 7)
        graph.add_edge(5, 1, 6)


        actual_result = Elements.is_arbitrage_existed(graph, 0)
        unittest.TestCase.assertTrue(self, actual_result)


if __name__ == "__main__":
    unittest.main()


