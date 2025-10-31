class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        set<int> s;
        vector<int> res;
        for (int num: nums) {
            if (s.count(num)) {
                res.push_back(num);
            }
            if (res.size() == 2) {
                break;
            }
            s.insert(num);
        }
        return res;
    }
};