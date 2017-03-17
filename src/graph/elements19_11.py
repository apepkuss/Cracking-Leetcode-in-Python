import unittest
import sys
import copy


class HighwaySection(object):
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

class Graph(object):
    def __init__(self, n):
        self.table = [[sys.maxint] * n for _ in xrange(n)]

    def add_edge(self, from_node, to_node, distance):
        self.table[from_node][to_node] = distance
        self.table[to_node][from_node] = distance


class Elements(object):
    """
    elements 19.11 Road network

    The Texas Department of Transportation is considering adding a new section of highway to the Texas Highway System.
    Each highway section connects two cities. City officials have submitted proposals for the new highway - each
    proposal includes the pair of cities being connected and the length of the section.

    Devise an efficient algorithm which takes the existing highway network(specified as a set of highway sections
    between pairs of cities) and proposals for new highway sections, and returns a proposed highway section which
    minimizes the shortest driving distance between El Paso and Corpus Christi. All sections, existing and proposed,
    allow for bi-directional traffic.

    Solution: First, we use Floyd-Warshall's APSP algorithm to compute all pairs of shortest paths distances in
    O(n^3) time. Then, we use a 2D array, table[i][j], to denote shortest path distances for each pair of cities
    i and j. Each proposal section p is a pair of cities (x,y). The best we can do by using proposal section p is
    min(S(a,b), S(a,x)+d(x,y)+S(y,b), S(a,y)+d(y,x)+S(x,b)) where d(x,y) is the distance of the proposed highway
    section p between x and y, and a and b are El Paso and Corpus Christi, respectively. This computation is O(1)
    time, so we can evaluate all the proposals in time proportional to the number of proposals after we have computed
    the shortest path between each pair of cities. This results in an O(n^3 + k) time complexity, k meaning the
    number of proposed sections; since k<=n(n-1)/2, the time complexity is O(n^3).
    """

    @classmethod
    def find_shortest_distance(cls, existing_sections, proposed_sections, num_cities, city1, city2):

        def FloydWarshall_APSP(graph):  # O(n^3) time
            n = len(graph.table)
            dp = copy.deepcopy(graph.table)
            for k in xrange(n):
                for i in xrange(n):
                    for j in xrange(n):
                        if dp[i][k] != sys.maxint and dp[k][j] != sys.maxint and \
                            dp[i][j] > dp[i][k] + dp[k][j]:
                            dp[i][j] = dp[i][k] + dp[k][j]
            return dp

        # construct a graph for the highways
        graph = Graph(num_cities)
        for section in existing_sections:
            graph.table[section.x][section.y] = graph.table[section.y][section.x] = section.distance

        # compute the minimum distances between each pair of cities based on the existing highways
        table = FloydWarshall_APSP(graph)
        # get the minimum distance between city1 and city2 in the current highway network
        min_distance_city1_city2 = table[city1][city2]

        # find the best proposed section which can minimize the current distance between city1 and city2
        best_proposed_section = None
        for section in proposed_sections:
            # checks the path of city1 -> section.x -> section.y -> city2
            if table[city1][section.x] != sys.maxint and table[section.y][city2] != sys.maxint and \
                min_distance_city1_city2 > table[city1][section.x]+table[section.x][section.y]+table[section.y][city2]:
                min_distance_city1_city2 = table[city1][section.x]+table[section.x][section.y]+table[section.y][city2]
                best_proposed_section = section

            # checks the path of city1 -> section.y -> section.x -> city2
            if table[city1][section.y] != sys.maxint and table[section.x][city2] != sys.maxint and \
                min_distance_city1_city2 > table[city1][section.y]+table[section.y][section.x]+table[section.x][city2]:
                min_distance_city1_city2 = table[city1][section.y]+table[section.y][section.x]+table[section.x][city2]
                best_proposed_section = section

        return best_proposed_section


class TestRun(unittest.TestCase):

    def test_case1(self):
        section1 = HighwaySection(0, 1, 5)
        section2 = HighwaySection(0, 3, 9)
        section3 = HighwaySection(0, 4, 2)
        section4 = HighwaySection(1, 2, 2)
        section5 = HighwaySection(2, 3, 3)
        section6 = HighwaySection(3, 5, 2)
        section7 = HighwaySection(4, 5, 3)
        existing_sections = [section1, section2, section3, section4, section5, section6, section7]

        new_section1 = HighwaySection(1, 3, 1)
        new_section2 = HighwaySection(3, 4, 5)
        proposed_sections = [new_section1, new_section2]

        actual_result = Elements.find_shortest_distance(existing_sections, proposed_sections, 6, city1=0, city2=3)
        unittest.TestCase.assertEqual(self, first=new_section1, second=actual_result)


if __name__ == "__main__":
    unittest.main()


