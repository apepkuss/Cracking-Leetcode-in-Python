import unittest


class Vertex(object):
    def __init__(self, value):
        self.adjacent_nodes = []
        self.value = value

class Elements(object):
    """
    elements 19.4 Clone a graph

    Design an algorithm that takes a reference to a vertex u, and creates a copy of the graph on the vertices
    reachable from u. Return the copy of u.
    """

    @classmethod
    def clone(cls, source):
        if source is None:
            return None
        # clone source node
        source_clone = Vertex(source.value)
        # track the relationship between the nodes in the original graph and those in the clone graph
        table = {source:source_clone}
        queue = [source]
        while len(queue) > 0:
            curr_node = queue.pop(0)
            clone_node = table[curr_node]
            if len(curr_node.adjacent_nodes) > 0:
                clone_node.adjacent_nodes = []
                for child in curr_node.adjacent_nodes:
                    if table.has_key(child):
                        continue
                    cnode = Vertex(child.value)
                    table[child] = cnode
                    queue.append(child)
                    clone_node.adjacent_nodes.append(cnode)
        return source_clone


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

        expected_res = []
        queue = [[source]]
        while len(queue) > 0:
            nodes = queue.pop(0)
            values = []
            next_level_nodes = []
            for node in nodes:
                values.append(node.value)
                if len(node.adjacent_nodes) > 0:
                    next_level_nodes += node.adjacent_nodes
            expected_res.append(values.sort())
            if len(next_level_nodes) > 0:
                queue.append(next_level_nodes)

        source_clone = Elements.clone(source)
        actual_res = []
        queue = [[source_clone]]
        while len(queue) > 0:
            nodes = queue.pop(0)
            values = []
            next_level_nodes = []
            for node in nodes:
                values.append(node.value)
                if len(node.adjacent_nodes) > 0:
                    next_level_nodes += node.adjacent_nodes
            actual_res.append(values.sort())
            if len(next_level_nodes) > 0:
                queue.append(next_level_nodes)

        unittest.TestCase.assertEqual(self, first=expected_res, second=actual_res)


if __name__ == "__main__":
    unittest.main()


