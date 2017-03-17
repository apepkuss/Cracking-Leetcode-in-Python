
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
    # method 1: find-union solution with union-by-rank
    def countComponents_UnionFind(self, n, edges): # O(nlogn)
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # FIND with path compression
        def find(x):
            # path comparession technique resets x and its all superiors to be the same root
            if roots[x] != roots[roots[x]]:
                roots[x] = find(roots[x])
            return roots[x]

        # UNION with union-by-rank
        def union(u, v):
            uu = find(u)
            vv = find(v)
            if uu == vv:
                return False
            if rank[uu] > rank[vv]:
                uu, vv = vv, uu
            if rank[uu] == rank[vv]:
                rank[vv] += 1
            roots[uu] = vv
            return True

        components = n
        # roots is union-find data structure
        roots = [i for i in range(n)]
        # rank[x]: the depth of the tree rooted at x. The initial value is 1.
        rank = [1 for _ in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            if union(u, v):
                components -= 1
        return components

    # method 2: slow union-find solution
    def countComponents_SlowUnionFind(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        def dfs_findroot(root, x):
            if root[x] == x:
                return x
            root[x] = dfs_findroot(root, root[x])
            return root[x]

        components = n
        root = [i for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]

            # find
            uroot = dfs_findroot(root, u)
            vroot = dfs_findroot(root, v)

            # union
            if uroot != vroot:
                components -= 1
                root[uroot] = vroot
        return components

    # method 3: dfs
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
