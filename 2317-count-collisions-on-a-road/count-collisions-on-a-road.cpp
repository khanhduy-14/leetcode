class Solution {
public:
    int countCollisions(string directions) {
        int n = directions.size(), i = 0, j = n - 1;
        while (i < n && directions[i] == 'L') i++;   
        while (j >= 0 && directions[j] == 'R') j--;   
        
        int ans = 0;
        for (i; i<=j; i++)
            if (directions[i] != 'S') ans++;
        return ans;
    }
};