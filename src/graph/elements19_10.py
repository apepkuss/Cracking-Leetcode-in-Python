import unittest
import heapq


class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent_nodes = []


class Graph(object):
    def __init__(self, vertices, weights_on_edges):
        self.vertices = vertices
        self.weights_on_edges = weights_on_edges

class Elements(object):
    """
    elements 19.10 Compute a shortest path with fewest edges

    Design an algorithm which takes as input a graph G=(V,E), directed or undirected, a nonnegative cost function on
    E, and vertices s and t; your algorithm should output a path with the fewest edges amongst all shortest paths from
    s to t.

    Solution: Dijkstra's SSSP algorithm is the best choice for single source shortest path problem when the weights on
    edges are all non-negative. When use Fibonacci heap to compute the minimum distance of nodes in next visit set, the
    run time is O(E+VlogV), approximately O(V^2) when E = V*V.

    If the weights on edges could be negative, Shimbel's SSSP algorithm is a better choice. The DP implementation of
    Shimbel's SSSP can reach O(VE) run time and O(V) space.
    """

    @classmethod
    def find_shortestPathWithFewestEdge(cls, graph, s, t):

        def Dijkstra_SSSP(graph, s):
            # next_visit dictionary keeps the candidate nodes for next visiting round
            # first element of value list is distance from s
            # second element denotes direct parent node
            # third element is the node itself
            # such a data structure design is for making use of min heap
            next_visit = {s:(0, None, s)}
            # visited dictionary keeps the nodes that have been visited
            visited = {}

            while next_visit:
                # find the node in next_visit, which currently has the minimum distance value.
                values = next_visit.values()
                heapq.heapify(values)
                min_node = values[0][2]
                if min_node is None:
                    break

                current_weight = next_visit[min_node][0]
                # update the distance values of adjacent nodes of current min node with new weights
                for adjacent_node in graph.vertices[graph.vertices.index(min_node)].adjacent_nodes:
                    weight = current_weight + graph.weights_on_edges[(min_node, adjacent_node)]
                    if (adjacent_node not in next_visit and adjacent_node not in visited) or \
                            (adjacent_node in next_visit and weight < next_visit[adjacent_node][0]):
                        next_visit[adjacent_node] = (weight, min_node, adjacent_node)

                # Dijkstra's SSSP algorithm guarantees each vertex and edge are just visited once.
                # Once a node is visited, remove it from nodes set.
                visited[min_node] = next_visit[min_node]
                del next_visit[min_node]

            return visited

        distances = Dijkstra_SSSP(graph, s)

        path = [t]
        parent = distances[t][1]
        while parent:
            path.append(parent)
            parent = distances[parent][1]

        return distances[t][0], path[::-1]



class TestRun(unittest.TestCase):

    def setUp(self):
        self.node1 = Vertex(1)
        self.node2 = Vertex(2)
        self.node3 = Vertex(3)
        self.node4 = Vertex(4)
        self.node5 = Vertex(5)
        self.node6 = Vertex(6)

        self.node1.adjacent_nodes.append(self.node2)
        self.node1.adjacent_nodes.append(self.node4)
        self.node1.adjacent_nodes.append(self.node5)
        self.node2.adjacent_nodes.append(self.node3)
        self.node3.adjacent_nodes.append(self.node4)
        self.node4.adjacent_nodes.append(self.node6)
        self.node5.adjacent_nodes.append(self.node6)

        self.vertices = [self.node1, self.node4, self.node2, self.node5, self.node3, self.node6]
        self.weights_on_edges = {(self.node1, self.node2):5, (self.node1, self.node4):9, (self.node1, self.node5):2, \
                      (self.node2, self.node3):2, (self.node3, self.node4):3, (self.node4, self.node6):2, \
                      (self.node5, self.node6):3}


    def test_case1(self):
        graph = Graph(self.vertices, self.weights_on_edges)
        actual_result = Elements.find_shortestPathWithFewestEdge(graph, self.node1, self.node6)
        expected_result = 5
        unittest.TestCase.assertEqual(self, first=expected_result, second=actual_result[0])


if __name__ == "__main__":
    unittest.main()









