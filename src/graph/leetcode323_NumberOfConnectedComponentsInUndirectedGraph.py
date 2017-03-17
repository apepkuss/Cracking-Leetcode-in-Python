
class Solution(object):
    """
    @ Google, Twitter

    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a
    function to find the number of connected components in an undirected graph.

    Example 1:
         0          3
         |          |
         1 --- 2    4
    Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

    Example 2:
         0           4
         |           |
         1 --- 2 --- 3
    Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

    Note:
    You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same
    as [1, 0] and thus will not appear together in edges.
    """
    # method 1: find-union
    def countComponents_FindUnion(self, n, edges): # O(nlogn)
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find(root, node):
            """
            Find the root of node
            :return: the root of node
            """
            if root[node] == node:
                return node
            # path compression
            root[node] = find(root, root[node])
            return root[node]

        components = n
        root = [i for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]

            # find the root of u and v, respectively
            uroot = find(root, u)
            vroot = find(root, v)

            # union two node sets
            if uroot != vroot:
                components -= 1
                root[uroot] = vroot
        return components

    # method 2: dfs
    def countComponents_dfs(self, n, edges):  # MLE: O(n + E) time
        def dfs(u):
            for v in range(n):
                if matrix[u][v] and not visited[v]:
                    visited[v] = True
                    dfs(v)

        matrix = [[False] * n for _ in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            matrix[u][v] = matrix[v][u] = True
        visited = [False] * n
        components = 0
        for u in range(n):
            if not visited[u]:
                visited[u] = True
                dfs(u)
                components += 1
        return components
