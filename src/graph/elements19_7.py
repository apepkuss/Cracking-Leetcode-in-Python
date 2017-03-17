import unittest
import sys


class Vertex(object):
    def __init__(self, value):
        self.min_discover_time = sys.maxint
        self.discover_time = 0
        self.adjacent_nodes = []
        self.visited = False
        self.value = value


class Elements(object):
    """
    elements 19.7 Test degrees of connectedness

    A graph is 2ForSome-connected if it remains connected even if any single edge is removed; a graph is 2ForSome-
    connected if there exists an edge that can be removed while still leaving the graph connected.

    Let G=(V,E) be a connected undirected graph. How would you efficiently check if G is 2ForSome-connected? Can
    you make your algorithm run in O(V) time? How would you check if G is 2ForAll-connected?
    """

    @classmethod
    def is_2ForSome_connected(cls, source):

        def dfs(parent, node):
            if node.visited:
                return True
            node.visited = True
            if len(node.adjacent_nodes) > 0:
                for child in node.adjacent_nodes:
                    if child != parent and dfs(node, child):
                        return True
            return False

        if source is None:
            return False
        return dfs(None, source)


    @classmethod
    def is_2ForAll_connected(cls, source):

        def dfs(parent, node, time):
            node.discover_time = time
            for child in node.adjacent_nodes:
                if child != parent:
                    if child.discover_time != 0:
                        # back edge
                        node.min_discover_time = min(node.min_discover_time, child.discover_time)
                    else:
                        # forward edge
                        if not dfs(node, child, time+1):
                            return False
                        node.min_discover_time = min(node.min_discover_time, child.min_discover_time)
            return parent is None or node.min_discover_time < node.discover_time

        if source is None:
            return True
        return dfs(None, source, 1)



class TestRun(unittest.TestCase):

    def test_hasNoCycle(self):
        source = Vertex(0)
        node1 = Vertex(1)
        node2 = Vertex(2)
        source.adjacent_nodes += [node1, node2]

        node3 = Vertex(3)
        node4 = Vertex(4)
        node5 = Vertex(5)
        node2.adjacent_nodes += [node3, node4, node5]

        node6 = Vertex(6)
        node4.adjacent_nodes.append(node6)

        res = Elements.is_2ForSome_connected(source)
        unittest.TestCase.assertFalse(self, res)

    def test_hasInvalidCycle(self):
        source = Vertex(0)
        node1 = Vertex(1)
        node2 = Vertex(2)
        source.adjacent_nodes += [node1, node2]

        node3 = Vertex(3)
        node4 = Vertex(4)
        node5 = Vertex(5)
        node2.adjacent_nodes += [node3, node4, node5]

        node4.adjacent_nodes.append(node2)

        res = Elements.is_2ForSome_connected(source)
        unittest.TestCase.assertFalse(self, res)

    def test_hasCycle(self):
        source = Vertex(0)
        node1 = Vertex(1)
        node2 = Vertex(2)
        source.adjacent_nodes += [node1, node2]

        node3 = Vertex(3)
        node4 = Vertex(4)
        node5 = Vertex(5)
        node2.adjacent_nodes += [node3, node4, node5]

        node4.adjacent_nodes.append(node1)

        res = Elements.is_2ForSome_connected(source)
        unittest.TestCase.assertTrue(self, res)

    def test_allEdgesOnCycle(self):
        source = Vertex(0)
        node1 = Vertex(1)
        node2 = Vertex(2)
        source.adjacent_nodes.append(node1)
        node1.adjacent_nodes.append(node2)
        node2.adjacent_nodes.append(source)

        node3 = Vertex(3)
        node4 = Vertex(4)
        source.adjacent_nodes.append(node3)
        node3.adjacent_nodes.append(node4)
        node4.adjacent_nodes.append(source)

        res = Elements.is_2ForAll_connected(source)
        unittest.TestCase.assertTrue(self, res)

    def test_notAllEdgesOnCycle(self):
        source = Vertex(0)
        node1 = Vertex(1)
        node2 = Vertex(2)
        source.adjacent_nodes.append(node1)
        node1.adjacent_nodes.append(node2)
        node2.adjacent_nodes.append(source)

        node3 = Vertex(3)
        node4 = Vertex(4)
        node5 = Vertex(5)
        source.adjacent_nodes.append(node3)
        node3.adjacent_nodes.append(node4)
        node4.adjacent_nodes.append(node5)
        node5.adjacent_nodes.append(node3)

        res = Elements.is_2ForAll_connected(source)
        unittest.TestCase.assertFalse(self, res)


if __name__ == "__main__":
    unittest.main()