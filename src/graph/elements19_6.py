import unittest


class Vertex(object):
    def __init__(self, value):
        self.adjacent_nodes = []
        self.value = value


class Elements(object):
    """
    elements 19.6 Bipartite

    Design an algorithm that checks if a graph is bipartite.
    Design an algorithm that checks if a graph is 2-colorable.
    """

    @classmethod
    def is_bipartite(cls, source):
        if source is None or len(source.adjacent_nodes) < 2:
            return False
        count = 0
        left_part = set()
        right_part = set()
        queue = [[source]]
        while len(queue) > 0:
            nodes = queue.pop(0)
            next_level_nodes = []
            for node in nodes:
                if count%2 == 0:
                    if node in right_part:
                        return False
                    left_part.add(node)
                else:
                    if node in left_part:
                        return False
                    right_part.add(node)
                next_level_nodes += node.adjacent_nodes
            if len(next_level_nodes) > 0:
                queue.append(next_level_nodes)
            count += 1
        return True


class TestRun(unittest.TestCase):

    def test_case1(self):
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

        res = Elements.is_bipartite(source)
        unittest.TestCase.assertTrue(self, res)

    def test_case2(self):
        source = Vertex(0)
        node1 = Vertex(1)
        node2 = Vertex(2)
        source.adjacent_nodes += [node1, node2]

        node3 = Vertex(3)
        node4 = Vertex(4)
        node5 = Vertex(5)
        node2.adjacent_nodes += [node3, node4, node5]
        node3.adjacent_nodes.append(node5)

        res = Elements.is_bipartite(source)
        unittest.TestCase.assertFalse(self, res)


if __name__ == "__main__":
    unittest.main()


