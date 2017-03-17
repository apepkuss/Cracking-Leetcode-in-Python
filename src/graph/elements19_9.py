import unittest


class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent_nodes = []

class Elements(object):
    """
    elements 19.9 Compute a minimum delay schedule, unlimited resources.

    Let T = {T(0),T(1),...,T(n-1)} be a set of tasks. Each task runs on a single generic server. Task T(i) has a
    duration t(i), and a set P(i) (possibly empty) of tasks that must be completed before T(i) can be started.
    The set is feasible if there does not exist a sequence of tasks <T(0),T(1),...,T(n-1),T(0)> starting and ending
    at the same task such that for each consecutive pair of tasks in the sequence, the first task must be completed
    before the second task can begin.

    Given an instance of the task scheduling problem, compute the least amount of time in which all the tasks can
    be performed, assuming an unlimited number of servers. Explicitly check that the system is feasible.

    Solution: we can model this task scheduling problem as a graph, which could be either DAG or not. Each task is
    a graph vertex, and each directed edge u->v exists if a relation of starting task v only after ending task u exists.
    To check the feasibility of the given task scheduling, we can make use of topological sort algorithm to get a
    topological ordering. If a cycle exists in the graph, it means the task scheduling is infeasible. If no cycle in
    the graph, we can get the topological ordering, then we can compute the least amount of time finishing all tasks
    by compute the maximum distance like elements 19.8.
    """

    @classmethod
    def check_feasibility(cls, graph):

        def topSort_dfs(node):
            unvisited.remove(node)
            active.add(node)
            for child in node.adjacent_nodes:
                if child in unvisited:
                    if not topSort_dfs(child):
                        return False
                elif child in active:
                    return False
            active.remove(node)
            done.add(node)
            stack.append(node.value)
            return True

        stack = []
        unvisited = set()
        active = set()
        done = set()

        # create a new vertex in graph, which has an outgoing edge to each node existed in graph
        source = Vertex(0)
        for node in graph:
            source.adjacent_nodes.append(node)
            unvisited.add(node)

        # do topological sort from source
        res = True
        for node in source.adjacent_nodes:
            if node in unvisited:
                res = topSort_dfs(node)
                if not res:
                    break
            elif node in active:
                res = False
        return res, stack[::-1]


class TestRun(unittest.TestCase):

    def setUp(self):
        self.node1 = Vertex(1)
        self.node2 = Vertex(2)
        self.node3 = Vertex(3)
        self.node4 = Vertex(4)
        self.node5 = Vertex(5)
        self.node6 = Vertex(6)
        self.node7 = Vertex(7)

        self.node1.adjacent_nodes.append(self.node3)
        self.node2.adjacent_nodes.append(self.node3)
        self.node2.adjacent_nodes.append(self.node5)
        self.node3.adjacent_nodes.append(self.node4)
        self.node4.adjacent_nodes.append(self.node6)
        self.node5.adjacent_nodes.append(self.node6)
        self.node6.adjacent_nodes.append(self.node7)

        self.graph = [self.node1, self.node4, self.node2, self.node5, self.node3, self.node7, self.node6]

    def test_case_DAG(self):
        actual_result = Elements.check_feasibility(self.graph)
        expected_result = True, [2,5,1,3,4,6,7]
        unittest.TestCase.assertEqual(self, first=expected_result, second=actual_result)

    def test_case_NotDAG(self):
        self.node7.adjacent_nodes.append(self.node5)

        actual_result = Elements.check_feasibility(self.graph)
        unittest.TestCase.assertFalse(self, actual_result[0])

        self.node7.adjacent_nodes = []

if __name__ == "__main__":
    unittest.main()
