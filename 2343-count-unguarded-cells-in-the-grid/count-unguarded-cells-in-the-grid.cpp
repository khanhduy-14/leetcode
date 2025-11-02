class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<int>> grid(m, vector<int>(n));
        // 0=free, 1=guard, 2=wall,3=guardable
        for(vector<int> row: guards) {
            grid[row[0]][row[1]] = 1;
        }
        for(vector<int> row: walls) {
            grid[row[0]][row[1]] = 2;
        }

        for(vector<int> guard: guards) {
            for(int i=guard[0]+1; i<m; i++) {
                if(grid[i][guard[1]] == 1 ||grid[i][guard[1]] ==2) {
                    break;
                }
                grid[i][guard[1]] = 3;
            }
            for(int i=guard[0]-1; i>=0; i--) {
                if(grid[i][guard[1]] == 1 ||grid[i][guard[1]] ==2) {
                    break;
                }
                grid[i][guard[1]] = 3;
            }
            for(int i=guard[1]+1; i<n; i++) {
                if(grid[guard[0]][i] == 1 || grid[guard[0]][i] ==2) {
                    break;
                }
                grid[guard[0]][i] = 3;
            }
            for(int i=guard[1]-1; i>=0; i--) {
                if(grid[guard[0]][i] == 1 || grid[guard[0]][i] ==2) {
                    break;
                }
                grid[guard[0]][i] = 3;
            }
        }

        int res = 0;

        for (vector<int> row:grid) {
            for(int cell: row) {
                if (cell == 0) {
                    res+=1;
                } 
            }
        }
        return res;
    }
};