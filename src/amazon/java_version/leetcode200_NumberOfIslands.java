

public class Solution {

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0)
            return 0;

        int m = grid.length;
        int n = grid[0].length;

        // store parent id of each id
        int[] parent = new int[m*n];
        for (int i=0; i<m*n; i++) {
            parent[i] = i;
        }

        // count the number of '1'
        int trees = 0;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == '1') {
                    trees++;
                }
            }
        }

        // count the number of islands
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == '0') {
                    continue;
                }

                int u = i * n + j;
                int v = 0;
                // check top cell
                if (i>0 && grid[i-1][j] == '1') {
                    v = u - n;
                    if (union(u, v, parent)) {
                        trees--;
                    }
                }

                // check bottom cell
                if (i<m-1 && grid[i+1][j] == '1') {
                    v = u + n;
                    if (union(u, v, parent)) {
                        trees--;
                    }
                }

                // check left cell
                if (j>0 && grid[i][j-1] == '1') {
                    v = u - 1;
                    if (union(u, v, parent)) {
                        trees--;
                    }
                }

                // check right cell
                if (j<n-1 && grid[i][j+1] == '1') {
                    v = u + 1;
                    if (union(u, v, parent)) {
                        trees--;
                    }
                }
            }
        }

        return trees;
    }

    // merge two neighbor ids into the same tree, if they have
    // different root ids.
    private boolean union(int u, int v, int[] parent) {
        int uu = find(u, parent);
        int vv = find(v, parent);

        if (uu == vv) {
            return false;
        }

        parent[uu] = parent[vv];
        return true;
    }

    // find the parent id of a specified id, u
    private int find(int u, int[] parent) {
        if (parent[u] != parent[parent[u]]) {
            parent[u] = find(parent[u], parent);
        }

        return parent[u];
    }
}