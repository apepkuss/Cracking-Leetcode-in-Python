# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @ Pocket Gems, Google, Uber, Facebook

    Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

    OJ's undirected graph serialization:
    Nodes are labeled uniquely.

    We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
    As an example, consider the serialized graph {0,1,2#1,2#2,2}.

    The graph has a total of three nodes, and therefore contains three parts as separated by #.

    First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    Second node is labeled as 1. Connect node 1 to node 2.
    Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
    """
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph_dfs(self, node):
        def dfs(root):
            if root in visited:
                return visited[root]
            else:
                copy_node = UndirectedGraphNode(root.label)
                visited[root] = copy_node

                for neighbor in root.neighbors:
                    # self-loop
                    if neighbor == root:
                        copy_node.neighbors.append(copy_node)
                    else:
                        copy_node.neighbors.append(dfs(neighbor))
                return copy_node

        if node is None:
            return None
        visited = {}
        dfs(node)
        return visited[node]

    def cloneGraph_bfs(self, node):
        if node is None: return None
        visited = {}
        queue = [node]
        while len(queue) > 0:
            root = queue.pop(0)
            if root not in visited:
                visited[root] = UndirectedGraphNode(root.label)
            copy_root = visited[root]
            for neighbor in root.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = UndirectedGraphNode(neighbor.label)
                copy_root.neighbors.append(visited[neighbor])
        return visited[node]