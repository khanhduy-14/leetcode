class Solution {

public:
    int minDeletionSize(vector<string>& strs) {
        int res = 0;
        for(int i = 0; i < strs[0].size(); i++) {
            int is_unsorted = 0;
            for (int j = 1; j < strs.size(); j++ ){
                if(strs[j][i] < strs[j-1][i]) {
                    is_unsorted = 1;
                    break;
                }
            }
            res += is_unsorted;
        }
        return res;
    }
};
