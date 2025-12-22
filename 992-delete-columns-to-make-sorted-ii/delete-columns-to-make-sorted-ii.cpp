class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int res = 0;
        vector<bool> sorted(strs.size() - 1, false);
        for(int i = 0; i < strs[0].size(); i++) {
            int is_unsorted = 0;
            for (int j = 1; j < strs.size(); j++ ){
                if(!sorted[j] && strs[j][i] < strs[j-1][i]) {
                    is_unsorted = 1;
                    break;
                }
            }
            if (is_unsorted == 1) {
              res++;
              continue;
            }


            for (int j = 1; j < strs.size(); j++) {
                if (!sorted[j] &&  strs[j][i] > strs[j-1][i]) {
                    sorted[j] = true;
                }
            }
        }
        return res;
    }
};
