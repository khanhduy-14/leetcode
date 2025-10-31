class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        int XOR = 0;
        int i = 0;
        while (i < nums.size()) {
            XOR ^= nums[i];
            if (i < (nums.size() - 2)) {
                XOR ^= i;
            }
            i++;
        }
        int right_most = XOR & -XOR, a = 0, b=0;
        i=0;
        while (i < nums.size()) {
            if((nums[i] & right_most) == 0) {
                a^=nums[i];
            } else {
                b^=nums[i];
            }
            if (i < (nums.size() - 2)) {
                if((i & right_most) == 0) {
                    a^=i;
                } else {
                    b^=i;
                }
            }
            cout <<" " << a << " " << b;
            i++;
        }
        return {a,b};
    }
};