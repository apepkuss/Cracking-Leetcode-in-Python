import unittest

class Elements(object):

    @classmethod
    def find_path_to_exit(cls, matrix):

        def dfs(matrix, i, j, path):
            if i==len(matrix)-1 and j==len(matrix[0])-1:
                path.append((i,j))
                res.append(path)
                return

            matrix[i][j] = -1

            if len(res)==0 and j>0 and matrix[i][j-1]==1:
                dfs(matrix, i, j-1, path+[(i,j)])
            if len(res)==0 and i>0 and matrix[i-1][j]==1:
                dfs(matrix, i-1, j, path+[(i,j)])
            if len(res)==0 and j<len(matrix[0])-1 and matrix[i][j+1]==1:
                dfs(matrix, i, j+1, path+[(i,j)])
            if len(res)==0 and i<len(matrix)-1 and matrix[i+1][j]==1:
                dfs(matrix, i+1, j, path+[(i,j)])

            if len(res) == 0:
                matrix[i][j] = 1
            else:
                return

        res = []
        dfs(matrix, 0, 0, [])
        return res


class TestRun(unittest.TestCase):

    def test_case1(self):
        matrix = [[1,1,1,1,1], [0,1,0,0,1], [0,1,0,1,0], [1,1,1,1,0], [1,0,0,1,1]]
        actual = Elements.find_path_to_exit(matrix)
        expected = [[(0,0),(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(4,3),(4,4)]]
        unittest.TestCase.assertEqual(self, first=expected, second=actual)


if __name__ == "__main__":
    unittest.main()