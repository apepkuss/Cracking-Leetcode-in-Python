import unittest


class Vertex(object):
    def __init__(self, value):
        self.adjacent_nodes = []
        self.visited = False
        self.distance = 1
        self.value = value


class Elements(object):
    """
    elements 19.8

    You will be taking pictures for soccer teams. All teams have the same number of players. How to determine the
    largest number of teams that can be photographed simultaneiously subject to the constraints: 1. the player in
    the back row must be taller than the player in front of him; 2. all players in a row must be from the same team.
    """

    @classmethod
    def find_largest_number_teams(cls, graph):
        vertex_order = cls.build_topological_ordering(graph)
        return cls.find_longest_path(vertex_order)

    @classmethod
    def build_topological_ordering(cls, graph):
        """
        build a topological ordering for DAG
        :param graph: the target directed acyclic graph, DAG
        :return: topological ordering
        """

        def dfs(node):
            node.visited = True
            for child in node.adjacent_nodes:
                if not child.visited:
                    dfs(child)
            vertex_order.append(node)

        vertex_order = []
        for node in graph:
            if not node.visited:
                dfs(node)
        return vertex_order

    @classmethod
    def find_longest_path(cls, vertex_order):
        max_distance = 0
        while len(vertex_order) > 0:
            u = vertex_order.pop()
            max_distance = max(max_distance, u.distance)
            for v in u.adjacent_nodes:
                v.distance = max(v.distance, u.distance+1)
        return max_distance


class TestRun(unittest.TestCase):

    def test_case1(self):
        node1 = Vertex(1)
        node2 = Vertex(2)
        node3 = Vertex(3)
        node4 = Vertex(4)

        node1.adjacent_nodes.append(node2)
        node2.adjacent_nodes.append(node4)
        node3.adjacent_nodes.append(node4)

        graph = [node4, node1, node3, node2]

        res = Elements.find_largest_number_teams(graph)
        unittest.TestCase.assertEqual(self, first=3, second=res)


if __name__ == "__main__":
    unittest.main()

