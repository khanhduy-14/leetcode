class Solution {
public:
    int smallestNumber(int n) {
        if (n == 1) return 1;
        int res = 1;
        while (res <= n) {
            res = res << 1;
        }
        return res - 1;
    }
};