class Solution(object):
    """
    @ Apple, Yelp, Zenefits
    
    DFS, BFS, TopSort, Graph
    
    There are a total of n courses you have to take, labeled from 0 to n - 1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
    which is expressed as a pair: [0,1]
    
    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
    
    For example:
    
    2, [[1,0]]
    There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
    
    2, [[1,0],[0,1]]
    There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take 
    course 0 you should also have finished course 1. So it is impossible.
    
    Note:
    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about 
    how a graph is represented. You may assume that there are no duplicate edges in the input prerequisites.
    """

    # Note: Union-Find approach is designed to check whether an UNDIRECTED graph contains circle or not. For a
    # directed graph, topological sorting, including Tarjan's and Kahn's algorithms, can be used to detect circle.

    # Method 1: Tarjan's algorithm, which is based on dfs idea
    def canFinish_Tarjan(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build a graph with an adjacent list
        graph = self.build_graph(numCourses)

        # permanent mark a vertex
        visited = [False] * numCourses
        # temporary mark a vertex
        onpath = [False] * numCourses

        # store a valid scheduling path
        schedule = []

        for u in range(numCourses):
            if not visited[u] and not self.dfs(u, graph, visited, onpath, schedule):
                return False
        return True

    def dfs(self, u, graph, visited, onpath, schedule):
        # if u is marked temporarily, it means graph has cycle
        if onpath[u]: return False

        # mark u temporarily
        onpath[u] = True

        for v in graph[u]:
            if not visited[v] and not self.dfs(v, graph, visited, onpath):
                return False

        # mark u permanently
        visited[u] = True
        # unmark n temporarily
        onpath[u] = False

        # add u to the head of schedule list
        schedule.insert(0, u)

        return True

    # Method 2: Kahn's algorithm, which is based on bfs idea
    def canFinish_Kahn(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build up a graph represented as an adjacent list
        graph = self.build_graph(numCourses)

        # record indegrees of each node in graph
        indegree = [0] * numCourses
        for elem in prerequisites:
            u = elem[0]
            indegree[u] += 1

        # store the vertices with 0 in-degree
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            u = queue.pop(0)
            count += 1

            # update in-degrees of u's neighbors
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return count == numCourses

    def build_graph(self, numCourses):
        """
        Build up a directed graph represented as adjacent list
        :param numCourses: graph nodes 
        """
        graph = [[] for _ in range(numCourses)]
        for elem in prerequisites:
            v, u = elem[0], elem[1]
            graph[u].append(v)

        return graph


if __name__ == "__main__":
    numCourses = 6
    prerequisites = [[0,1],[1,2],[2,3],[2,4],[3,5],[4,5]]
    res = Solution().canFinish(numCourses, prerequisites)
    print res
