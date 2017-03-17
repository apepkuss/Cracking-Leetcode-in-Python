
import collections

class Solution(object):
    """
    @ Google

    Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the
    itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

    Note:
    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when
    read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.
    Example 1:
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
    Example 2:
        tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
        Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.


    Analysis:

    This question can be modelled as a graph, where the nodes represent the airports and the edges are the lines between
    two airports. The answer is to find a path, and following this path, each edge can be visited once. Therefore, the
    path is a Eulerian path. We can find a Eulerian path in a graph using Hierholzer's algorithm.

    About the definitions and properties of Euler path and cycle, reference https://en.wikipedia.org/wiki/Eulerian_path

    """
    def findItinerary(self, tickets):  # O(n) time, where n is the number of edges in graph, namely tickets.
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def visit(airport):
            while targets[airport]:
                dest = targets[airport].pop(0)
                visit(dest)
            route.append(airport)

        targets = collections.defaultdict(list)
        for x, y in sorted(tickets):
            targets[x].append(y)
        route = []
        visit('JFK')
        return route[::-1]


if __name__ == "__main__":
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    res = Solution().findItinerary(tickets)
    print res
