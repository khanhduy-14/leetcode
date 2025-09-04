class Solution {
public:
    int findClosest(int x, int y, int z) {
        return abs(y-z) < abs(x-z) ? 2 : abs(y-z) > abs(x-z);
    }
};